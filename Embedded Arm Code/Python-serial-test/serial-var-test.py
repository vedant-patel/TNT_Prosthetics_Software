import serial
L = 0
M = 1
R = 0

# Set up the serial:

ser = serial.Serial(port='COM3', baudrate=57600, timeout=1)
ser.reset_input_buffer()

# Send the signal through the serial:
ser.read_until("\n",1)