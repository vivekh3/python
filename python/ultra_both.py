import RPi.GPIO as GPIO
#import curses
import time
GPIO.setmode(GPIO.BOARD)
TRIG_R=11
ECHO_R=13
TRIG_L=16
ECHO_L=18
#stdscr = curses.initscr()
print ("Distance measurement in progress")
GPIO.setup(TRIG_R,GPIO.OUT)
GPIO.setup(ECHO_R,GPIO.IN)
GPIO.setup(TRIG_L,GPIO.OUT)
GPIO.setup(ECHO_L,GPIO.IN)

GPIO.output(TRIG_R,False)
GPIO.output(TRIG_L,False)

print ("Sensor settling down")
time.sleep(1)

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

while (True):

 Distance_R = fireandmeasure("Right")
 Distance_L = fireandmeasure("Left")
 #key= stdscr.getch()
 #if(key==27):
 # break


 print ("Distance from right: "+str(Distance_R) + " Distance from left: "+str(Distance_L)) 
 time.sleep(0.5)
#stdscr.endwin()
GPIO.cleanup()
