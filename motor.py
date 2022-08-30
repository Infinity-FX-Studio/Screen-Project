#IMPORTS

from typing import Counter
import RPi.GPIO as GPIO                                             # using Rpi.GPIO module
from time import sleep                                              # import function sleep for delay
import threading
import time

#SET MODES

GPIO.setmode(GPIO.BCM)                                              # GPIO numbering
GPIO.setwarnings(False)
AN1 = 12                                                            # set pwm1 pin on MD10-hat
DIG1 = 26                                                           # set dir1 pin on MD10-Hat
ENA = 17
ENB = 18
GPIO.setup(AN1, GPIO.OUT)                                           # set pin as output
GPIO.setup(DIG1, GPIO.OUT)                                          # set pin as output
GPIO.setup(ENA, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)              # set ENA as input
GPIO.setup(ENB, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)              # set ENB as input


sleep(1)                                                            # delay for 1 seconds
p1 = GPIO.PWM(DIG1, 60)                                             # set pwm for M1

counter = 0
alpha = 0
ENAlastState = GPIO.input(ENA)

#FUNCTIONS

def MotorClockWise():
    GPIO.output(AN1, GPIO.HIGH)                                    # set AN1 as HIGH, M1B will turn ON
    p1.start(0)                                                    # set Direction for M1
    sleep(2)                                                       # delay for 2 second

def MotorAntiClockWise():
    GPIO.output(AN1, GPIO.HIGH)
    p1.start(100)
    sleep(2)

def MotorStop():
    GPIO.output(AN1, GPIO.LOW)
    p1.start(0)
    sleep(2)

#Program start

while True:
    ENAstate = GPIO.input(ENA)
    ENBstate = GPIO.input(ENB)
    alpha = (counter/800)*360
    if ENAstate == 1 and ENBstate == 0:
        counter = counter +1
        print(alpha)
    elif ENAstate == 0 and ENBstate == 1:
        counter = counter -1
        print(alpha)
    elif ENAstate == 0 and ENBstate == 0:
        print(alpha)
        print("Motor Duruyor")
    else:
        print("Bu terslikte bi iş var")
    for i in range(0,1):
        MotorClockWise()
    i = 3
    MotorStop()
    break

i = 3

MotorStop()