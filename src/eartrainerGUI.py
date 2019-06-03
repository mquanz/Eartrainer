import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as tkk
import simpleaudio as sa
import os
import random

media = random.sample(os.listdir("../media"), len(os.listdir("../media")))

dic = {'C0.wav':'1: Prime', 'C1.wav':'2: Sekunde kl.', 'C1r.wav':'2: Sekunde kl.', 'C2.wav':'2: Sekunde gr.','C2r.wav':'2: Sekunde gr.', 'C3.wav':'3: Terz kl.', 'C3r.wav':'3: Terz kl.', 'C4.wav':'3: Terz gr.', 'C4r.wav':'3: Terz gr.', 'C5.wav':'4: Quarte r.', 'C5r.wav':'4: Quarte r.', 'C6.wav':'5: Quinte verm.', 'C6r.wav':'5: Quinte verm.', 'C7.wav':'5: Quinte r.', 'C7r.wav':'5: Quinte r.', 'C8.wav':'6: Sexte kl.', 'C8r.wav':'6: Sexte kl.', 'C9.wav':'6: Sexte gr.', 'C9r.wav':'6: Sexte gr.', 'C10.wav':'7: Septime kl.', 'C10r.wav':'7: Septime kl.', 'C11.wav':'7: Septime gr.', 'C11r.wav':'7: Septime gr.', 'C12.wav':'8: Oktave', 'C12r.wav':'8: Oktave'}
counter = 0

class Window:
    
    def __init__(self, master):
        self.master = master
        master.title('Eartrainer')
        master.bind('<Return>', self.Check_Answer)
        
        self.label1 = tk.Label(master, text = 'Welcome to the famous Eartrainer - created by M & R', font = ('Arial Bold', 14), bg = 'white')
        self.label1.grid(row = 0, columnspan = 3, pady = 20, padx = 10)
        
        self.previous_button = tk.Button(master, text = 'PREVIOUS', bg = 'grey', bd = 5, command = self.Previous_Interval)
        self.previous_button.grid(row = 1, column = 0)
        
        self.play_button = tk.Button(master, text = 'PLAY', bg = 'green', bd = 5, command = self.Play_Interval)
        self.play_button.grid(row = 1, column = 1)
        
        self.next_button = tk.Button(master, text = 'NEXT', bg = 'grey', bd = 5, command = self.Next_Interval)
        self.next_button.grid(row = 1, column = 2)
        
        self.check_button = tk.Button(master, text = 'CHECK', bg = 'orange', bd = 5)
        self.check_button.bind('<Button-1>', lambda event: self.Check_Answer(event))
        self.check_button.grid(row = 2, column = 1, pady = 10)
        
        self.combo = tkk.Combobox(master)
        self.combo['values'] = sorted(list(set([dic[x] for x in media])))
        self.combo.grid(row = 3, columnspan = 3, pady = 10)
        
        self.progress = tkk.Progressbar(master, length = 500)
        self.progress['value'] = 0
        self.progress.grid(row = 4, columnspan = 3, sticky = 'WE')

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
            self.progress['value'] = (counter+1)/len(media) * 100
        else:
            messagebox.showinfo('End of Trainng', '''Congrats! You've trained hard. List is replaying now.''' )
            counter = 0
            self.progress['value'] = 0

    def Play_Interval(self):
        wave_obj = sa.WaveObject.from_wave_file("../media/" + media[counter])
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print(media, media[counter])
        
    def Check_Answer(self, event):
        user_input = self.combo.get()
        if user_input == dic[media[counter]]:
            messagebox.showinfo('Result', 'Well done, it was a ' + dic[media[counter]] + '! :)')
        else:
            messagebox.showinfo('Result', 'You are wrong, please try again.')
        return "break"

root = tk.Tk()
root.configure(background = 'white')
create_window = Window(root)
root.mainloop()
