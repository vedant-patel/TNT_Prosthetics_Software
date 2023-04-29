from pyfirmata import Arduino, SERVO, util
from time import sleep
import keyboard
import threading
from constants import *
    
board = Arduino(PORT)

board.digital[SERVO0].mode = SERVO
board.digital[SERVO1].mode = SERVO
board.digital[SERVO2].mode = SERVO
board.digital[SERVO3].mode = SERVO
board.digital[SERVO4].mode = SERVO
# board.digital[SERVO5].mode = SERVO

angle = 0
da = 5

def clench_finger(servonum):
    if angle + da < 180:
            angle = angle + da
            board.digital[servonum].write(angle)
            sleep(SERVO_DELAY)

def unclench_finger(servonum):
    if angle - da > 0:
            angle = angle - da
            board.digital[SERVO0].write(angle)
            sleep(SERVO_DELAY)


while True:

    if keyboard.is_pressed('r'):
        clench_finger(SERVO0)
    if keyboard.is_pressed('f'):
        unclench_finger(SERVO0)

    if keyboard.is_pressed('t'):
        clench_finger(SERVO1)
    if keyboard.is_pressed('g'):
        unclench_finger(SERVO1)

    if keyboard.is_pressed('y'):
        clench_finger(SERVO2)
    if keyboard.is_pressed('h'):
        unclench_finger(SERVO2)

    if keyboard.is_pressed('u'):
        clench_finger(SERVO3)
    if keyboard.is_pressed('j'):
        unclench_finger(SERVO3)

    if keyboard.is_pressed('i'):
        clench_finger(SERVO4)
    if keyboard.is_pressed('k'):
        unclench_finger(SERVO4)

        