import RPi.GPIO as GPIO
import time

# Setup GPIO using board numbering
GPIO.setmode(GPIO.BOARD)

# Declare variables
RED = 11
GREEN = 13
BLUE = 17

# Main function
GPIO.setup(RED, GPIO.output) #set pin 11 as output
GPIO.output(RED, 1)
GPIO.setup(GREEN, GPIO.output) #set pin 13 as output
GPIO.output(GREEN, 1)
GPIO.setup(BLUE, GPIO.output) #set pin 17 as output
GPIO.output(BLUE, 1)

try:
	while(True):
		### Simple RGB LED Strip test
		request = raw_input("RGB: ")
		if (len(request) ==3):
			GPIO.output(RED, int(request[0])) # storing the first digit 
			GPIO.output(GREEN, int(request[1])) # storing the second digit 
			GPIO.output(BLUE, int(request[2])) # storing the third digit 

except KeyboardInterrupt:
	GPIO.cleanup()

