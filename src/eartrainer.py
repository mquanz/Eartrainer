print('Welcome to EARTRAINER - developed by Richard and Martin!')

import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("../media/test.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
