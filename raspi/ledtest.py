import RPi.GPIO as GPIO

# Setup GPIO using board numbering
GPIO.setmode(GPIO.BOARD)

# Declare variables
RED = 11
GREEN = 13
BLUE = 17

# Main function
GPIO.setup(RED, GPIO.output) #set pin 11 as output
GPIO.setup(GREEN, GPIO.output) #set pin 13 as output
GPIO.setup(BLUE, GPIO.output) #set pin 17 as output

pr = GPIO.PWM(RED, 50)
pg = GPIO.PWM(GREEN, 0)
pb = GPIO.PWM(BLUE, 0)

pr.start(0);


GPIO.cleanup()

