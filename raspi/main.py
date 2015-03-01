import json
import urllib
import ledUtils
import dataProcessors

# vars
url = 'http://leapfashion.herokuapp.com/api/bigdata'

#initialize things
ledUtils.init_LEDs()
processor = dataProcessors.WhiteOrBlue()

while True:

	try:
		response = urllib.urlopen(url).read()
		# print response
		data = json.loads(response)['bigdata']
		processor.process(data)
	except KeyboardInterrupt:
		break
	except:
		print 'An error occured'
		continue

# clean up
ledUtils.cleanUp()