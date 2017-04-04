import numpy as np
import matplotlib.pyplot as plt

def readFile(fileName, xList):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")

		xList.append(float(line[1]))

	f.close()
	return xList

def plotHistogram(xList):
	orderedXList = sorted(xList)

	H, X1 = np.histogram(xList, bins=10, normed=True)
	dx = X1[1]-X1[0]
	F1 = np.cumsum(H)*dx

	plt.plot(X1[1:], F1)
	plt.xlabel("x=0 proportion")
	plt.ylabel("cdf")
	plt.title("WECM x distribution")
	plt.show()


xFile = "./xVal.txt"
xList = list()

readFile(xFile, xList)
plotHistogram(xList)
