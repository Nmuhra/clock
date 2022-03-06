from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("live time")

def time():
  string = strftime("%H:%M:%S %P")
  label.config(text=string)
  label.after(1000, time)

wake_up = input("wake up at: ")
label = Label(root, font=("ds-digital", 80), background = "cyan", foreground = "red")
label.pack(anchor="center")
time()
mainloop()
if time == "wake_up":
  print("Wake up")
