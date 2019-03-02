import simpleaudio as sa
import os
import random

print("Hello, do you want to train? Enter 'y' for Yes or 'n' for No")
user_input = input(">")
if user_input == "y":
    sounds = os.listdir("../media")

    media = random.choice(sounds)
    wave_obj = sa.WaveObject.from_wave_file("../media/" + media)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    user_guess = input("What did you hear?")
    if user_guess == media[0:len(media)-4]:
        print("right, it's " + media)
    else:
        print("wrong")


