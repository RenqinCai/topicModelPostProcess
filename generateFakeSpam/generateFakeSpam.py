import numpy as np
import random
import json

class _ParentDoc:
	def __init__(self):
		self.m_name = ""
		self.m_topicProportion = {}

class _ChildDoc:
	def __init__(self):
		self.m_name = ""
		self.m_topicProportion = []

class _Beta:
	def __init__(self):
		self.m_topicWord = {}

def loadParentFile(fileName, corpusObj):
	f = open(fileName, 'r')
	for rawLine in f:
		parentObj = _ParentDoc()
		line = rawLine.strip().split("\t")

		parentName = line[0]
		parentObj.m_name = parentName

		topicLen = 30

		for i in range(0, 30):
			topicPro = float(line[i+2])

			parentObj.m_topicProportion.setdefault(i, topicPro)

		corpusObj.setdefault(parentName, parentObj)
		corpusObj[parentName] = parentObj

def loadTopWordFile(fileName, betaObj):
	f = open(fileName, "r")
	lineIndex = 0
	for rawLine in f:
		line = rawLine.strip().split("\t")
		#print line
		# print debug

		wordList = []
		lineLen = len(line)
		for i in range(1, lineLen):
			wordUnit = line[i]
			word = wordUnit.strip().split("(")[0]
			wordList.append(word)

		betaObj.m_topicWord.setdefault(lineIndex, wordList)
		lineIndex += 1

def randomGenerateFakeComments(corpusObj, betaObj, selectedParentLen, cmntLen):
	parentSize = len(corpusObj)
	selectedParentNameList = []
	i = 0
	parentNameList = corpusObj.keys()
	while i<selectedParentLen:
		parentIndex = random.randint(0, parentSize-1)
		seletecdParentName = parentNameList[parentIndex]
		if seletecdParentName not in selectedParentNameList:
			selectedParentNameList.append(seletecdParentName)
			i += 1

	print "selected Parent Name list"
	for i in range(selectedParentLen):
		print selectedParentNameList[i],

	for parentName in selectedParentNameList:
		generateFakeComments4Parent(parentName, corpusObj, betaObj, cmntLen)

def generateFakeComments4Parent(parentName, corpusObj, betaObj, cmntLen):
	fakeCommentName = "./"+parentName+"_100.json"
	f = open(fakeCommentName, 'w')
	content = ""
	childName = ""
	jsonFileFormat = {}
	title = ""

	parentObj = corpusObj[parentName]

	sortedTopicProportionList = sorted(parentObj.m_topicProportion, key=parentObj.m_topicProportion.__getitem__) 

	print "parentName\t", parentName
	for topicIndex in sortedTopicProportionList[0:3]:
		print topicIndex

		topWords = betaObj.m_topicWord[topicIndex]

		for i in range(cmntLen/3):
			wordIndex = random.randint(0, len(topWords)-1)
			# print wordIndex
			content += topWords[wordIndex]+" "

	jsonFileFormat.setdefault("content", content)
	jsonFileFormat.setdefault("child", childName)
	jsonFileFormat.setdefault("title", title)
	jsonFileFormat.setdefault("name", parentName+"_100")
	jsonFileFormat.setdefault("parent", parentName)

	json.dump(jsonFileFormat, f)
	f.close()

parentFile = "parentParameter.txt"
topWordFile = "topWords.txt"
corpusObj = {}
betaObj = _Beta()
selectedParentLen = 50
cmntLen = 100

loadParentFile(parentFile, corpusObj)
loadTopWordFile(topWordFile, betaObj)
randomGenerateFakeComments(corpusObj, betaObj, selectedParentLen, cmntLen)
