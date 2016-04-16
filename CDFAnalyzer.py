import math, numpy as np, copy, os, sys, matplotlib.pyplot as plt

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

    def getCNDCurve(self, groups, sorting = 'ASC', n = 64):
        #Arguments validation
        sorting = sorting.upper()
        if sorting not in ('ASC', 'DESC'):
            raise ValueError, "Parameter 'sorting' can only be either 'ASC' or 'DESC'"
        if not str(groups).isdigit():
            raise ValueError, "Parameter 'groups' can only be digit number"
        if not str(n).isdigit():
            raise ValueError, "Parameter 'n' can only be digit number"

        #result lists
        xList = []
        yList = []

        #Sort the data
        dataList = copy.copy(self.__private_data)
        dataList.sort()
        if sorting == 'DESC':
            dataList.reverse()

        #Generate Groups
        first_value = dataList[0]
        last_value = dataList[self.__private_dataCount - 1]
        groups_array = np.linspace(first_value, last_value, groups)

        y = 0.0
        for value in groups_array:
            erf = (value - self.__private_mean) / (self.__private_std * math.sqrt(2))
            for i in range(0, n):
                y += math.pow(-1, i) * math.pow(erf, 2 * i + 1) / ((2 * i + 1) * (1 if i == 0 else math.factorial(i)))
            y = y / math.sqrt(math.pi) + 0.5
            xList.append(value)
            yList.append(y)
            y = 0.0

        return (xList, yList)

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
    #Generate random data for analysis
    sampleData = list(np.random.normal(10.0, 1, 1000))
    cdf = CDF(sampleData)
    print 'Data Count: %s\nMean: %s\nStandard Deviation: %s' % (cdf.getDataCount(), cdf.getMean(), cdf.getSTD())
    
    resultData = cdf.getCDData(groups = 100, sorting = 'asc')
    cndCurveData = cdf.getCNDCurve(groups = 100, sorting = 'asc', n = 64)
    
    plt.scatter(resultData[0], resultData[1], color = 'red', alpha = 0.3, label = 'Cumulative Distribution')
    plt.plot(cndCurveData[0], cndCurveData[1], color = 'blue')
    plt.xlabal = 'Value'
    plt.ylabal = 'Probability'
    plt.grid(True)
    plt.show()
