import math, numpy as np, copy, os, sys

class CDF:
    __private_data = []
    __private_uniqueData = []
    __private_dataCount = 0
    __private_mean = 0
    __private_std = 0

    def __init__(self, data):
        self.__private_data = copy.copy(data)
        self.__private_uniqueData = np.unique(self.__private_data)
        self.__private_dataCount = len(self.__private_data)
        self.__private_mean = np.mean(self.__private_data)
        self.__private_std = np.std(self.__private_data)

    def getDataCount(self):
        return self.__private_dataCount

    def getMean(self):
        return self.__private_mean

    def getSTD(self):
        return self.__private_std

    def getCDData(self, groups, sorting = 'ASC'):
        #Argument validation
        sorting = sorting.upper()
        if sorting not in ('ASC','DESC'):
            raise ValueError,"Parameter 'sorting' can only be either 'ASC' or 'DESC'"
        if not str(groups).isdigit():
            raise ValueError, "Parameter 'groups' can only be digit number"

        #Result lists
        xList = []
        yList = []

        #Sort the data
        dataList = copy.copy(self.__private_data)
        dataList.sort()
        if sorting == 'DESC':
            dataList.reverse()

        #Generate groups
        first_value = dataList[0]
        last_value = dataList[self.__private_dataCount - 1]
        groups_array = np.linspace(first_value, last_value, groups)

        #Compute CD data
        group_first = 0
        for value in groups_array:
            for i in range(group_first, self.__private_dataCount):
                if (sorting == 'ASC' and dataList[i] > value) or (sorting == 'DESC' and dataList[i] < value):
                    group_first = i
                    xList.append(value) 
                    yList.append(i * 1.0 / self.__private_dataCount)
                    break
        xList.append(last_value)
        yList.append(1.0)

        return (xList, yList)

if __name__ == '__main__':
    sampleData = list(np.random.normal(10.0, 1, 1000))
    cdf = CDF(sampleData)
    print 'Data Count: %s\nMean: %s\nStandard Deviation: %s' % (cdf.getDataCount(), cdf.getMean(), cdf.getSTD())
    resultData = cdf.getCDData(groups = 100, sorting = 'desc')
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
