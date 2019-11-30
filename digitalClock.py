import tkinter as tk
import time

def update_time():
    now = time.strftime('%H:%M:%S')
    label1['text'] = now
    root.after(1000, update_time)

def change_colour():
    if label1['fg'] == 'white':
        label1['fg'] = 'black'
        label1['bg'] = 'white'
    else:
        label1['fg'] = 'white'
        label1['bg'] = 'black'

root = tk.Tk()
label1 = tk.Label(root, bg = 'black', fg = 'white', width = 10)
label1.grid(row = 0, column = 0)
button1 = tk.Button(root, width = 10, text = 'Start Clock', command = update_time)
button1.grid(row = 0, column = 1)
button2 = tk.Button(root, width = 10, text = 'Quit', command = quit)
button2.grid(row = 1, column = 0)
button3 = tk.Button(root, width = 10, text = 'Switch colour', command = change_colour)
button3.grid(row = 1, column = 1)
# button2.pack(side = tk.BOTTOM)
root.mainloop()