from pyfirmata import Arduino, SERVO, util
from time import sleep
import keyboard
from constants import *
import numpy as np
import threading


class Control: 
    def __init__(self):
        
        board = Arduino(self.port)

        # board.digital[SERVO0].mode = SERVO
        board.digital[SERVO1].mode = SERVO
        board.digital[SERVO2].mode = SERVO
        board.digital[SERVO3].mode = SERVO
        board.digital[SERVO4].mode = SERVO
        # board.digital[SERVO5].mode = SERVO

    
    def holdUpFinger(self, holdup_servonum):
        threads = []
        for i in SERVOLIST:
            if i is not holdup_servonum:
                threads.append(i)
        for th in threads:
            th.start()
        for th in threads:
            th.join()
        
            

    def run(self, hand_state):      
        if hand_state == OPEN:
            self.board.digital[SERVO1].write(0)
            self.board.digital[SERVO2].write(0)
            self.board.digital[SERVO3].write(0)
            self.board.digital[SERVO4].write(0)
            # self.board.digital[SERVO5].write(0)

        if hand_state == INDEX:
            self.holdUpFinger(SERVO1)        
        if hand_state == MIDDLE:
            self.holdUpFinger(SERVO2)
        if hand_state == RING:
            self.holdUpFinger(SERVO3)
        if hand_state == PINKY:
            self.holdUpFinger(SERVO4)
        if hand_state == THUMB:
            self.holdUpFinger(SERVO5)
        
        if hand_state == CLENCHED:
            self.lerp(0, 180, SERVO1)
            self.lerp(0, 180, SERVO2)
            self.lerp(0, 180, SERVO3)
            self.lerp(0, 180, SERVO4)
            self.lerp(0, 180, SERVO5)

            # self.board.digital[SERVO1].write(180)
            # self.board.digital[SERVO2].write(180)
            # self.board.digital[SERVO3].write(180)
            # self.board.digital[SERVO4].write(180)
            # self.board.digital[SERVO5].write(180)


    def lerp(self, start_angle, end_angle, servonum):
        t_array = np.linspace(0,1,TIME_DIVISIONS)
        for t in t_array:
            angle = (1-t)*(start_angle) + t*(end_angle)
            self.board.digital[servonum].write(angle)
            sleep(SERVO_DELAY)

