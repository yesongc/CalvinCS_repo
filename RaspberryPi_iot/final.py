#Yesong Choi yc38
#CS300 Project
#A program that uses the RaspberryPi to monitor movement and provide visual feedback.
#Uses the PIR motion sensor to detect movement
#Uses the USB camera via OpenCV to take a picture of the intruder
#Uses Base64 enconding to convert the image file into a string
#Uses MQTT to transfer the converted image file to the broker using a specific topic

import RPi.GPIO as GPIO
import numpy as np
import cv2 as cv #OpenCV to control usb camera
import time
import paho.mqtt.client as mqtt
import base64 #to convert images and send them via MQTT

#variables 

#GPIO port numbers
sensor = 16
cameraPort = 0
#MQTT broker, port, qos
BROKER = #broker address here
PORT = 1883
QOS = 2

#Set up GPIO for Motion Sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)


#method to take a photo from the USB camera
def takePhoto():
                #starts recording a video from camera
                camera = cv.VideoCapture(cameraPort)
                if camera.isOpened():
                        #delay for the camera to get ready
                        time.sleep(0.1)
                        #take the picture
                        returnValue, picture = camera.read()
                        #if the camera worked, returnValue should be true
                        if returnValue:
                                #convert img to grayscale to reduce memory
                                grayScale = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
                                #save file as jpg in buffer
                                returnValue, buffer = cv.imencode('.jpg', grayScale)
                                #save the buffer as base64 string
                                strImg = base64.b64encode(buffer)
                                #open up the camera for others to use
                                camera.release()
                                print("done capturing")
                                return strImg
                        else:
                                print("return value was False")

#mqtt

# Callback when a message is published
def on_publish(client, userdata, mid):
        print("data published")

# Callback when a connection has been established with the MQTT broker
def on_connect(client, userdata, rc, *extra_params):
        print('Connected with result code='+str(rc))

# Callback when client receives a PUBLISH message from the broker
def on_message(client, data, msg):
        if msg.topic == "yc38/camera":
                print("message published")

# Setup MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

# Connect to MQTT broker
client.connect(BROKER, PORT, 60)
client.loop_start()


#main loop
try:
        while True:
                #delay for sensor to detect
                time.sleep(4)
                #if sensor detects something, turn the LED on
                if GPIO.input(sensor) == True:
                                print("movement detected")
                                screenShot = takePhoto()
                                #after taknig the picture, publish the image to the yc38/camera topic
                                client.publish("yc38/camera", screenShot, qos=QOS)
                else:
                                print("no movement detected")
except:
        GPIO.cleanup()
client.disconnect()
