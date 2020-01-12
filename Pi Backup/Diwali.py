import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import RPi.GPIO as GPIO
from picamera import PiCamera

GPIO.setmode(GPIO.BOARD)

## Setting up sensor pins
lightpin=11
GPIO.setup(lightpin,GPIO.OUT)

def send_email(body):

    localtime = time.asctime(time.localtime(time.time()) )

    email_user="vivekscratch@gmail.com"
    email_pwd="Vishnu303!"
    msg = "Lets check this"
    email_recep="vivek.hari79@gmail.com"

    subject="The status at "+localtime


    msg=MIMEMultipart()
    msg['From']=email_user
    msg['To']=email_recep
    msg['subject']=subject

    msg.attach(MIMEText(body,'plain'))


    folderpath=os.getcwd()
    filename='/home/pi/Desktop/Diwali1.jpg'

    attachment=open(filename,'rb')

    part=MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
    text=msg.as_string()


    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_pwd)

    server.sendmail(email_user,email_recep,text)
    server.quit()
    return

def lights_on():
    GPIO.output(lightpin,False)
    return

def lights_off():
    GPIO.output(lightpin,True)
    return

def take_a_picture():
    camera=PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/Diwali.jpg')
    camera.stop_preview()
    return
lights_on()   
print("Lights On - Happy Diwali")
send_email("Lights On - Happy Diwali")
#take_a_picture()
time.sleep(10800)
print("Lights Off - Happy Diwali")
send_email("Lights Off - Happy Diwali")
print("All Done")
GPIO.cleanup()
