import datetime, random, sys, os

class randomValueGenerator:
	@staticmethod
	def writeToCSV(outputFilePath, startTime, timeDelta, baseValue = 0, valueRange = 10, dataCount = 1000): 
		outputFile = open(outputFilePath,'w')
		maxIncrease = valueRange
		minIncrease = 0 - valueRange

		outputFile.write('sample_time,sample_value\n')

		currentTime = startTime
		for i in range(0,dataCount):
			currentTime = currentTime + timeDelta
			randomValue = baseValue + random.uniform(minIncrease,maxIncrease)
			outString = '%s,%s\n' % (str(currentTime + datetime.timedelta(seconds = random.uniform(0,10))),randomValue)
			print outString
			outputFile.write(outString)

		outputFile.close()

if __name__ == '__main__':
	currentPath = ''
	sysPath = sys.path[0]
	if os.path.isdir(sysPath):
		currentPath = sysPath
	elif os.path.isfile(sysPath):
		currentPath = os.path.dirname(sysPath)
	randomValueGenerator.writeToCSV(outputFilePath = '%s%s%s' % (currentPath, os.sep, r'\randomData.csv'), startTime = datetime.datetime(2015,1,1,0,0,0,0), timeDelta = datetime.timedelta(minutes = 1))
