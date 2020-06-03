import RPi.GPIO as GPIO
import time
import tkinter as tk
from tkinter import *
root = Tk()
root.title("Movement")
root.geometry("900x600")
root.config(bg = "grey")

MainFrame = Frame(root, bg = 'white')
MainFrame.grid()

HeadFrame = Frame(MainFrame, bd = 1, padx= 200, pady = 10,
                  bg = 'white', relief = RIDGE)
HeadFrame.pack(side = TOP)
ITitle = Label(HeadFrame, font = ('arial', 10), fg = 'blue',
                    text = 'current readings cages 1-16 with time every 3 seconds.',
               bg = 'white')
ITitle.grid()

# frame for current data display
MiddleFrame = Frame(root, bd = 1, padx = 30, pady = 10,
                    bg = 'grey' , relief = RIDGE)
MiddleFrame.grid()


label1 = Label(MiddleFrame)
label2 = Label(MiddleFrame)


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
   
GPIO.setup(11, GPIO.OUT) #s0
GPIO.setup(13, GPIO.OUT) #s1
GPIO.setup(15, GPIO.OUT) #s2
GPIO.setup(16, GPIO.OUT) #s3
GPIO.setup(22, GPIO.OUT) #enable
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Signal Input

s0 = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] #s0 values
s1 = [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1] #s1 values
s2 = [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1] #s2 values
s3 = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1] #s3 values

GPIO.output(22,GPIO.LOW)

def s0_pin(x,y):
    GPIO.output(x,y)

def s1_pin(x,y):
    GPIO.output(x,y)
    
def s2_pin(x,y):
    GPIO.output(x,y)

def s3_pin(x,y):
    GPIO.output(x,y)

def current_readings():
    signal_reading = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    times = []
    for i in range(16): 
        s0_pin(11,s0[i])
        s1_pin(13,s1[i])
        s2_pin(15,s2[i])
        s3_pin(16,s3[i])
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        times.append(current_time)
        if GPIO.input(18):
            signal_reading[i] = 0
        else:
            signal_reading[i] = 1
            
    global label1
    global label2

    label1.destroy()
    label2.destroy()

    label1 = Label(MiddleFrame, font = ('arial', 10), text  = signal_reading,
                   fg = 'black', bg='grey')
    label1.pack(side = LEFT, fill = 'both')
    label2 = Label(MiddleFrame, font = ('arial', 10), text = times[1],
                   fg = 'black', bg = 'grey')
    label2.pack(side = RIGHT)
    root.after(3000, current_readings)
        
def previous_readings(readings_list):
    old_readings.append(readings_list)
    if len(old_readings) > 5:
        old_readings.pop(0)
    return old_readings

def previous_times(times_list):
    old_times.append(times_list)
    if len(old_times) > 5:
        old_times.pop(0)
    return old_times

root.after(3000, current_readings)
root.mainloop()

