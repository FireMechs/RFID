#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

mf_inst = SimpleMFRC522()

try:
    tag_textData  = input("Secret code string: ")
    # /* TODO - check in the database if the same string exist */
    print("Place the tag to write your data...")
    mf_inst.write(tag_textData)
    print("Written")
finally:
    GPIO.cleanup()

