import numpy as np
import matplotlib.pyplot as plt

def loadFile(fileName):
	f = open(fileName)

	timesMap = {}

	totalTimes = 0;

	for rawLine in f:
		line = rawLine.strip().split(":")
		wordTimes = float(line[0])
		timesValue = float(line[1])

		totalTimes += timesValue

		timesMap.setdefault(wordTimes, timesValue)

	
	wordTimesSortedList = sorted(timesMap.keys(), reverse=True)

	accumulateTimes = 0
	x = []
	y = []
	for wordTimes in wordTimesSortedList:
		timesValue = timesMap[wordTimes]
		print wordTimes, timesValue
		accumulateTimes += timesValue

		prob = accumulateTimes*1.0/totalTimes

		timesMap[wordTimes] = prob

		x.append(wordTimes)
		y.append(prob)

	return x, y

def plotXY(x, y):
	xLen = len(x)
	for eachXIndex in range(xLen):
		print x[xLen-eachXIndex-1], "\t",

	for eachXIndex in range(xLen):
		print y[xLen-eachXIndex-1], "\t",
	plt.plot(x, y)
	plt.show()


file1 = "burstiness_merged.txt"
# file1 = "burstiness.txt"

x, y = loadFile(file1)

plotXY(x, y)
