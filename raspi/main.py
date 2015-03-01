import urllib
import ledUtils

# vars
url = 'http://leapfashion.herokuapp.com/api/data'
interval = 255 / 8

ledUtils.init_LEDs()

while True:
	try:
		response = urllib.urlopen(url).read()
		print response
		
		data = json.loads(response)['data']
		print data
		color = int(data['brightness'] / interval)
		print color
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
		print 'An error occured'
		continue

# clean up
cleanUp()