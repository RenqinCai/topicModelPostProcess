import numpy as np
import matplotlib.pyplot as plt

###the data imported as NumOfWords:Probability

def loadFile(fileName):
	f = open(fileName)

	timesMap = {}

	totalTimes = 0;

	for rawLine in f:
		line = rawLine.strip().split(":")
		wordTimes = float(line[0])
		timesProb = float(line[1])

		timesMap.setdefault(wordTimes, timesProb)

	
	wordTimesSortedList = sorted(timesMap.keys(), reverse=True)

	accumulateTimes = 0
	x = []
	y = []
	for wordTimes in wordTimesSortedList:
		timesProb = timesMap[wordTimes]
		# print wordTimes, timesProb

		x.append(wordTimes)
		y.append(timesProb)

	return x, y

def averageXY(x, y):
	xTimesMap = {}
	yProbMap = {}

	sampleLen = len(x)

	for sampleIndex in range(sampleLen):
		xSample = x[sampleIndex]
		xLen = len(xSample)

		ySample = y[sampleIndex]
		yLen = len(ySample)

		if xLen != yLen:
			print "error"
			break

		for i in range(xLen):
			xUnit = xSample[i]
			yUnit = ySample[i]

			if xUnit not in xTimesMap.keys():
				xTimesMap.setdefault(xUnit, 0)

			oldVal = xTimesMap[xUnit]
			xTimesMap[xUnit] = oldVal+1

			if xUnit not in yProbMap.keys():
				yProbMap.setdefault(xUnit, [])

			yProbMap[xUnit].append(yUnit)


	xAvgList = []

	yAvgList = []
	yVarList = []

	xAvgList = sorted(xTimesMap.keys(), reverse=True)

	for xUnit in xAvgList:
		xTimes = xTimesMap[xUnit]

		yList = yProbMap[xUnit]

		avgY = np.mean(yList)
		varY = np.sqrt(np.var(yList))

		print xUnit, "\t", avgY, "\t", varY

		yAvgList.append(avgY)
		yVarList.append(varY)

	return xAvgList, yAvgList, yVarList


def plotXY(x, y):
	xLen = len(x)
	for eachXIndex in range(xLen):
		print x[xLen-eachXIndex-1], "\t",

	for eachXIndex in range(xLen):
		print y[xLen-eachXIndex-1], "\t",
	plt.plot(x, y)
	plt.show()

def plotTwoXY_Variance(x1, y1, x2, y2, yVarList):
	# handle1, = plt.semilogy(x1, y1, label="Tech dataset")
	# handle2, = plt.semilogy(x2, y2, label="Synthetic dataset")

	print yVarList
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_yscale('log')
	ax.errorbar(x1, y1, label="natrual merged documents")
	ax.errorbar(x2, y2, yerr=[yVarList, yVarList], label="synthetic merged documents")
	# handle1, a, b= ax.errorbar(x1, y1, label="Tech dataset")
	# handle2, c, d= ax.errorbar(x2, y2, label="Synthetic dataset")

	# handles = []
	# handles.append(handle1)
	# handles.append(handle2)
	plt.ylabel("probability")
	plt.xlabel("a word occuring x times in a document")
	plt.legend()
	# plt.legend(handles=handles)
	plt.title("burstiness")
	plt.savefig("burstiness.png", format="png", dpi=1000)
	plt.show()

def plotTwoXY(x1, y1, x2, y2):
	handle1, = plt.semilogy(x1, y1, label="ArsTechnica Blog")
	handle2, = plt.semilogy(x2, y2, label="Synthetic Blog")


	# handle1, = plt.plot(x1, y1, label="Tech dataset")
	# handle2, = plt.plot(x2, y2, label="Synthetic dataset")

	# print yVarList
	# fig = plt.figure()
	# ax = fig.add_subplot(111)
	# ax.set_yscale('log')
	# ax.errorbar(x1, y1, label="original merged documents")
	# ax.errorbar(x2, y2, yerr=[yVarList, yVarList], label="fake merged documents")
	

	handles = []
	handles.append(handle1)
	handles.append(handle2)
	plt.ylabel("probability")
	plt.xlabel("a word occuring x times in a document")
	# plt.legend()
	# plt.xlim([0, 50])
	plt.legend(handles=handles)
	plt.title("burstiness")
	plt.savefig("burstiness_Tech.png", format="png", dpi=1000)
	plt.show()

