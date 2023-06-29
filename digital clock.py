from tkinter import Tk
import time
from tkinter import Label

def present_time():
    dispay_time = time.strftime("%H:%M:%S %p")
    clock_type.configure(text = dispay_time)
    clock_type.after(1000, present_time)

digi_clock = Tk()
digi_clock.title("Digital clock")

clock_type = Label(digi_clock, font = ("arial", 100), bg = "grey", fg = "white")
clock_type.pack()
    
present_time()

digi_clock.mainloop()    

