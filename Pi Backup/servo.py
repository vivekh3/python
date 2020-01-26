import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
p=GPIO.PWM(7,50)
p.start(2.5)
#float (j,2)
try:
    for i in range(0,180,5):
        j=float(1/18)*i+2.5
        print (i,round(j,2))
        p.ChangeDutyCycle(j)
        time.sleep(0.5)


#    while(True):
#        p.ChangeDutyCycle(7.5)
#        time.sleep(1)
#        p.ChangeDutyCycle(12.5)
#        time.sleep(1)
#        p.ChangeDutyCycle(2.5)
#        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
