import numpy as np

def loadFile(fileName, corpusObj):
	f = open(fileName)

	stnIndex = 0
	for rawLine in f:
		line = rawLine.strip().split("\t")

		if stnIndex == 0:
			parentName = line[0]
			stnNum = float(line[1])

			parentObj = _ParentDoc(parentName)



	return stnMap



