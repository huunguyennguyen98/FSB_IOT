import sys
from Adafruit_IO import MQTTClient
import numpy as np
import random
import time
from collections import Counter
import base64
import cv2 as cv
import serial.tools.list_ports

AIO_FEED_ID = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "huunguyenng"
AIO_KEY = "aio_cfTE85AxGAVyAuJ93DgpX6OZ7yIB"

# Ket noi voi Adafruit-IO
def connected(client):
    print("Ket noi thanh cong ...")
    #client.subscribe(AIO_FEED_ID)
    for topic in AIO_FEED_ID:
      client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)
def message(client , AIO_FEED_ID , payload):
    print("Nhan du lieu: "+ payload + ", Feed ID: " + AIO_FEED_ID)
    print(AIO_FEED_ID)
    writeData(payload)

# Xu ly ve serial
def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    comPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            comPort = (splitPort[0])
    return "COM5"

def processData(data):
    data = data.replace("!","")
    data = data.replace("#","")
    splitData = data.split(":")
    print("splitData")
    if splitData[1] == "TEMP":
        client.publish("cambien1", splitData[2])

if getPort()!= "None":
    ser = serial.Serial(port = getPort(), baudrate=115200)
mess = ""

def readSerial():
    bytesToRead = ser.inWaiting()
    if(bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while("" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("!")
            processData(mess[start:end + 1])
            if(end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def writeData(data):
    ser.write(str(data).encode('utf-8'))

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 0
sensor_type = 0
counter_ai = 5
while True:
    pass