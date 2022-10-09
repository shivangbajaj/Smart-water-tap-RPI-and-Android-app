
import requests
from datetime import datetime,timedelta,date
import time
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

#-------------------UBIDOTS------------------------
TOKEN = "" # Assign your Ubidots Token
DEVICE =   "rpi" # Assign the device label to obtain the variable
VARIABLE = "var_label" # Assign the variable label to obtain the variable value
DELAY = 1  # Delay in seconds
now=datetime.now()

#----------------SERVOMOTOR-----------------------------
GPIO.setmode(GPIO.BCM)
servoPIN = 17
GPIO.setup(servoPIN, GPIO.OUT)
pwm = GPIO.PWM(servoPIN, 50)
pwm.start(0)

#------------------SERVOANGLE------------------------
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoPIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    pwm.ChangeDutyCycle(0)

#-----------------UBIDOTS-VALUE-FETCH--------------
def get_var(device, variable):
    try:
        url = "http://things.ubidots.com/"
        url = url + \
            "api/v1.6/devices/{0}/{1}/".format(device, variable)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        req = requests.get(url=url, headers=headers)
        val= req.json()['last_value']['value']
        return val
    except:
        pass

#-------------------CALCULATE--DISTANCE-ROTATING-SERVOMOTOR-------------
def distance():
    GPIO_TRIGGER = 23
    GPIO_ECHO = 24

    print ("Distance Measurement In Progress")

    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)


    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance



if __name__ == "__main__":
    print('INSIDE MAIN')
    time=str(get_var(DEVICE, VARIABLE))
    list1=list(time)
    hr=int(list1[0]+list1[1])1
    min = int(list1[2] + list1[3])
    user=timedelta(hours=hr,minutes=min)
    systime=timedelta(hours=now.hour,minutes=now.minute)
    print(user)
    print(systime)
    sleeptime=str(user-systime)
    ftr = [3600, 60, 1]
    seconds=int(sum([a * b for a, b in zip(ftr, map(int, sleeptime.split(':')))]))
    #sleep(int(seconds))
    flag =True

    try:
        while flag:
            print('INDSIDE FLAG')
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(0.5)
            if dist < 20 :
                SetAngle(0)
                sleep(0.5)
                SetAngle(180)

                pwm.stop()
                flag = False

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
GPIO.cleanup()
