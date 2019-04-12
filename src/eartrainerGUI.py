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
        
        # Possible rows for placement of checkbuttons are 3, 4 and 5.
        rows = [3,4,5]
        # True answer will be placed randomly.
        truerow = random.choice(rows)
        # Remove true row from list for placement of wrong checkbuttons.
        rows.remove(truerow)
        # Create list without true answer for labels of wrong heckbuttons and shuffle it.
        labels = random.sample([x for i,x in enumerate(media) if i!=counter], len(media)-1)
        # Checkbox1 always contains true answer.
        self.checkbox1 = tk.IntVar()
        tk.Checkbutton(text = media[counter], variable = self.checkbox1).grid(row = truerow)
        self.checkbox2 = tk.IntVar()
        tk.Checkbutton(text = labels[0], variable = self.checkbox2).grid(row = rows[0])
        self.checkbox3 = tk.IntVar()
        tk.Checkbutton(text = labels[1], variable = self.checkbox3).grid(row = rows[1])

    def Control(self):
        user_input = self.checkbox1.get()
        if user_input == 1:
            messagebox.showinfo('Result', 'Well done, it was ' + media[counter] + '! :)')
        else:
            messagebox.showinfo('Result', 'Youre wrong, it was ' + media[counter] + '! :(')
        
    def entry_click(self, event, default_text):
            self.entry.delete(0, tk.END)
            self.entry.config(fg = 'black')

root = tk.Tk()
create_window = Window(root)
root.mainloop()
