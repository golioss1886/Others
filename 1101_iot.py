import RPi.GPIO as GPIO
import time

button_tag = 2
BTN_PIN = 15
LED_PIN = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)
def ButtonPressed(btn):
    global button_tag
    button_tag = button_tag/2
    if button_tag < 0.5: 
        button_tag = 2   
    print("Change Pattern ", button_tag)
        #    while True:
        #        print("LED in on.")
        #        GPIO.output(LED_PIN, GPIO.HIGH)
        #        time.sleep(button_tag)
        #        print("LED in off.")
        #         GPIO.output(LED_PIN, GPIO.LOW)
        #         time.sleep(button_tag)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, ButtonPressed, 200) 
try:
    while True:
        print("LED in on.")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(button_tag)
        print("LED in off.")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(button_tag)
        #try:
        #    while
        #    True:
        #        time.sleep(1)
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
finally:
    GPIO.cleanup()


