import tkinter as tk
from tkinter import messagebox
import simpleaudio as sa
import os
import random

media = random.sample(os.listdir("../media"), len(os.listdir("../media")))
counter = 0

class Window:
    
    def __init__(self, master):
        self.master = master
        master.title('Eartrainer')
        
        self.label1 = tk.Label(master, text = 'Welcome to the famous Eartrainer - created by M & R', font = ('Times', 14), bd = 15)
        self.label1.grid(row = 0, columnspan = 2)
        
        self.previous_button = tk.Button(master, text = 'PREVIOUS', command = self.Previous_Interval)
        self.previous_button.grid(row = 2, column = 1)
        
        self.play_button = tk.Button(master, text = 'PLAY', command = self.Play_Interval)
        self.play_button.grid(row = 2, column = 2)
        
        self.next_button = tk.Button(master, text = 'NEXT', command = self.Next_Interval)
        self.next_button.grid(row = 2, column = 3)
        
        self.check_button = tk.Button(master, text = 'CHECK', bg = 'orange', command = self.Control)
        self.check_button.grid(row = 1, column = 1)

        self.entry = tk.Entry(master, width = 32, fg = 'grey')
        self.entry.insert(0, 'Enter your guess here...')
        self.entry.bind('<Button-1>', lambda event: self.entry_click(event, 'Enter your guess here...'))
        self.entry.bind('<Return>', lambda event: self.Control())
        self.entry.grid(row = 1)
    
    def Previous_Interval(self):
        global counter
        if counter > 0:
            counter -= 1
            print(media, media[counter])
        else:
            messagebox.showinfo('Error', 'Counter too low')
            counter = 0

    def Next_Interval(self):
        global counter
        counter += 1
        print(media, media[counter])

    def Play_Interval(self):
        wave_obj = sa.WaveObject.from_wave_file("../media/" + media[counter])
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print(media, media[counter])

    def Control(self):
        user_input = self.entry.get() + ".wav"
        try:
            if user_input == media[counter]:
                messagebox.showinfo('Result', 'Well done, it was ' + media[counter] + '! :)')
            else:
                messagebox.showinfo('Result', 'Youre wrong, it was ' + media[counter] + '! :(')
        except NameError:
                    messagebox.showinfo('Error', 'Enter your guess first')
        
    def entry_click(self, event, default_text):
        if self.entry.get() == default_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg = 'black')

root = tk.Tk()
create_window = Window(root)
root.mainloop()
