import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG=11
ECHO=13
print ("Distance measurement in progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print ("Sensor settling down")
time.sleep(1)


while (True):
 GPIO.output(TRIG,True)
 time.sleep(0.00001)
 GPIO.output(TRIG,False)

 while (GPIO.input(ECHO)==0):
  pulse_start=time.time()
 while (GPIO.input(ECHO)==1):
  pulse_end=time.time()

 Pulse_duration=pulse_end-pulse_start

 Distance=17150*Pulse_duration

 Distance=round(Distance,2)

 print (Distance)

GPIO.cleanup()
