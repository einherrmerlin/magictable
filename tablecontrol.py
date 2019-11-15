import time
import constants as c
import RPi.GPIO as GPIO

nearfloor = False # if table is calibrated on lowest or highest setting
preheight = 0 # last height stored for comparison
gpio_clean = True # false if gpios are in use

# setup and calibration functions
def gpio_setup():
    global gpio_clean
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(c.RELAIS_1_GPIO, GPIO.OUT)
    GPIO.setup(c.RELAIS_2_GPIO, GPIO.OUT)
    gpio_clean = False

def table_calibrate():
    global nearfloor
    global preheight
    if nearfloor == False:
        table_lower(c.FULLTIME)
        nearfloor = True
        preheight = 0
    else:
        table_raise(c.FULLTIME)
        nearfloor = False
        preheight = 0

def gpio_cleanup():
    global gpio_clean
    GPIO.cleanup()
    gpio_clean = True

# basic commands - only 1 direction and/or stop
def table_stop():
    GPIO.output(c.RELAIS_1_GPIO, GPIO.HIGH)
    GPIO.output(c.RELAIS_2_GPIO, GPIO.HIGH)
    time.sleep(c.STOP_SLEEP_DURATION)


def table_lower(height):
    GPIO.output(c.RELAIS_1_GPIO, GPIO.LOW)
    time.sleep(height)
    table_stop()


def table_raise(height):
    GPIO.output(c.RELAIS_2_GPIO, GPIO.LOW)
    time.sleep(height)
    table_stop()


# advanced commands - 2 or more directions
def table_sitposition(height):
    global preheight
    global nearfloor
    if nearfloor == False:
        table_calibrate()
    if height != preheight:
        table_lower(preheight)
        table_raise(height)
        preheight = height
    else:
        print ("~ Tisch bereits auf dieser Höhe")


def table_standposition(height):
    global preheight
    global nearfloor
    if nearfloor == True:
        table_calibrate()
    if height != preheight:
        table_raise(preheight)
        table_lower(height)
        preheight = height
    else:
        print ("~ Tisch bereits auf dieser Höhe ~")
