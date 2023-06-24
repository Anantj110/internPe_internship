from tkinter import *
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox 

alarm_clock = Tk()
alarm_clock.title("Alarm clock")
alarm_clock.geometry("300x260")

alarmtime = StringVar()
msgi = StringVar()

head = Label(alarm_clock, text = "Alarm clock", font = ('calibri', 20))
head.grid(row = 0, columnspan = 3, pady = 10)

mixer.init()

def alarmC():
    ac = alarmtime.get()
    
    AlarmT= ac
    currentT = time.strftime("%H:%M")
    
    while AlarmT != currentT:
        currentT = time.strftime("%H:%M")
    
    if AlarmT == currentT: 
        msg = messagebox.showinfo('Info', f'{msgi.get()}')
        mixer.music.load('Alarm-Fast-A1-www.fesliyanstudios.com')
        mixer.music.play() 
        if msg == 'ok':
            mixer.music.stop()
    
inputt = Label(alarm_clock, text = "Input time", font = ('calibri',20))
inputt.grid(row = 1, column = 1)

altime = Entry(alarm_clock, textvariable = alarmtime, font = ('calibri',15))
altime.grid(row = 1, column = 2)

message = Label(alarm_clock, text = "Message", font = ('calibri', 20))
message.grid(row = 2, column = 1, columnspan = 2)

inpmsg = Entry(alarm_clock, textvariable = msgi, font = ('calibri', 15))
inpmsg.grid(row = 3, column = 1, columnspan = 3)

save = Button(alarm_clock, text = "Save", font = ('calibri', 20))
save.grid(row = 4, column = 1, columnspan = 2)

alarm_clock.mainloop()
