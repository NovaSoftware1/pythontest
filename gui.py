import tkinter as tk
from tkinter import messagebox
from tkinter import Button

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")


def helloCallback():
  msg = messagebox.showinfo("Hello Python", "Hello World")


btn = Button(window, text="Hello", command=helloCallback)
btn.place(x=50, y=50)

tk.mainloop()