def outputAvgList(x1, y1, yval, outputFile):
	f = open(outputFile, "w")

	elementLen = len(x1)

	for elementIndex in range(elementLen):
		x1Element = x1[elementIndex]
		y1Element = y1[elementIndex]
		yvalElement = yval[elementIndex]
		f.write(str(x1Element)+"\t"+str(y1Element)+"\t"+str(yvalElement)+"\n")

	f.close()

# file21 = "20160913-2024-Burstiness-TechfakeCorpus_statistics.txt"
# file22 = "20160913-2019-Burstiness-TechfakeCorpus_statistics.txt"
# file23 = "20160822-1044-Burstiness-TechfakeCorpus_statistics.txt"
# file24 = "20160822-1046-Burstiness-TechfakeCorpus_statistics.txt"
# file25 = "20160822-1050-Burstiness-TechfakeCorpus_statistics.txt"
# file26 = "20160822-1057-Burstiness-TechfakeCorpus_statistics.txt"
# file27 = "20160822-1100-Burstiness-TechfakeCorpus_statistics.txt"
# file28 = "20160822-1102-Burstiness-TechfakeCorpus_statistics.txt"
# file29 = "20160822-1103-Burstiness-TechfakeCorpus_statistics.txt"
# file30 = "20160822-1104-Burstiness-TechfakeCorpus_statistics.txt"
# file1 = "20160913-2026-Burstiness-Tech_burstiness.txt"

file21 = "20160913-2043-Burstiness-YahoofakeCorpus_statistics.txt"
file22 = "20160913-2053-Burstiness-YahoofakeCorpus_statistics.txt"
file23 = "20160913-2102-Burstiness-YahoofakeCorpus_statistics.txt"
file24 = "20160913-2112-Burstiness-YahoofakeCorpus_statistics.txt"
file25 = "20160913-2231-Burstiness-YahoofakeCorpus_statistics.txt"
file26 = "20160913-2228-Burstiness-YahoofakeCorpus_statistics.txt"
file27 = "20160913-2241-Burstiness-YahoofakeCorpus_statistics.txt"
file28 = "20160913-2245-Burstiness-YahoofakeCorpus_statistics.txt"
file29 = "20160913-2153-Burstiness-YahoofakeCorpus_statistics.txt"
file30 = "20160913-2202-Burstiness-YahoofakeCorpus_statistics.txt"
file1 = "20160913-2038-Burstiness-Yahoo_burstiness.txt"

x1, y1 = loadFile(file1)
x21, y21 = loadFile(file21)
x22, y22 = loadFile(file22)
x23, y23 = loadFile(file23)
x24, y24 = loadFile(file24)
x25, y25 = loadFile(file25)
x26, y26 = loadFile(file26)
x27, y27 = loadFile(file27)
x28, y28 = loadFile(file28)
x29, y29 = loadFile(file29)
x30, y30 = loadFile(file30)

x = []
y = []
x.append(x21)
y.append(y21)

x.append(x22)
y.append(y22)

x.append(x23)
y.append(y23)

x.append(x24)
y.append(y24)

x.append(x25)
y.append(y25)

x.append(x26)
y.append(y26)

x.append(x27)
y.append(y27)

x.append(x28)
y.append(y28)

x.append(x29)
y.append(y29)

x.append(x30)
y.append(y30)
# plotXY(x2, y2)
# plotTwoXY(x1, y1, x21, y21)

avgXList, avgYList, yVarList = averageXY(x, y)

outputFile = "yahoo_burstiness.txt"
outputAvgList(avgXList, avgYList, yVarList, outputFile)

plotTwoXY_Variance(x1, y1, avgXList, avgYList, yVarList)

