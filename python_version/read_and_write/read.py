#!/usr/bin/env python
import RPi.GPIO  as GPIO
from mfrc522 import SimpleMFRC522

read_inst = SimpleMFRC522()

try:
    id,text = read_inst.read()
    print("ID: {} \n code: {}".format(id,text))
    # TODO -authentication of the data
finally:
    GPIO.cleanup()