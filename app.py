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
# curl  -F api_key=XXXXX -F 'f=@example_wav/example.wav' 10.0.0.124:5000/upload

@app.route('/upload', methods=['POST'])
def upload_file():
  if request.method == 'POST':
    f = request.files['f']
    letters = string.ascii_lowercase
    file_name = ''.join(random.choice(letters) for i in range(10))
    p = 'uploads/'+file_name+'.wav'

    if request.form.get('api_key') != os.getenv('API_KEY'):
      return "<h1>Error</h1>"

    onset_threshold = request.form.get('onset_threshold')
    if onset_threshold != None:
      onset_threshold = float(onset_threshold)
    frame_threshold = request.form.get('frame_threshold')
    if frame_threshold != None:
      frame_threshold = float(frame_threshold)
    minimum_note_length = request.form.get('minimum_note_length')
    if minimum_note_length != None:
      minimum_note_length = int(minimum_note_length)
    minimum_frequency = request.form.get('minimum_frequency')
    if minimum_frequency != None:
      minimum_frequency = float(minimum_frequency)
    maximum_frequency = request.form.get('maximum_frequency')
    if maximum_frequency != None:
      maximum_frequency = float(maximum_frequency)

    if not os.path.exists("uploads"):
      os.makedirs("uploads")

    f.save(p)
    model_output, midi_data, note_activations = predict(
      audio_path=p,
      model_or_model_path=basic_pitch_model,
      onset_threshold = (onset_threshold or 0.6),
      frame_threshold = (frame_threshold or 0.4),
      minimum_note_length = (minimum_note_length or 100),
      minimum_frequency = (minimum_frequency or 200.0),
      maximum_frequency = (maximum_frequency or 8000.0),
    )

    # onset-threshold - lower a -default=0.5,
    # frame-threshold - longer =0.3
    # minimum-note-length - in ms 58
    # minimum-frequency in hz
    # maximum-frequency in hz

    if not os.path.exists("saved_midi"):
      os.makedirs("saved_midi")

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
