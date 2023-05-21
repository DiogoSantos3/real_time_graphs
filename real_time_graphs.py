import serial
from serial import SerialException
import matplotlib.pyplot as plt
from drawnow import *

portName = 'COM3'
baudrateNum = 19200
plt.ion() #tell matplotlib you want interactive mode to plot live data


tempF = []
pressF = []
altF = []
ser = serial.Serial(port=portName,baudrate=baudrateNum)

def make_fig(): #make a plot
  plt.plot(tempF,'ro-')

while True:
   while (ser.in_waiting == 0):
    ser_data = (ser.readline().replace(b'\n', b' ').replace(b'\r', b' ').strip().decode('utf-8'))
    data_array = ser_data.split(',') #0-temp, 1-press, 2-alt
    temp = float(data_array[0])
    press = float(data_array[1])
    alt = float(data_array[2])
    tempF.append (temp)
    pressF.append(press)
    altF.append(alt)
    drawnow(make_fig)
    plt.pause(.000001)
        