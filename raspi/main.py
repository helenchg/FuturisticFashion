import json
import urllib
import ledUtils
import dataProcessors
import sys

# vars
url = 'http://leapfashion.herokuapp.com/api/bigdata'

modes = []
modes.append(dataProcessors.PinchColor())
modes.append(dataProcessors.WhiteOrBlue())
nModes = len(modes)
modeIdx = 0;
currMode = modes[modeIdx]
ledUtils.init_LEDs()

# if grabStrength > threshold for changeModeThreshold, change mode
changeModeThreshold = 8
grabThreshold = 0.95
grabCounter = 0

while True:

	try:
		response = urllib.urlopen(url).read()
		# print response
		data = json.loads(response)['bigdata']
		
		if data['handcount'] == 0:
			print 'No hands were detected. Please try again.'
		elif data['grabstrength'] > grabThreshold:
			ledUtils.all_LEDs_on()
			ledUtils.all_LEDs_steady()
			grabCounter += 1
			if grabCounter >= changeModeThreshold:
				# fist held for long enough, change mode
				modeIdx = (modeIdx + 1) % nModes
				currMode = modes[modeIdx]
				grabCounter = 0
				print 'Entering mode: ', currMode.name
		else:
			currMode.process(data)

	except KeyboardInterrupt:
		break
	except:
		print 'An error occured: ', sys.exc_info()
		continue

# clean up
ledUtils.cleanUp()