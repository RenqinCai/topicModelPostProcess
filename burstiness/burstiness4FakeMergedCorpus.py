import numpy as np
import os

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

	def setProb(self):
		print self.m_timesMap.keys()
		sortedTimesList = sorted(self.m_timesMap.keys(), reverse=True)
		# print sortedTimesList

		print self.m_totalTimes

		frequency = 0
		for times in sortedTimesList:

			print self.m_timesMap[times]
			print "....."
			frequency += self.m_timesMap[times]
			print frequency
			print "#########"
			prob = frequency*1.0/self.m_totalTimes

			self.m_timesProbMap.setdefault(times, prob)

		print frequency 

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

	corpusObj.addDoc(fileIndex, pDoc)

def loadCorpus(dirName, corpusObj):
	for fileName in os.listdir(dirName):
		if fileName.endswith(".txt"):
			loadFile(dirName, fileName, corpusObj)

def burstinessStatistics(corpusObj):
	fileNum = 0
	for fileIndex in corpusObj.m_docMap.keys():
		fileNum += 1
		# print fileIndex
		pDoc = corpusObj.m_docMap[fileIndex]

		for wid in pDoc.m_wordFrequency.keys():
			times = pDoc.m_wordFrequency[wid]
			corpusObj.addFrequency(times)

	print fileNum
	corpusObj.setProb()

	for times in corpusObj.m_timesProbMap.keys():
		print times, "\t", corpusObj.getProb(times)

corpusObj = _corpus()
dirName = "./Burstiness-TechfakeMergedCorpus"
loadCorpus(dirName, corpusObj)
burstinessStatistics(corpusObj)

