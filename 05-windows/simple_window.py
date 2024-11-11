from tkinter import Tk, Label, Entry, Button

def clicked():
    data = entry.get()
    label.configure(text=data)

window = Tk()

label = Label(window, text="-")
label.grid(row=0, column=0)
entry = Entry(window)
entry.grid(row=1, column=0)
button = Button(window, text="Click", command=clicked)
button.grid(row=2, column=0)

window.mainloop()