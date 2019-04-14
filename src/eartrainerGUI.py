import tkinter as tk
from tkinter import messagebox
import simpleaudio as sa
import os
import random

media = random.sample(os.listdir("../media"), len(os.listdir("../media")))
dic = {'C1.wav':'kl. Sekunde', 'C4.wav':'gr. Terz', 'C6.wav':'verm. Quinte', 'C7.wav':'r. Quinte'}
counter = 0

class Window:
    
    def __init__(self, master):
        self.master = master
        master.title('Eartrainer')
        
        self.label1 = tk.Label(master, text = 'Welcome to the famous Eartrainer - created by M & R', font = ('Times', 14), bd = 18)
        self.label1.grid(row = 0, columnspan = 2)
        
        self.previous_button = tk.Button(master, text = 'PREVIOUS', bg = 'grey', bd = 5, command = self.Previous_Interval)
        self.previous_button.grid(row = 1, column = 0)
        
        self.play_button = tk.Button(master, text = 'PLAY', bg = 'green', bd = 5, command = self.Play_Interval)
        self.play_button.grid(row = 1, column = 1)
        
        self.next_button = tk.Button(master, text = 'NEXT', bg = 'grey', bd = 5, command = self.Next_Interval)
        self.next_button.grid(row = 1, column = 2)
        
        self.check_button = tk.Button(master, text = 'CHECK', bg = 'orange', bd = 5, command = self.Check_Answer)
        self.check_button.grid(row = 2, column = 1)
        
        self.create_checkboxes()

    def Previous_Interval(self):
        global counter
        if counter > 0:
            counter -= 1
            print(media, media[counter])
            self.create_checkboxes()
        else:
            messagebox.showinfo('Error', 'Counter too low')
            counter = 0

    def Next_Interval(self):
        global counter
        if counter < len(media)-1:
            counter += 1
            print(media, media[counter])
            self.create_checkboxes()
        else:
            messagebox.showinfo('End of Trainng', '''Congrats! You've trained hard. List is replaying now.''' )
            counter = 0
            print(media, media[counter])

    def Play_Interval(self):
        wave_obj = sa.WaveObject.from_wave_file("../media/" + media[counter])
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print(media, media[counter])
        
    def Check_Answer(self):
        user_input = [self.checkbox1.get(), self.checkbox2.get(), self.checkbox3.get()]
        # When (only) messagebox1 is true, show right answer.
        if user_input[0] == 1 and user_input[1] == 0 and user_input[2] == 0:
            messagebox.showinfo('Result', 'Well done, it was a ' + dic[media[counter]] + '! :)')
        else:
            messagebox.showinfo('Result', 'You are wrong or tried to enter multiple answers. Please try again.')
            
    def create_checkboxes(self):
        # Possible rows for placement of checkbuttons are 3, 4 and 5.
        rows = [3,4,5]
        # True answer will be placed randomly.
        truerow = random.choice(rows)
        # Remove true row from list for placement of wrong checkbuttons.
        rows.remove(truerow)
        # Create list without true answer for labels of wrong ceckbuttons and shuffle it.
        labels = random.sample([x for i,x in enumerate(media) if i!=counter], len(media)-1)
        # Create checkboxes, checkbox1 always contains true answer.
        self.checkbox1 = tk.IntVar()
        tk.Checkbutton(text = dic[media[counter]], variable = self.checkbox1, bg = 'white', width = 20).grid(row = truerow, sticky = 'w')
        self.checkbox2 = tk.IntVar()
        tk.Checkbutton(text = dic[labels[0]], variable = self.checkbox2, bg = 'white', width = 20).grid(row = rows[0], sticky = 'w')
        self.checkbox3 = tk.IntVar()
        tk.Checkbutton(text = dic[labels[1]], variable = self.checkbox3, bg = 'white', width = 20).grid(row = rows[1], sticky = 'w')


root = tk.Tk()
create_window = Window(root)
root.mainloop()
