import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import simpleaudio as sa
import os
import random

media = random.sample(os.listdir("../media"), len(os.listdir("../media")))

dic = {'C0.wav':'Prime', 'C1.wav':'kl. Sekunde', 'C1r.wav':'kl. Sekunde', 'C2.wav':'gr. Sekunde','C2r.wav':'gr. Sekunde', 'C3.wav':'kl. Terz', 'C3r.wav':'kl. Terz', 'C4.wav':'gr. Terz', 'C4r.wav':'gr. Terz', 'C5.wav':'r. Quarte', 'C5r.wav':'r. Quarte', 'C6.wav':'verm. Quinte', 'C6r.wav':'verm. Quinte', 'C7.wav':'r. Quinte', 'C7r.wav':'r. Quinte', 'C8.wav':'kl. Sexte', 'C8r.wav':'kl. Sexte', 'C9.wav':'gr. Sexte', 'C9r.wav':'gr. Sexte', 'C10.wav':'kl. Septime', 'C10r.wav':'kl. Septime', 'C11.wav':'gr. Septime', 'C11r.wav':'gr. Septime', 'C12.wav':'Oktave', 'C12r.wav':'Oktave'}
counter = 0

class Window:
    
    def __init__(self, master):
        self.master = master
        master.title('Eartrainer')
        
        self.label1 = tk.Label(master, text = 'Welcome to the famous Eartrainer - created by M & R', font = ('Arial Bold', 14), bd = 18, bg = 'white')
        self.label1.grid(row = 0, columnspan = 2)
        
        self.previous_button = tk.Button(master, text = 'PREVIOUS', bg = 'grey', bd = 5, command = self.Previous_Interval)
        self.previous_button.grid(row = 1, column = 0)
        
        self.play_button = tk.Button(master, text = 'PLAY', bg = 'green', bd = 5, command = self.Play_Interval)
        self.play_button.grid(row = 1, column = 1)
        
        self.next_button = tk.Button(master, text = 'NEXT', bg = 'grey', bd = 5, command = self.Next_Interval)
        self.next_button.grid(row = 1, column = 2)
        
        self.check_button = tk.Button(master, text = 'CHECK', bg = 'orange', bd = 5, command = self.Check_Answer)
        self.check_button.grid(row = 2, column = 1)
        
        self.combo = Combobox(master)
        self.combo['values'] = sorted(list(set([dic[x] for x in media])))
        self.combo.grid(row = 3)

    def Previous_Interval(self):
        global counter
        if counter > 0:
            counter -= 1
        else:
            messagebox.showinfo('Error', 'Counter too low')
            counter = 0

    def Next_Interval(self):
        global counter
        if counter < len(media)-1:
            counter += 1
        else:
            messagebox.showinfo('End of Trainng', '''Congrats! You've trained hard. List is replaying now.''' )
            counter = 0

    def Play_Interval(self):
        wave_obj = sa.WaveObject.from_wave_file("../media/" + media[counter])
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print(media, media[counter])
        
    def Check_Answer(self):
        user_input = self.combo.get()
        if user_input == dic[media[counter]]:
            messagebox.showinfo('Result', 'Well done, it was a ' + dic[media[counter]] + '! :)')
        else:
            messagebox.showinfo('Result', 'You are wrong, please try again.')

root = tk.Tk()
root.configure(background = 'white')
create_window = Window(root)
root.mainloop()
