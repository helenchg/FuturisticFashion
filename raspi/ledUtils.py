import RPi.GPIO as GPIO
import time

# Default values
MODE = GPIO.BOARD
RED_PIN = 11 # pin no.s will change in different mode
GREEN_PIN = 13
BLUE_PIN = 15

HERTZ = 1
DUTY_CYCLE = 100 # in percentage; 0-100

# Initial output values
RED_INIT = 1
BLUE_INIT = 1
GREEN_INIT = 1

# The PWM (Pulse-Width Modulation) handlers
pwmR = None
pwmG = None
pwmB = None

def init_LEDs():

	global pwmR
	global pwmG
	global pwmB

	GPIO.setmode(GPIO.BOARD)
	# GPIO.setwarnings(False)
	
	GPIO.setup(RED_PIN, GPIO.OUT)
	GPIO.setup(GREEN_PIN, GPIO.OUT)
	GPIO.setup(BLUE_PIN, GPIO.OUT)
	
	GPIO.output(RED_PIN, RED_INIT) # storing the first digit 
	GPIO.output(GREEN_PIN, BLUE_INIT) # storing the second digit 
	GPIO.output(BLUE_PIN, GREEN_INIT) # storing the third digit
	
	pwmR = GPIO.PWM(RED_PIN, HERTZ)
	pwmG = GPIO.PWM(GREEN_PIN, HERTZ)
	pwmB = GPIO.PWM(BLUE_PIN, HERTZ)
	
	pwmR.start(DUTY_CYCLE)
	pwmG.start(DUTY_CYCLE)
	pwmB.start(DUTY_CYCLE)
	
def all_LEDs_on():
	GPIO.output(RED_PIN, 1)
	GPIO.output(GREEN_PIN, 1)
	GPIO.output(BLUE_PIN, 1)
	
def all_LEDs_off():
	GPIO.output(RED_PIN, 0)
	GPIO.output(GREEN_PIN, 0)
	GPIO.output(BLUE_PIN, 0)
	
# Removing all blinking
def all_LEDs_steady():
	setRedDutyCycle(100)
	setBlueDutyCycle(100)
	setGreenDutyCycle(100)

def cleanUp():
	try:
		all_LEDs_off()
		pwmR.stop()
		pwmG.stop()
		pwmB.stop()
	finally:
		GPIO.cleanup()

# Functions for red channel
def setRedFrequency(freq):
	pwmR.ChangeFrequency(freq)

def setRedDutyCycle(dutyCycle):
	pwmR.ChangeDutyCycle(dutyCycle)
	
def turnRedOff():
	GPIO.output(RED_PIN, 0)
	setRedDutyCycle(0)

def turnRedOn():
	GPIO.output(RED_PIN, 1)
	setRedDutyCycle(100)

# Functions for green channel
def setGreenFrequency(freq):
	pwmG.ChangeFrequency(freq)

def setGreenDutyCycle(dutyCycle):
	pwmG.ChangeDutyCycle(dutyCycle)
	
def turnGreenOff():
	GPIO.output(GREEN_PIN, 0)
	setGreenDutyCycle(0)

def turnGreenOn():
	GPIO.output(GREEN_PIN, 1)
	setGreenDutyCycle(100)

# Functions for blue channel
def setBlueFrequency(freq):
	pwmB.ChangeFrequency(freq)

def setBlueDutyCycle(dutyCycle):
	pwmB.ChangeDutyCycle(dutyCycle)
	
def turnBlueOff():
	GPIO.output(BLUE_PIN, 0)
	setBlueDutyCycle(0)

def turnBlueOn():
	GPIO.output(BLUE_PIN, 1)
	setBlueDutyCycle(100)

# test code; uncomment to make sure this works
# init_LEDs()
# time.sleep(10)
# setGreenDutyCycle(50)
# time.sleep(5)
# cleanUp()

# while True:
	# try:
		# GPIO.output(BLUE, 1)
		# time.sleep(0.01)
		# GPIO.output(BLUE, 0)
		# time.sleep(0.01)
	# except KeyboardInterrupt:
		# break



