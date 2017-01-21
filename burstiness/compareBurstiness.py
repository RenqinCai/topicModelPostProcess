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
		accumulateTimes += timesValue

		prob = accumulateTimes*1.0/totalTimes

		timesMap[wordTimes] = prob

		x.append(wordTimes)
		y.append(prob)

	return x, y

def plotXY(x1, y1, x2, y2):
	print x1
	print y1

	print x2 
	print y2
	handles1, = plt.plot(x1, y1, 'r', label="corpus")
	handles2, = plt.plot(x2, y2, 'b', label="fakeCorpus")
	t_handles = []
	t_handles.append(handles1)
	t_handles.append(handles2)
	plt.legend(handles=t_handles)
	plt.show()


file1 = "burstiness.txt"
file2 = "fakeBurstiness.txt"
x1, y1 = loadFile(file1)
x2, y2 = loadFile(file2)

plotXY(x1, y1, x2, y2)
