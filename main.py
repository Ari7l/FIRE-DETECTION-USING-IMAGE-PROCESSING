import numpy as np
import cv2
import time
import smtplib
# import tensorflow
from twilio.rest import Client

account_sid = 'AC20e7fb2ac64bf81564a46683cf097684'
auth_token = '7ad24daaa0798ed79ac9ccc58c5f7464'
client1 = Client(account_sid, auth_token)
#
# account_sid1 = 'AC86adfb7094286973492789b5c35e12b5'
# auth_token1 = '88d297ec8dcb75b8333bf3b98a00ebcf'
# client2 = Client(account_sid1, auth_token1)

fire_cascade = cv2.CascadeClassifier('C:\\fire_detection\\data\\fire_smoke_detection.xml')
human_detection = cv2.CascadeClassifier('C:\\fire_detection\\haarcascade_fullbody_alt.xml')
#img = cv2.imread('F:\\New folder\\group_photo.jpg')

room_one = cv2.VideoCapture(0)
room_two = cv2.VideoCapture(1)
while 1:
    ret0, frame0 = room_one.read()
    ret1, frame1 = room_two.read()
    if (ret0):

        gray = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
        dst = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
        fire = fire_cascade.detectMultiScale(dst, 1.5, 1)
        for (x, y, w, h) in fire:
            cv2.rectangle(frame0, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi_color = frame0[y:y + h, x:x + w]
            message = client1.messages.create(
                # media_url=["https://www.qsrmagazine.com/sites/default/files/story/red-roofs-are-haunting-pizza-huts-sales.jpg"],
                from_='whatsapp:+14155238886',
                body="Fire Alert in Room 1",
                to='whatsapp:+918668402601'
            )
        # cv2.imshow('frame0', frame0)

        frame = cv2.resize(frame0, (640, 480))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        human = human_detection.detectMultiScale(gray, 1.5, 1)
        for (x1, y1, w1, h1) in human:
            cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
            roi_color = frame[y1:y1 + h1, x1:x1 + w1]
        cv2.imshow('frame', frame)

    if (ret1):
        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        dst = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
        fire = fire_cascade.detectMultiScale(dst, 1.5, 1)
        for (x2, y2, w2, h2) in fire:
            cv2.rectangle(frame1, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)
            roi_color = frame1[y2:y2 + h2, x2:x2 + w2]
            # message = client2.messages.create(
            #     # media_url=["https://www.qsrmagazine.com/sites/default/files/story/red-roofs-are-haunting-pizza-huts-sales.jpg"],
            #     from_='whatsapp:+14155238886',
            #     body="Fire Alert in Room 2",
            #     to='whatsapp:+919689119630'
            # )

        frame = cv2.resize(frame1, (640, 480))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        human = human_detection.detectMultiScale(gray, 1.5, 3)
        for (x, y, w, h) in human:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = frame[y:y + h, x:x + w]
        cv2.imshow('frame1', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break



