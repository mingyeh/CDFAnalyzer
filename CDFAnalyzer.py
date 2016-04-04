import math, numpy as np, copy

class CDF:
	__private_rawData = []
	__private_dataCount = 0
	__private_mean = 0
	__private_std = 0

	def __init__(self, data):
		self.__private_rawData = copy.copy(data)
		self.__private_dataCount = len(self.__private_rawData)
		self.__private_mean = np.mean(self.__private_rawData)
		self.__private_std = np.std(self.__private_rawData)

	def getDataCount(self):
		return self.__private_dataCount

	def getMean(self):
		return self.__private_mean

	def getStandardDeviation(self):
		return self.__private_std

if __name__ == '__main__':
	cdf = CDF([i for i in range(0,100)])
	print 'Data Count: %s\nMean: %s\nStandard Deviation: %s' % (cdf.getDataCount(), cdf.getMean(), cdf.getStandardDeviation())

