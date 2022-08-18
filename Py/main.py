#IMPORTS

import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
import threading
import time
import PID

#SET MODES

GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)
AN1 = 12				# set pwm1 pin on MD10-hat
DIG1 = 26				# set dir1 pin on MD10-Hat
EN1 = 17
EN2 = 18
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
GPIO.setup(EN1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(EN2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


sleep(1)				# delay for 1 seconds
p1 = GPIO.PWM(DIG1, 100)		# set pwm for M1

counter = 0
alpha = 0
EN1lastState = GPIO.input(EN1)

#FUNCTIONS

def MotorClockWise():
    GPIO.output(AN1, GPIO.HIGH)	# set AN1 as HIGH, M1B will turn ON
    p1.start(0)				# set Direction for M1
    sleep(2)				#delay for 2 second

def MotorAntiClockWise():
    GPIO.output(AN1, GPIO.HIGH)
    p1.start(1)
    sleep(2)

while True:
    EN1state = GPIO.input(EN1)
    EN2state = GPIO.input(EN2)
    alpha = (counter/800)*360

    if EN1state != EN1lastState:
        if EN2state != EN1state:
            counter -= 1
            MotorAntiClockWise()
        else:
            counter += 1
            MotorClockWise()
        print(f"{alpha} Degrees")           