import os
class _Feature:
	def __init__(self, name):
		self.m_name = name
		self.m_TTF = 0
		self.m_phiTTF = 0

	def addTTF(self):
		self.m_TTF += 1

	def addPhiTTF(self, val):
		self.m_phiTTF += val

def readXDir(dirName, corpusObj):
	for fileName in os.listdir(dirName):
		if fileName.endswith(".txt"):
			readXFile(corpusObj, dirName, fileName)

def readXFile(corpusObj, dirName, fileName):
	dirFileName = os.path.join(dirName, fileName)
	f = open(dirFileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		wordNum = len(line)
		for i in range(wordNum):
			word = line[i].strip().split(":")
			wordName = word[0]
			wordProb = float(word[2])

			# print word
			featureObj = None
			if wordName not in corpusObj.keys():
				featureObj = _Feature(wordName)
				corpusObj.setdefault(wordName, featureObj)
			else:
				featureObj = corpusObj[wordName]

			# print "wordProb\t", wordProb
			# print debug
			featureObj.addTTF()
			featureObj.addPhiTTF(wordProb)

	f.close()

def readTopWords(fileName):
	f = open(fileName)

	topWordsList = []

	for rawLine in f:
		line = rawLine.strip().split("\t")
		lineLen = len(line)

		for i in range(2, lineLen):
			word = line[i].strip().split("(")
			wordName = word[0]

			if wordName in topWordsList:
				continue
			topWordsList.append(wordName)

	return topWordsList

def statisticsTopWords(corpusObj, topWordsList, threshold):
	missingImportantWordList = []

	for word in topWordsList:
		wordObj = corpusObj[word]

		TTF = wordObj.m_TTF
		phiTTF = wordObj.m_phiTTF

		TTFRatio = phiTTF/TTF*1.0

		if TTFRatio > threshold:
			print TTFRatio
			missingImportantWordList.append(word)

	return missingImportantWordList


corpusObj = {}
# ACCTMCdirName = "./XValue" 
# readXDir(ACCTMCdirName, corpusObj)
# 
ACCTMPDirName1 = "./ParentXValue"
ACCTMPDirName2 = "./ChildXValue"
readXDir(ACCTMPDirName1, corpusObj)
readXDir(ACCTMPDirName2, corpusObj)


ldaTopWordFile = "./LDA_topWords.txt"
threshold = 0.1

topWordsList = readTopWords(ldaTopWordFile)
missingImportantWordList = statisticsTopWords(corpusObj, topWordsList, threshold)
print missingImportantWordList
print len(missingImportantWordList)*1.0/len(topWordsList)


