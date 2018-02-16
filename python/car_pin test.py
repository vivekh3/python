import RPi.GPIO as GPIO
#import curses
import time
GPIO.setmode(GPIO.BOARD)

## Setting up sensor pins
#TRIG_R=11
#ECHO_R=13
#TRIG_L=16
#ECHO_L=18
#GPIO.setup(TRIG_R,GPIO.OUT)
#GPIO.setup(ECHO_R,GPIO.IN)
#GPIO.setup(TRIG_L,GPIO.OUT)
#GPIO.setup(ECHO_L,GPIO.IN)

## Setting up Car pins
FWD=29
BK=31
LEFT=32
RIGHT=33
GPIO.setup(FWD, GPIO.OUT)
GPIO.setup(BK, GPIO.OUT)
GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)

## Start Function block
GPIO.output(FWD,True)
time.sleep(2)
GPIO.output(FWD,False)
GPIO.output(BK,True)
time.sleep(2)
GPIO.output(BK,False)
GPIO.output(LEFT,True)
time.sleep(2)
GPIO.output(LEFT,False)
GPIO.output(RIGHT,True)
time.sleep(2)
GPIO.output(RIGHT,False)

