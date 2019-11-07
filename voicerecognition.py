import random
import time
import speech_recognition as sr
import RPi.GPIO as GPIO

# set GPIO Pins
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
RELAIS_1_GPIO = 17
RELAIS_2_GPIO = 18

# set local variables
tup = "aufwärts"
tdown = "abwärts"
tname = "banane"
merlinsit = "banane waschbär sitzen"
merlinstand = "banane waschbär stehen"
jansit = "banane ameisenbär sitzen"
janstand = "banane ameisenbär stehen"
jansitpos = 3.1
merlinsitpos = 3.5
merlinstandpos = 3.0
janstandpos = 3.2


def gpio_setup():
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.setup(RELAIS_2_GPIO, GPIO.OUT)


def table_stop():
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)


def table_down():
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)


def table_up():
    GPIO.output(RELAIS_2_GPIO, GPIO.LOW)


def gpio_cleanup():
    GPIO.cleanup()


def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='de-DE')
    except sr.RequestError:
        # API was unreachable or unresponsive
        text = ("API nicht erreichbar")
    except sr.UnknownValueError:
        # speech was unintelligible
        text = ("Spracheingabe nicht verstanden")
    return text


def table_merlin_sit():
    table_down()
    time.sleep(13)
    table_stop()
    time.sleep(1)
    table_up()
    time.sleep(3.5)
    table_stop()


def table_merlin_stand():
    table_up()
    time.sleep(13)
    table_stop()
    time.sleep(1)
    table_down()
    time.sleep(3)
    table_stop()


def table_jan_sit():
    table_down()
    time.sleep(13)
    table_stop()
    time.sleep(1)
    table_up()
    time.sleep(3.1)
    table_stop()


def table_jan_stand():
    table_up()
    time.sleep(13)
    table_stop()
    time.sleep(1)
    table_down()
    time.sleep(3.1)
    table_stop()

if __name__ == "__main__":
	# create recognizer and mic instancve
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    gpio_setup()

    # recognize speech and print speech
    text = recognize_speech_from_mic(recognizer, microphone)
    text = text.lower()
    listen = True
    while listen == True
        if (text) == merlinsit:
            print ("Ich habe verstanden: " + text)
            table_merlin_sit()
            print ("Tisch an Position Merlin - Sitzen gefahren")
        elif (text) == merlinstand:
            print ("Ich habe verstanden: " + text)
            table_merlin_stand()
            print ("Tisch an Position Merlin - Stehen gefahren")
        elif (text) == jansit:
            print ("Ich habe verstanden: " + text)
            table_jan_sit()
            print ("Tisch an Position Jan - Sitzen gefahren")
        elif (text) == janstand:
            print ("Ich habe verstanden: " + text)
            table_jan_stand()
            print ("Tisch an Position Jan - Stehen gefahren")
        else:
            print (text)
            gpio_cleanup()
            print ("Keine Auswahl getroffen - Programm beendet")
