dc motor

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
motorForward = 13
motorReverse = 19
GPIO.setup(motorForward, GPIO.OUT)
GPIO.setup(motorReverse, GPIO.OUT)
def motorDrive(Dir, time):
	
    if Dir == 'F':
        GPIO.output(motorForward, True)
        GPIO.output(motorReverse, False)
        print('motor is tuning forward')

    if Dir == 'R':
        GPIO.output(motorForward, False)
        GPIO.output(motorReverse, True)
        print('motor is turning revers')

    if Dir == 'S':
        GPIO.output(motorForward, False)
        GPIO.output(motorReverse, False)
        print('motor stopped')
        
    time.sleep(time)
		
	
while True:

    motorDrive('F',3)
    motorDrive('S',2)
    motorDrive('R',5)
    motorDrive('S')
