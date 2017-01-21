import numpy as np
import os

#######
######iterate all vocabulary 
####the denominator is vocabulary*corpusSize
#######

class _parentDoc:
	def __init__(self, name):
		self.m_name = name
		### wid:frequency
		self.m_wordFrequency = {}

	def getWordFrequency(self, wid):
		return self.m_wordFrequency[wid]

	def addWordFrequency(self, wid):
		if wid not in self.m_wordFrequency.keys():
			self.m_wordFrequency.setdefault(wid, 1)
		else:
			self.m_wordFrequency[wid] += 1

class _corpus:
	def __init__(self):

		self.m_featureList = []
		##docID: docObj
		self.m_docMap = {}
		###times: timesFrequency
		self.m_timesMap = {}
		self.m_totalTimes = 0
		self.m_timesProbMap = {}

	def addDoc(self, docID, pDoc):
		self.m_docMap.setdefault(docID, pDoc)

	def addFrequency(self, times):
		# print times
		if times not in self.m_timesMap.keys():
		#	print times
			self.m_timesMap.setdefault(times, 1)
		else:
			self.m_timesMap[times] += 1

		self.m_totalTimes += 1

	def addZero(self, frequency):
		if 0 not in self.m_timesMap.keys():
			self.m_timesMap.setdefault(0, frequency)
		else:
			self.m_timesMap[0] += frequency

	def setProb(self, featureSize, docSize):
		print self.m_timesMap.keys()
		sortedTimesList = sorted(self.m_timesMap.keys(), reverse=True)
		# print sortedTimesList

		totalTimes = featureSize*docSize;

		frequency = 0
		for times in sortedTimesList:

			frequency = self.m_timesMap[times]
			# print frequency
			# print "#########"
			prob = frequency*1.0/totalTimes

			self.m_timesProbMap.setdefault(times, prob)

		# print frequency 

	def getProb(self, times):
		return self.m_timesProbMap.get(times)


def loadFile(dirName, fileName, corpusObj):
	fileAbsoluteName = os.path.join(dirName, fileName)
	f = open(fileAbsoluteName)

	# print fileAbsoluteName 
	fileIndex = fileName.split(".")[0]

	pDoc = _parentDoc(fileIndex)
	for rawLine in f:
		line = rawLine.strip().split("\t")

		lineLen = len(line)

		for i in range(lineLen):
			wid = line[i]
			pDoc.addWordFrequency(wid)

			# print wid
			if wid not in corpusObj.m_featureList:
				corpusObj.m_featureList.append(wid)

	corpusObj.addDoc(fileIndex, pDoc)

def loadCorpus(dirName, corpusObj):
	for fileName in os.listdir(dirName):
		if fileName.endswith(".txt"):
			loadFile(dirName, fileName, corpusObj)

def burstinessStatistics(corpusObj, burstinessFile):

	f = open(burstinessFile, "w")

	fileNum = 0
	featureSize = len(corpusObj.m_featureList)
	docSize = 0
	for fileIndex in corpusObj.m_docMap.keys():
		fileNum += 1
		docSize += 1
		# print fileIndex
		pDoc = corpusObj.m_docMap[fileIndex]

		for wid in pDoc.m_wordFrequency.keys():
			times = pDoc.m_wordFrequency[wid]
			corpusObj.addFrequency(times)

		zeroWordNum = featureSize - len(pDoc.m_wordFrequency)
		corpusObj.addZero(zeroWordNum)

	print fileNum, featureSize, docSize
	corpusObj.setProb(featureSize, docSize)


	for times in corpusObj.m_timesProbMap.keys():
		print times, "\t", corpusObj.getProb(times)
		f.write(str(times)+":"+str(corpusObj.getProb(times))+"\n")

	f.close()


corpusObj = _corpus()
dirName = "./20160913-2202-Burstiness-YahoofakeCorpus"
loadCorpus(dirName, corpusObj)

outputFile = "20160913-2202-Burstiness-YahoofakeCorpus_statistics.txt"
burstinessStatistics(corpusObj, outputFile)

