import numpy as np

class _Corpus:
	def __init__(self):
		### parentID:parentObj
		self.m_parentIDList = []
		self.m_parentMap = {}

		###childID:childObj
		self.m_childIDList = []
		self.m_childMap = {}

class _ParentDoc:
	def __init__(self):
		self.m_ID = ""
		self.m_childList = []
		self.m_topicProportion = []
		self.m_childSimMap = {}

class _ChildDoc:
	def __init__(self):
		self.m_ID = ""
		self.m_parent = ""
		self.m_topicProportion = []

def readSelectedArticlesComments(file1, file2, corpusObj):
	f1 = open(file1)

	for rawLine in f1:
		line = rawLine.strip().split("\t")

		parentName = line[0]

		corpusObj.m_parentIDList.append(parentName)
		if parentName not in corpusObj.m_parentMap.keys():
			parentObj = _ParentDoc()
			parentObj.m_ID = parentName

			corpusObj.m_parentMap.setdefault(parentName, parentObj)

	f1.close()

	f2 = open(file2)
	for rawLine in f2:
		line = rawLine.strip().split("\t")

		parentName = line[0]

		parentObj = corpusObj.m_parentMap[parentName]

		lineLen = len(line)
		for i in range(1, lineLen):
			commentName = line[i]
			corpusObj.m_childIDList.append(commentName)

			parentObj.m_childList.append(commentName)

			if commentName not in corpusObj.m_childMap.keys():
				childObj = _ChildDoc()
				childObj.m_ID = commentName
				childObj.m_parent = parentName
				corpusObj.m_childMap.setdefault(commentName, childObj)

	f2.close()

def readSCTMOutput(file1, file2, corpusObj):
	articleF = open(file1)

	while True:
		line1 = articleF.readline()

		if not line1:
			break

		line2 = articleF.readline()
		parentNameIndex = int(line1.strip().split("\t")[0])

		parentName = corpusObj.m_parentIDList[parentNameIndex-1]

		proportionLine = line2.strip().split(" ")
		proportionLineLen = len(proportionLine)

		parentObj = corpusObj.m_parentMap[parentName]

		for i in range(proportionLineLen):
			parentObj.m_topicProportion.append(proportionLine[i])

	articleF.close()

	commentF = open(file2)

	commentIndex = 0

	while True:
		line1 = commentF.readline()

		if not line1:
			break

		line = line1.strip().split(" ")
		print line
		parentNameIndex = line[0]
		commentNum = int(line[1])
		
		for i in range(commentNum):
			commentIndex += 1
			line2 = commentF.readline()
			proportionLine = line2.strip().split(" ")
			proportionLineLen = len(proportionLine)

			commentName = corpusObj.m_childIDList[commentIndex-1]
			commentObj = corpusObj.m_childMap[commentName]

			for i in range(proportionLineLen):
				commentObj.m_topicProportion.append(proportionLine[i])

		line3 = commentF.readline()

	commentF.close()

def calSim(corpusObj):
	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]
		parentTopicProportion = parentObj.m_topicProportion

		for commentName in parentObj.m_childList:
			commentObj = corpusObj.m_childMap[commentName]
			commentTopicProportion = commentObj.m_topicProportion

			sim = cosineSim(parentTopicProportion, commentTopicProportion)

			parentObj.m_childSimMap.setdefault(commentName, sim)

def outputSim(corpusObj, outputFile):
	f = open(outputFile, "w")

	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]
		f.write(parentName+"\t")
		for commentName in parentObj.m_childSimMap.keys():
			sim = parentObj.m_childSimMap[commentName]
			f.write(commentName+":"+str(sim)+"\t")

		f.write("\n")

	f.close()

def cosineSim(topic1, topic2):
	topicLen1 = len(topic1)	
	topicLen2 = len(topic2)

	topicLen = 0
	if topicLen1 > topicLen2:
		topicLen = topicLen2
	else:
		topicLen = topicLen1

	numerator = 0
	denominator1 = 0
	denominator2 = 0
	for i in range(topicLen):
		numerator += float(topic1[i])*float(topic2[i])

		denominator1 += float(topic1[i])*float(topic1[i])
		denominator2 += float(topic2[i])*float(topic2[i])

	denominator2 += float(topic2[topicLen2-1])*float(topic2[topicLen2-1])

	sim = numerator*1.0/(np.sqrt(denominator1)*np.sqrt(denominator2))
	
	return sim

selectedStnFile = "selected_Stn.txt"

selectedCommentFile = "selected_Comments.txt"

corpusObj = _Corpus()

outputFile = "topChild4Parent_SCTM_2.txt"

articleProportionFile = "z_distDoc.txt"

commentProportionFile = "y_dist.txt"

readSelectedArticlesComments(selectedStnFile, selectedCommentFile, corpusObj)

readSCTMOutput(articleProportionFile, commentProportionFile, corpusObj)

calSim(corpusObj)

outputSim(corpusObj, outputFile)
