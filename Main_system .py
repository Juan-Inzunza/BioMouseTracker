import serial
import time

port = serial.Serial("/dev/rfcomm1", baudrate=9600)

while True:
    
    if(port.in_waiting > 0):
        data = port.readline()
        print(data)
    time.sleep(3)
