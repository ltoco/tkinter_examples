import tkinter as tk

def buttonClickEvent(b, label):
    # label.config(text='Button ' + str(b) + ' is pressed')
    # print(b._name)
    label['text'] = label['text'] + '\n' + b['text'] + ' is pressed'

root = tk.Tk()

label = tk.Label(root)
label.grid(row = 3, column = 0)
button1 = tk.Button(root, text = 'Button 1')
button1.configure(command = lambda b = button1: buttonClickEvent(b, label))
button1.grid(row = 0, column = 0)
button2 = tk.Button(root, text = 'Button 2', command = buttonClickEvent)
button2.configure(command = lambda : buttonClickEvent(button2, label))
button2.grid(row = 1, column = 0)
button5 = tk.Button(root, text ='Button 5', command = buttonClickEvent)
button5.configure(command = lambda : buttonClickEvent(button5, label))
button5.grid(row = 2, column = 0)

root.mainloop()