import time
import constants as c
import RPi.GPIO as GPIO

floorcal = False
preheight = 0

# setup and calibration functions
def gpio_setup():
    if c.GPIO_CLEAN == False:
        gpio_cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(c.RELAIS_1_GPIO, GPIO.OUT)
    GPIO.setup(c.RELAIS_2_GPIO, GPIO.OUT)


def table_calibrate():
    print ("Kalibrierung läuft, bitte warten")
    if floorcal == False: # hier kommt der Error, da floorcal noch nicht assignet ist bis dato
    # Traceback (most recent call last):
  # File "voicerecognition.py", line 39, in <module>
    # tc.table_calibrate])
  # File "/home/pi/tablecontrol.py", line 19, in table_calibrate
    # table_raise(preheight)
# UnboundLocalError: local variable 'floorcal' referenced before assignment

        table_lower(c.FULLTIME)
        floorcal = True
    else:
        table_raise(c.FULLTIME)

def gpio_cleanup():
    GPIO.cleanup()
    c.GPIO_CLEAN = True

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
    table_lower(preheight)
    table_raise(height)
    preheight = height


def table_standposition(height):
    table_raise(preheight)
    table_lower(height)
    preheight = height
