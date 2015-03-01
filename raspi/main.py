import urllib
import ledUtils

# vars
url = 'http://leapfashion.herokuapp.com/api/data'
interval = 255 / 8

ledUtils.init_LEDs()

while True:
	try:
		response = urllib.urlopen(url).read()
		data = json.loads(response)['data']
		color = data['brightness'] / interval
		redOn = color / 4
		greenOn = (color % 4) / 2
		blueOn = (color % 2)
		
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
			
	except KeyboardInterrupt:
		break
	except:
		continue

# clean up
cleanUp()