import RPi.GPIO as GPIO
import time

# Setup GPIO using board numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Declare variables
RED = 17
GREEN = 27
BLUE = 22
HERTZ = 50 # this is high enough to not see the LED blinking
time_delay = 0.02 # three seconds delay
steps = 255

# Main function
GPIO.setup(RED, GPIO.OUT) #set pin 11 as output
GPIO.output(RED, 1)
GPIO.setup(GREEN, GPIO.OUT) #set pin 13 as output
GPIO.output(GREEN, 1)
GPIO.setup(BLUE, GPIO.OUT) #set pin 17 as output
GPIO.output(BLUE, 1)
pwmR = GPIO.PWM(RED, HERTZ) 
pwmG = GPIO.PWM(GREEN, HERTZ)
pwmB = GPIO.PWM(BLUE, HERTZ)

pwmR.start(0) #make sure pwm is off in the begining 
pwmG.start(0)
pwmB.start(0)


try:
	while(True):
		### Simple RGB LED Strip test
		request = raw_input("RGB: ")
		dc = raw_input("Brightness: ")
		if (len(request) ==3):
			GPIO.output(RED, int(request[0])) # storing the first digit 
			GPIO.output(GREEN, int(request[1])) # storing the second digit 
			GPIO.output(BLUE, int(request[2])) # storing the third digit 
#			pwmR.start(float(dc))
#			pwmG.start(float(dc))
#			pwmB.start(float(dc))
#			time.sleep(time_delay)
			for i in range (steps):				# make LED brighter in 100 steps
				pwmR.ChangeDutyCycle(i)
				time.sleep(time_delay) 				# every time, on for 20ms. To make sure the LED has enough time to perform change
			for i in range(steps):				# make LED dimmer in 100 steps
				p.ChangeDutyCycle(100-i)
				time.sleep(time_delay)



except KeyboardInterrupt:
	pass
pwmR.stop()
pwmG.stop()
pwmB.stop()
GPIO.cleanup()

