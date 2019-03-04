import tkinter as tk
from tkinter import messagebox
import simpleaudio as sa
import os
import random


class Window:
    
    media = ""
    
    def __init__(self, master):
        self.master = master
        master.title('Eartrainer')
        
        self.label1 = tk.Label(master, text = 'Welcome to the famous Eartrainer - created by M & R', font = ('Times', 14), bd = 15)
        self.label1.grid(row = 0, columnspan = 2)

        self.repeat_button = tk.Button(master, text = 'Repeat Interval', command = self.Repeat_Interval)
        self.repeat_button.grid(row = 2, column = 1)
        
        self.play_button = tk.Button(master, text = 'Play new Interval', command = self.Play_Interval)
        self.play_button.grid(row = 2, column = 2)

        self.entry = tk.Entry(master, width = 32, fg = 'grey')
        self.entry.insert(0, 'Enter your guess here...')
        self.entry.bind('<Button-1>', lambda event: self.entry_click(event, 'Enter your guess here...'))
        self.entry.bind('<Return>', lambda event: self.Control())
        self.entry.grid(row = 1)
    
    def Repeat_Interval(self):
        wave_obj = sa.WaveObject.from_wave_file("../media/" + media)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print(media)
    
    def Play_Interval(self):
        sounds = os.listdir("../media")
        global media
        media = random.choice(sounds)
        wave_obj = sa.WaveObject.from_wave_file("../media/" + media)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print(media)

    def Control(self):
        user_input = self.entry.get() + ".wav"
        if user_input == media:
            messagebox.showinfo('Ergebnis', 'Well done, it was ' + media + '! :)')
        else:
            messagebox.showinfo('Ergebnis', 'Youre wrong, it was ' + media + '! :(')
#        self.entry.delete(0, tk.END)

    def entry_click(self, event, default_text):
        if self.entry.get() == default_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg = 'black')



root = tk.Tk()
create_window = Window(root)
root.mainloop()
