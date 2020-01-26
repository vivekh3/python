
# import the necessary packages

from picamera import PiCamera
import time

 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32

 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
camera.start_preview()
time.sleep(100)
camera.stop_preview()
