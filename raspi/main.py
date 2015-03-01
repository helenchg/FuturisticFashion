import ledUtils

# vars
url = 'http://leapfashion.herokuapp.com/api/data'
interval = 255 / 8

init_LEDs()

while True:
	try:
		response = urllib.urlopen(url).read()
		data = json.loads(response)['data']
		color = data['brightness'] / interval
		redOn = color / 4
		greenOn = (color % 4) / 2
		blueOn = (color % 2)
		
		if redOn:
			turnRedOn()
		else:
			turnRedOff()
			
		if greenOn:
			turnGreenOn()
		else:
			turnGreenOff()
			
		if blueOn:
			turnBlueOn()
		else:
			turnBlueOff()
	except KeyboardError:
		break
	except:
		continue

# clean up
cleanUp()