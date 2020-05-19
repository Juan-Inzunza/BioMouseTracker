import serial
import time

port = serial.Serial("/dev/rfcomm2", baudrate=9600)
port.flush() # This wil flush any input and output buffer, so it will
#avoid receiving or sending bad data

while True:
    
    if(port.in_waiting > 0):
        data = port.readline().decode('utf-8').rstrip() # decode will translate
        #the data from unicode to byte
        print(data)
