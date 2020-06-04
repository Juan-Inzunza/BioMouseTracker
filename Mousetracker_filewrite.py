import RPi.GPIO as GPIO
import time
from datetime import date

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
    return signal_reading, times

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

cage_totals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

try:
    today = date.today()
    today_now = str(today)
    now = time.localtime()
    time_now = time.strftime("%H:%M:%S", now)
    results = open("MCRs"+today_now+"_"+time_now+".txt", "a+")
    results.write("Mouse Cage Reading results for: " + today_now + "(Year/Month/Day)\n")
    results.write("This file displays and records information on mouse movement for cages who return a 1 (i.e. the mouse set off the sensor) on a predefined time interval (currently 5 seconds)\n")
    results.write("Total mouse movements will be displayed as a running total at the end of this file for each cage\n")
    while True:
        old_readings = []
        old_times = []
        present_readings, present_time = current_readings()
        results.write("\n")
        results.write("Cage     Movement     Time\n")
        print("Multiplexer readings: ")
        print("----------------------")
        for i in range(16):
          print(i," = ", s0[i],s1[i],s2[i],s3[i],"Reading: ",present_readings[i], " at time: ", present_time[i])
          cage_totals[i] = cage_totals[i] + present_readings[i]
          if present_readings[i] == 1:
              results.write(str(i) + "   " + str(present_readings[i]) + "   " + str(present_time[i])+"\n")
        print("-----------------------")
        results.write("\n")
        time.sleep(5)
        old_readings = previous_readings(present_readings)
        old_times = previous_times(present_time)
        print()
        print("Here are the previous readings: ", old_readings)
        print("Here are the previous times: ", old_times)
except KeyboardInterrupt:
    results.write("\n")
    results.write("Here are the cage totals for the run-time of this experiment\n")
    results.write("Cage     # of times moved\n")
    for i in range(16):
        results.write(str(i) + "    " + str(cage_totals[i])+"\n")
    results.close()
    GPIO.cleanup()
