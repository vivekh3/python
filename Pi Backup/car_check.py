import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#For forward
GPIO.setup(29,GPIO.OUT)
#For backward
GPIO.setup(31,GPIO.OUT)
#For left
GPIO.setup(32,GPIO.OUT)
#For right
GPIO.setup(33,GPIO.OUT)

GPIO.output(29,False)
GPIO.output(31,False)
GPIO.output(32,False)
GPIO.output(33,False)

GPIO.output(29,True)
time.sleep(5)
GPIO.cleanup()




