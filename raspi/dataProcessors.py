import ledUtils

class PinchColor:
	name = 'Pinch Color'
	interval = 0.125 # 1/8; because 8 colors are available
	
	# hue depends on pinch strength
	def process(self, data):
		color = int(data['pinchstrength'] / interval)
		# print color
		redOn = color / 4 # MSB
		greenOn = (color % 4) / 2 # middle bit
		blueOn = (color % 2) # LSB
		
		if redOn:
			ledUtils.turnRedOn()
		else:
			ledUtils.turnRedOff()
			
		if greenOn:
			ledUtils.turnGreenOn()
		else:
			ledUtils.turnGreenOff()
			
		if blueOn:
			ledUtils.turnBlueOn()
		else:
			ledUtils.turnBlueOff()
			
class WhiteOrBlue:
	name = 'White or Blue?'
	
	# blink blue/null vs. white/gold depending on relative heights of hands
	def process(self, data):
		yLeft = float(data['yl'])
		yRight = float(data['yr'])
		print data['xl'], data['xr']
		print yLeft, yRight
		print data['zl'], data['zr']
		
		if (yLeft >= yRight):
			# blink blue and nothing
			ledUtils.setRedDutyCycle(0)
			ledUtils.setGreenDutyCycle(0)
			ledUtils.setBlueDutyCycle(50)
		else:
			# blink white and gold
			ledUtils.setBlueDutyCycle(50)
			ledUtils.setRedDutyCycle(100)
			ledUtils.setGreenDutyCycle(100)