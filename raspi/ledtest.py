import RPi.GPIO as GPIO
import time
from 

# Setup GPIO using board numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Declare variables
RED = 17
GREEN = 27
BLUE = 22

# Main function
GPIO.setup(RED, GPIO.OUT) #set pin 11 as output
GPIO.output(RED, 1)
GPIO.setup(GREEN, GPIO.OUT) #set pin 13 as output
GPIO.output(GREEN, 1)
GPIO.setup(BLUE, GPIO.OUT) #set pin 17 as output
GPIO.output(BLUE, 1)

try:
	while(True):
		### Simple RGB LED Strip test
		request = raw_input("RGB: ")
		pwm = raw_input("Brightness: ")
		if (len(request) ==3):
			GPIO.output(RED, int(request[0])) # storing the first digit 
			GPIO.output(GREEN, int(request[1])) # storing the second digit 
			GPIO.output(BLUE, int(request[2])) # storing the third digit 
			pwmR = GPIO.PWM(RED, pwm)
			pwmG = GPIO.PWM(GREEN, pwm)
			pwmB = GPIO.PWM(BLUE, pwm)
			time.sleep(3)



except KeyboardInterrupt:
	GPIO.cleanup()

