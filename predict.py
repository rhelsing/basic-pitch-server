from cog import BasePredictor, Input, Path
import tensorflow as tf
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

import os
import string
import random

class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        self.model = tf.saved_model.load(str(ICASSP_2022_MODEL_PATH))

    def predict(
        self,
        audio_file: Path = Input(description="Wav file"),
        # scale: float = Input(description="Factor to scale image by", ge=0, le=10, default=1.5),
    ) -> Path:
        """Run a single prediction on the basic_pitch model"""

        # TODO:  make these input parameters
        onset_threshold = None
        frame_threshold = None
        minimum_note_length = None
        minimum_frequency = None
        maximum_frequency = None

        model_output, midi_data, note_activations = predict(
          audio_path=p,
          model_or_model_path=self.model,
          onset_threshold = (onset_threshold or 0.6),
          frame_threshold = (frame_threshold or 0.4),
          minimum_note_length = (minimum_note_length or 100),
          minimum_frequency = (minimum_frequency or 200.0),
          maximum_frequency = (maximum_frequency or 8000.0),
        )

        # TODO: how to return a file correctly with cog
        if not os.path.exists("saved_midi"):
          os.makedirs("saved_midi")

        letters = string.ascii_lowercase
        file_name = ''.join(random.choice(letters) for i in range(10))
        m = 'saved_midi/'+file_name+'.mid'
        midi_data.write(m)
        return Path(m)
