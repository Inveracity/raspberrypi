import rpi.PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math

DO = 17
GPIO.setmode(GPIO.BCM)
ADC.setup(0x48)
GPIO.setup(DO, GPIO.IN)

def temp():
    analogVal = ADC.read(0)
    Vr = 5 * float(analogVal) / 255
    Rt = 10000 * Vr / (5 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    temp = temp - 273.15
    # For Analog Temperature module(with DO)
    # tmp = GPIO.input(DO);

    return round(temp, 1)
