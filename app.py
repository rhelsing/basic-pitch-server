import os
import base64
import string
import random

from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve

import tensorflow as tf
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

basic_pitch_model = tf.saved_model.load(str(ICASSP_2022_MODEL_PATH))

app = Flask(__name__)

# APP USAGE:
# flask run --with-threads --host=0.0.0.0
# curl -F 'f=@example_wav/example.wav' 10.0.0.124:5000/upload

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    f = request.files['f']
    letters = string.ascii_lowercase
    file_name = ''.join(random.choice(letters) for i in range(10))
    p = 'uploads/'+file_name+'.wav'
    f.save(p)
    model_output, midi_data, note_activations = predict(
      p,
      basic_pitch_model,
    )

    m = 'saved_midi/'+file_name+'.mid'
    midi_data.write(m)
    midi_file = open(m,"rb")
    midi_data_binary = midi_file.read()
    midi_data_e = (base64.b64encode(midi_data_binary)).decode('ascii')
    d = {'midi': midi_data_e}

    if os.path.exists(p):
      os.remove(p)
    if os.path.exists(m):
      os.remove(m)

    return jsonify(d)

@app.route("/")
def index():
    return "<h1>Hello!</h1>"

serve(app, host='0.0.0.0', port=os.getenv('PORT'))
