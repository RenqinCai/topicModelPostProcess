
def loadFile(fileName1, fileName2):
	f1 = open(fileName1)
	f2 = open(fileName2)

	stnMap1 = {}
	stnMap2 = {}

	for rawLine1 in f1:
		line = rawLine1.strip().split("\t")
		# print "line\t", line
		stnName = line[1]
		apDiff = float(line[2])

		stnMap1.setdefault(stnName, apDiff)
	f1.close()

	for rawLine2 in f2:
		line = rawLine2.strip().split("\t")
		# print "line\t", line
		stnName = line[1]
		apDiff = float(line[2])

		stnMap2.setdefault(stnName, apDiff)
	f2.close()

	return stnMap1, stnMap2

def getCommonLarge(stnMap1, stnMap2):

	for stnName in stnMap1.keys():
		if stnName in stnMap2.keys():
			apDiff1 = stnMap1[stnName]
			apDiff2 = stnMap2[stnName]

			if apDiff1 > 0.5:
				if apDiff2 > 0.5:
					print stnName, "\t", apDiff1, "\t", apDiff2

# fileName1 = "./LDABetter.txt"
# fileName2 = "./LDABetter2.txt"

# fileName1 = "./ACCTMBetter.txt"
# fileName2 = "./ACCTMBetter2.txt"

fileName1 = "./ACCTMBetter4.txt"
fileName2 = "./ACCTMBetter5.txt"

(stnMap1, stnMap2) = loadFile(fileName1, fileName2)
getCommonLarge(stnMap1, stnMap2)