import os
import numpy

class _Corpus:
	def __init__(self):
		print "initial corpus"
		self.m_docMap = dict()
		self.m_topicMap = dict()

class _Doc:
	def __init__(self):
		self.m_name = ""
		self.m_topicVec = []
		self.m_maxIndex = -1

	def setName(self, name):
		self.m_name = name

	def setMaxIndex(self, index):
		self.m_maxIndex = index

	def addTopicProportion(self, topicPro):
		self.m_topicVec.append(topicPro)


def loadFile(fileName, topicSize, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")

		docName = line[0]

		docObj = None

		if docName not in corpusObj.m_docMap.keys():
			docObj = _Doc()
			docObj.setName(docName)
			corpusObj.m_docMap.setdefault(docName, docObj)
		else:
			docObj = corpusObj.m_docMap[docName]

		maxTopicIndex = -1
		maxTopicPro = 0

		for i in range(topicSize):
			topicPro = float(line[i+2])
			docObj.addTopicProportion(topicPro)

			if topicPro > maxTopicPro:
				maxTopicIndex = i
				maxTopicPro = topicPro

			docObj.setMaxIndex(maxTopicIndex)

		if maxTopicIndex not in corpusObj.m_topicMap.keys():
			corpusObj.m_topicMap.setdefault(maxTopicIndex, [])
			corpusObj.m_topicMap[maxTopicIndex].append(docName)
		else:
			corpusObj.m_topicMap[maxTopicIndex].append(docName)

	f.close()

def topDoc4Topic(corpusObj):
	for topicIndex in corpusObj.m_topicMap.keys():
		topicProDocMap = {}
		docNameList = corpusObj.m_topicMap[topicIndex]

		for docName in docNameList:
			docObj = corpusObj.m_docMap[docName]

			topicPro = docObj.m_topicVec[topicIndex]

			topicProDocMap.setdefault(docName, topicPro)

		topDoc4TopirProList = sorted(topicProDocMap, key=topicProDocMap.__getitem__, reverse=True)

		print "top doc for topic index\t", topicIndex
		print len(topDoc4TopirProList)
		for i in range(3):
			print topDoc4TopirProList[i]

parentFile = "ACCTM_C_Hard_parentParameter.txt"
childFile = "ACCTM_C_Hard_childParameter.txt"

# parentFile = "LDA_parentParameter.txt"
# childFile = "LDA_childParameter.txt"

topicSize = 30
corpusObj = _Corpus()

loadFile(parentFile, topicSize, corpusObj)

# loadFile(childFile, topicSize, corpusObj)

topDoc4Topic(corpusObj)

