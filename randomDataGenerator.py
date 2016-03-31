import datetime,random

outputFile = open(r'c:\code\randomData.csv','w')
startTime = datetime.datetime(2015,1,1,0,0,0,0)
baseValue = 70.0
maxIncrease = 10.0
minIncrease = -10.0
dataCount = 20000

outputFile.write('sample_time,sample_value\n')

currentTime = startTime
for i in range(0,dataCount):
	currentTime = currentTime + datetime.timedelta(minutes = 1)
	randomValue = baseValue + random.uniform(minIncrease,maxIncrease)
	outString = '%s,%s\n' % (str(currentTime + datetime.timedelta(seconds = random.uniform(0,10))),randomValue)
	print outString
	outputFile.write(outString)

outputFile.close()
