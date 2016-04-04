import math, numpy as np, copy, os, sys

class CDF:
    __private_sortedData = []
    __private_uniqueData = []
    __private_dataCount = 0
    __private_mean = 0
    __private_std = 0

    def __init__(self, data):
        self.__private_sortedData = copy.copy(data)
        self.__private_sortedData.sort()
        self.__private_uniqueData = np.unique(self.__private_sortedData)
        self.__private_dataCount = len(self.__private_sortedData)
        self.__private_mean = np.mean(self.__private_sortedData)
        self.__private_std = np.std(self.__private_sortedData)

    def getDataCount(self):
        return self.__private_dataCount

    def getMean(self):
        return self.__private_mean

    def getSTD(self):
        return self.__private_std

    def getCDData(self, sorting = 'ASC'):
        sorting = sorting.upper()
        if sorting not in ('ASC','DESC'):
            raise ValueError,"Parameter can only be either 'ASC' or 'DESC'"
        xList = []
        yList = []
        dataList = []
        if sorting == 'ASC':
            dataList = copy.copy(self.__private_sortedData)
            dataList.reverse()
            xList = self.__private_uniqueData
        else:
            dataList = self.__private_sortedData
            xList = copy.copy(self.__private_uniqueData)
            xList.reverve()

        for d in xList:
            yList.append((self.__private_dataCount - dataList.index(d)) * 1.0 / self.__private_dataCount)

        return (xList, yList)

if __name__ == '__main__':
    sampleData = [0.000000023, 0.000004653, 0.000255472, 0.002161668, 0.008506355, 0.022004493, 0.043655827, 0.072118903, 0.104195635, 0.135891934, 0.163482069, 0.184236358, 0.196722368, 0.200752145, 0.19711215, 0.187209165, 0.172729521, 0.155366517, 0.136635479, 0.117772356, 0.099699433, 0.083037811, 0.068147615, 0.055180665, 0.044134867, 0.034903708, 0.027317505, 0.021175394, 0.016268481, 0.012395371, 0.009371594, 0.007034433, 0.005244519, 0.003885297, 0.002861207, 0.002095228]
    #sampleData = [10.67, 10.40, 11.30, 11.80, 12.06, 12.18, 12.22, 12.25, 12.25, 12.29, 12.31, 13.32, 12.33, 12.34, 12.35, 14.36, 14.37, 14.38, 14.39, 12.40, 13.39, 12.40, 14.41, 12.41, 12.42, 12.49, 7.42, 7.79, 8.36, 8.78, 9.07, 9.25, 9.34, 9.58, 9.65, 9.93, 10.23, 10.39, 10.49, 10.56, 10.62, 10.48, 10.68, 10.72, 10.73, 10.85, 10.38, 9.61, 9.05, 8.84, 8.78, 4.31, 4.37, 4.69, 5.26, 5.33, 5.53, 5.68, 5.85, 6.00, 6.15, 6.30, 6.46, 6.60, 6.74, 6.26, 6.14, 6.19, 6.20, 6.20, 6.18, 6.18, 6.18, 6.15, 6.02, 5.89, 4.03, 3.60, 3.95, 4.36, 4.69, 4.85, 4.89, 4.90, 4.97, 5.02, 5.08, 5.15, 5.23, 5.49, 5.76, 5.42, 4.96, 4.79, 4.66, 4.57, 4.51, 4.47, 4.45, 4.43, 4.48, 7.48, 7.60, 7.66, 7.71, 7.77, 7.81, 7.84, 7.86, 7.85, 7.83, 7.82, 7.82, 7.81, 7.81, 7.80, 7.81, 7.75, 7.24, 2.94, 0.18, 0.28, 0.25, 0.22] 
    cdf = CDF(sampleData)
    print 'Data Count: %s\nMean: %s\nStandard Deviation: %s' % (cdf.getDataCount(), cdf.getMean(), cdf.getSTD())
    resultData = cdf.getCDData()
    currentPath = ''
    sysPath = sys.path[0]
    if os.path.isdir(sysPath):
        currentPath = sysPath
    elif os.path.isfile(sysPath):
        currentPath = os.path.dirname(sysPath)
    dataOutputFile = open('%s%s%s' % (currentPath, os.sep, r'\randomData.csv'), 'w')
    for i in range(0, len(resultData[0])):
        dataOutputFile.write('%s,%s\n' % (resultData[0][i],resultData[1][i]))

    dataOutputFile.close()
