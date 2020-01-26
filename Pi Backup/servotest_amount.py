from __future__ import division
import time

import Adafruit_PCA9685

pwm=Adafruit_PCA9685.PCA9685()

servo_min = 145
servo_max=650
slope=int((servo_max-servo_min)/180)

'''def set_servo_pulse(channel,pulse):
    pulse_length = 1000000
    pulse_length //=60
    print('{0}us per period'.format(pulse_length))
    pulse_length //=4096
    print('{0}s per bit'.format(pulse_length))
    pulse*=1000
    pulse //=pulse_length
'''
def set_servo_angle(angle):
    pulse_width=servo_min+slope*angle
    return pulse_width

pwm.set_pwm_freq(60)
print('Moving')
#while True:
 #   pwm.set_pwm(0,0,servo_min)
  #  time.sleep(1)
   # pwm.set_pwm(0,0,servo_max)
    #time.sleep(1)

for angle in range(150,200,5):
    pwm.set_pwm(8,0,set_servo_angle(angle))
    print("going")
    time.sleep(.2)


for angle in range(200,150,-5):
    pwm.set_pwm(8,0,set_servo_angle(angle))
    print("coming back")
    time.sleep(.2)
    
    
    
