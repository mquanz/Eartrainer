print('Welcome to EARTRAINER - developed by Richard and Martin!')

import simpleaudio as sa
import os
import random

sounds = os.listdir('../media')

media = random.choice(sounds)
wave_obj = sa.WaveObject.from_wave_file("../media/" + media)
play_obj = wave_obj.play()
play_obj.wait_done()

print(media)
