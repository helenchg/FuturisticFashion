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
print modes[0]
print modes[1]
modeIdx = (modeIdx + 1) % nModes
currMode = modes[modesIdx]

modeIdx = (modeIdx + 1) % nModes
currMode = modes[modesIdx]

modeIdx = (modeIdx + 1) % nModes
currMode = modes[modesIdx]

modeIdx = (modeIdx + 1) % nModes
currMode = modes[modesIdx]

ledUtils.init_LEDs()

# if grabStrength > threshold for changeModeThreshold, change mode
changeModeThreshold = 8
grabThreshold = 0.9
grabCounter = 0

# while True:

	# try:
		# response = urllib.urlopen(url).read()
		# print response
		# data = json.loads(response)['bigdata']
		# print data
		
		# if data['grabstrength'] > grabThreshold:
			# grabCounter += 1
			# if grabCounter >= changeModeThreshold:
				# fist held for long enough, change mode
				# modeIdx = (modeIdx + 1) % nModes
				# print modeIdx, modes
				# currMode = modes[modesIdx]
				# grabCounter = 0
				# print 'Entering mode: ', currMode.name
		
		# if data['handcount'] == 0:
			# print 'No hands were detected. Please try again.'
		# else:
			# currMode.process(data)

	# except KeyboardInterrupt:
		# break
	# except:
		# print 'An error occured'
		# continue

# clean up
ledUtils.cleanUp()