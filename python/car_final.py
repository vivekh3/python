import RPi.GPIO as GPIO
#import curses
import time
GPIO.setmode(GPIO.BOARD)

## Setting up sensor pins
TRIG_R=11
ECHO_R=13
TRIG_L=16
ECHO_L=18
GPIO.setup(TRIG_R,GPIO.OUT)
GPIO.setup(ECHO_R,GPIO.IN)
GPIO.setup(TRIG_L,GPIO.OUT)
GPIO.setup(ECHO_L,GPIO.IN)

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
#Setting up call pins to zero
def Allzero():
 GPIO.output(TRIG_R,False)
 GPIO.output(TRIG_L,False)
 return

def Carstop():
 GPIO.output(FWD,False)
 GPIO.output(BK,False)
 GPIO.output(LEFT,False)
 GPIO.output(RIGHT,False)
 return

# Fire and Measure
def fireandmeasure(channel):
 if (channel=="Left"):
  Trigger=TRIG_L
  Echo=ECHO_L
 elif (channel=="Right"):
  Trigger=TRIG_R
  Echo=ECHO_R
 GPIO.output(Trigger,True)
 time.sleep(0.00001)
 GPIO.output(Trigger,False)
 
 while(GPIO.input(Echo)==0):
  pulse_start=time.time()
 while(GPIO.input(Echo)==1):
  pulse_end=time.time()
 pulse_duration=pulse_end-pulse_start
 distance=pulse_duration*17150
 distance=round(distance,2)
 return distance 

def movethecarforward():
 GPIO.output(FWD,True)
 obstaclecheck() 
 print("Moving car forward")
 return

def movethecarbackward():
 GPIO.output(BK,True)
 print("Car backing up")
 time.sleep(1)
 return

def turncarleft(t):
 GPIO.output(LEFT,True)
 print("Car's wheel left")
 movethecarforward()
 time.sleep(t)
 GPIO.output(LEFT,False)
 return

def turncarright(t):
 GPIO.output(RIGHT,True)
 print("Car's wheel right")
 movethecarforward()
 time.sleep(t)
 GPIO.output(RIGHT,False)
 return

def obstaclecheck():
	Distance_R=fireandmeasure("Right")
	Distance_L=fireandmeasure("Left")
	print ("Distance from right: "+str(Distance_R) + " Distance from left: "+str(Distance_L)) 

	if (Distance_R <=30):
		Carstop()
		movethecarbackward()
		Carstop()
		turncarleft(2)
		Distance_L = 100
	elif(Distance_L<=30):
		Carstop()
		movethecarbackward()
		Carstop()
		turncarright(2)
		Distance_R=100
	
	return

## End function block


Allzero()
print ("Sensor settling down")
time.sleep(1)

try:
	while (True):

 		movethecarforward()

except KeyboardInterrupt:
	Allzero()
	Carstop()
	GPIO.cleanup()
	print ("I am out of here "+ str(Distance_R) + " " +str(Distance_L))
