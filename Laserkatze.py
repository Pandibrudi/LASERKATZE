import RPi.GPIO as GPIO
import time
from random import randint
#steuerung für lasercat

servopin = 11
fPWM = 50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT)

servo = GPIO.PWM(servopin, fPWM)

servo.start(2.5)

def setservo(winkel):
    if winkel < 0:
        winkel = 0
    if winkel > 180:
        winkel = 180
    pwm = winkel/18 + 2.5
    servo.ChangeDutyCycle(pwm)

try:
    while True:
        zufallswinkel = randint(0,90)
        zufallszeit = randint(1,3)
        setservo(zufallswinkel)
        print("Winkel:", zufallswinkel)
        time.sleep(zufallszeit)
        zufallswinkel = randint(90,180)
        zufallszeit = randint(1,3)
        setservo(zufallswinkel)
        print("Winkel:", zufallswinkel)
        time.sleep(zufallszeit)


except KeyboardInterrupt:
    setservo(0)
    time.sleep(1)
    servo.ChangeDutyCycle(0)
    time.sleep(1)
    servo.stop()
    GPIO.cleanup()
