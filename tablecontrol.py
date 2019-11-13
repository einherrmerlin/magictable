import time
import constants as c
import RPi.GPIO as GPIO

floorcal = False
preheight = 0
gpio_clean = False

# setup and calibration functions
def gpio_setup():
    if gpio_clean == False:
        gpio_cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(c.RELAIS_1_GPIO, GPIO.OUT)
    GPIO.setup(c.RELAIS_2_GPIO, GPIO.OUT)


def table_calibrate():
    print ("Kalibrierung läuft, bitte warten")
    global floorcal
    if floorcal == False:
        table_lower(c.FULLTIME)
        floorcal = True
    else:
        table_raise(c.FULLTIME)

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
    global floorcal
    if floorcal == False:
        table_calibrate()
    table_lower(preheight)
    table_raise(height)
    preheight = height


def table_standposition(height):
    global preheight
    global floorcal
    if floorcal == True:
        table_calibrate()
    table_raise(preheight)
    table_lower(height)
    preheight = height
