import json
import urllib
import ledUtils
import dataProcessors

# vars
url = 'http://leapfashion.herokuapp.com/api/bigdata'

modes = []
modes.append(dataProcessors.PinchColor())
modes.append(dataProcessors.WhiteOrBlue())
nModes = len(modes)
modeIdx = 0;
currMode = modes[modeIdx]

ledUtils.init_LEDs()

while True:

	try:
		response = urllib.urlopen(url).read()
		# print response
		data = json.loads(response)['bigdata']
		if data['handcount'] == 0:
			print 'No hands were detected. Please try again.'
		elif data['swipegesture'] == 1:
			modeIdx = (modeIdx + 1) % nModes
			currMode = modes[modesIdx]
			print 'Entering mode: ', currMode.name
		else:
			print currMode
			currMode.process(data)
	except KeyboardInterrupt:
		break
	except:
		print 'An error occured'
		continue

# clean up
ledUtils.cleanUp()