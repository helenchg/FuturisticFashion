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

pwmR = GPIO.PWM(RED, HERTZ) 
pwmG = GPIO.PWM(GREEN, HERTZ)
pwmB = GPIO.PWM(BLUE, HERTZ)

pwmR.start(1.0) #make sure pwm is off in the begining 
pwmG.start(0)
pwmB.start(0)

try:
	while(True):
		### Simple RGB LED Strip test
		# request = raw_input("RGB: ")
#		dc = raw_input("Brightness: ")
#		if (len(request) ==3):
			# GPIO.output(RED, 1) # storing the first digit 
			# GPIO.output(GREEN, 0) # storing the second digit 
			# GPIO.output(BLUE, 0) # storing the third digit 

			for i in range (11):				# make LED brighter in 100 steps
				print i;
				pwmR.ChangeDutyCycle(10.0 * i)
				time.sleep(3);				# every time, on for 20ms. To make sure the LED has enough time to perform change
			
			# for i in range(steps):				# make LED dimmer in 100 steps
			# 	pwmR.ChangeDutyCycle(steps-i)
			# 	time.sleep(time_delay)
except KeyboardInterrupt:
	pass
pwmR.stop()
pwmG.stop()
pwmB.stop()
GPIO.cleanup() #reset GPIO pin to whatever it is defauld

