import RPi.GPIO as GPIO
import time

# Setup GPIO using board numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Declare variables
RED = 11
GREEN = 13
BLUE = 15
HERTZ = 100.0 # this is high enough to not see the LED blinking
time_delay = 0.02 # three seconds delay
steps = 100

# Main function
GPIO.setup(RED, GPIO.OUT) #set pin 11 as output
GPIO.setup(GREEN, GPIO.OUT) #set pin 13 as output
GPIO.setup(BLUE, GPIO.OUT) #set pin 17 as output

GPIO.output(RED, 1) # storing the first digit 
GPIO.output(GREEN, 0) # storing the second digit 
GPIO.output(BLUE, 0) # storing the third digit 

# pwmR = GPIO.PWM(RED, 1) 
# pwmG = GPIO.PWM(GREEN, HERTZ)
# pwmB = GPIO.PWM(BLUE, HERTZ)

# pwmR.start(100) #make sure pwm is off in the begining 
# pwmG.start(100)
# pwmB.start(50)

while True:
	try:
		GPIO.output(RED, 1)
		time.sleep(0.01)
		GPIO.output(RED, 0)
		time.sleep(0.01)
	except KeyboardInterrupt:
		break

GPIO.output(RED, 0)
# pwmR.stop()
# pwmG.stop()
# pwmB.stop()
GPIO.cleanup() #reset GPIO pin to whatever it is defauld



