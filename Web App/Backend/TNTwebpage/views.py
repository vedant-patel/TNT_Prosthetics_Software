from django.shortcuts import render
from django.http import HttpResponse


from pyfirmata import Arduino, SERVO, util
from time import sleep


#Create your views here.
def moveFinger(pin, angle):
    for i in range(0, angle):
        board.digital[pin].write(i)
        sleep(0.005)
    for i in range(angle, 0, -1):
        board.digital[pin].write(i)
        sleep(0.005)


port = 'COM3'
board = Arduino(port)

servo0 = 9  # Thumb
servo1 = 10  # Index
servo2 = 6  # Middle
servo3 = 11  # Ring
# servo4 = 6 #Pinkie
# servo5 = 7 #Wrist

board.digital[servo0].mode = SERVO
board.digital[servo1].mode = SERVO
board.digital[servo2].mode = SERVO
board.digital[servo3].mode = SERVO


# board.digital[servo4].mode = SERVO
# board.digital[servo5].mode = SERVO


def index(request):
    return render(request, "index.html")


def testarm(request):
    servo_num = 0
    print(servo_num)
    return render(request, "testarm.html")


def testarm1(request):
    servo_num = 1
    print(servo_num)
    return render(request, "testarm.html")
