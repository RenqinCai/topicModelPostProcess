import matplotlib.pyplot as plt
import numpy as np

class _ParentDoc:
	def __init__(self, a_ID):
		self.m_ID = a_ID
		self.m_spamCommentList = []
		self.m_normalCommentList = []
		self.m_predictSpamList = []
		self.m_predictNormalList = []
		self.m_commentList = []

	def addSpam(self, commentID):
		self.m_spamCommentList.append(commentID)

	def addNormal(self, commentID):
		self.m_normalCommentList.append(commentID)

	def addPredictSpam(self, commentID):
		self.m_predictSpamList.append(commentID)

	def addPredictNormal(self, commentID):
		self.m_predictNormalList.append(commentID)

	def addComment(self, commentID):
		self.m_commentList.append(commentID)

class _corpus:
	def __init__(self):
		self.m_parentMap = {}
		self.m_simMAP={}
		self.m_spamMAP = {}
		self.m_spamNum = 0

def readNormalFile(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split()

		parentID = line[0]
		childID = line[2]

		parentDocObj = None
		if parentID in corpusObj.m_parentMap.keys():
			parentDocObj = corpusObj.m_parentMap[parentID]
		else:
			parentDocObj = _ParentDoc(parentID)
			corpusObj.m_parentMap.setdefault(parentID, parentDocObj)

		parentDocObj.addNormal(childID)

	f.close()

# def readSpamNormalCommentFile(fileName, corpusObj):
# 	f = open(fileName)

# 	while True:
# 		line1 = f.readline()
# 		line2 = f.readline()
# 		line3 = f.readline()

# 		parentID = line1.strip()
# 		parentDocObj = _ParentDoc(parentID)
# 		spamCommentList = line2.strip().split()
# 		normalCommentList = line3.strip().split()

# 		corpusObj.setdefault(parentID, parentDocObj)

# 		parentDocObj.m_spamCommentList = spamCommentList
# 		parentDocObj.m_normalCommentList = normalCommentList


# 	print "corpus parentDoc size", len(corpusObj)
# 	f.close()


def spamByThreshold(a_corpusObj, a_threshold, a_fileName):
	f = open(a_fileName)
	totalComment = 0;

	for rawLine in f:
		line = rawLine.strip().split()

		parentID = line[0]
		lineLen = len(line)

		parentDocObj = a_corpusObj.m_parentMap[parentID]

		for index in range(1, lineLen):
			unitLine = line[index].split(":")
			childID = unitLine[0]
			childSim = float(unitLine[1])

			a_corpusObj.m_simMAP.setdefault(childID, childSim)

			if childSim > a_threshold:
				parentDocObj.addPredictNormal(childID)
			else:
				parentDocObj.addPredictSpam(childID)

			parentDocObj.addComment(childID)

		commonNormalCommentSet= set(parentDocObj.m_commentList).intersection(parentDocObj.m_normalCommentList)
		parentDocObj.m_normalCommentList = list(commonNormalCommentSet)

		for commentID in parentDocObj.m_commentList:
			totalComment += 1
			if commentID not in commonNormalCommentSet:
				parentDocObj.addSpam(commentID)
				corpusObj.m_spamMAP.setdefault(commentID, 1) ###1 for spam, 0 for normal
				corpusObj.m_spamNum += 1
			else:
				corpusObj.m_spamMAP.setdefault(commentID, 0)

	print "totalSpam \t", corpusObj.m_spamNum
	print "total comment\t", totalComment
	f.close()

def recallOrPrecision(a_corpusObj):
	TP = 0
	FP = 0
	FN = 0
	TN = 0
	
	for parentID in a_corpusObj.m_parentMap.keys():
		parentDocObj = a_corpusObj.m_parentMap[parentID]

		for predictSpamUnit in parentDocObj.m_predictSpamList:
			if predictSpamUnit in parentDocObj.m_spamCommentList:
				TP += 1
			else:
				FP += 1

		for predictNormalUnit in parentDocObj.m_predictNormalList:
			if predictNormalUnit in parentDocObj.m_normalCommentList:
				TN += 1
			else:
				FN += 1

	print TP, "\t", FP, "\t", FN, "\t", TN

	precision = TP*1.0/(TP+FP)
	recall = TP*1.0/(TP+FN)

	F1Score = 2*1.0/((1.0/precision)+(1/recall))

	print "precision\t", precision, "\t recall \t", recall, "\t F1Score\t", F1Score

# def precisionRecall(a_corpusObj):
# 	sortedChildList = sorted(a_corpusObj.m_simMAP, key=a_corpusObj.m_simMAP.__getitem__, reverse=True)

# 	recallList = []
# 	precisionList = []

# 	TP = 0
# 	childLen = len(sortedChildList)
# 	spamLen = a_corpusObj.m_spamNum
# 	normalLen = childLen-spamLen
# 	predictNormalLen = 0
# 	for childID in sortedChildList:
# 		predictNormalLen += 1
# 		childSpam = a_corpusObj.m_spamMAP[childID]

# 		if childSpam == 0:
# 			TP += 1
# 		recallUnit = TP*1.0/normalLen
# 		recallList.append(recallUnit)
# 		# print "recallUnit\t", recallUnit

# 		precisionUnit = TP*1.0/predictNormalLen
# 		precisionList.append(precisionUnit)

# 	if predictNormalLen != childLen:
# 		print "error"
# 	else:
# 		return recallList, precisionList

# 		plotCurve(recallList, precisionList)

def precisionRecall(a_corpusObj):
	sortedChildList = sorted(a_corpusObj.m_simMAP, key=a_corpusObj.m_simMAP.__getitem__)

	recallList = []
	precisionList = []

	TP = 0
	childLen = len(sortedChildList)
	spamLen = a_corpusObj.m_spamNum
	predictSpamLen = 0
	# normalLen = childLen-spamLen
	# predictNormalLen = 0
	for childID in sortedChildList:
		predictSpamLen += 1
		childSpam = a_corpusObj.m_spamMAP[childID]

		if childSpam == 1:
			TP += 1
		recallUnit = TP*1.0/spamLen
		recallList.append(recallUnit)
		# print "recallUnit\t", recallUnit

		precisionUnit = TP*1.0/predictSpamLen
		precisionList.append(precisionUnit)

	if predictSpamLen != childLen:
		print "error"
	else:
		return recallList, precisionList

def plotCurve(recallList, precisionList):
	plt.plot(recallList, precisionList, label="topic model")
	plt.title("spam detection")
	plt.xlabel("recall")
	plt.ylabel("precision")
	plt.show()

def plotAllModelCurve(allModelRecallList, allModelPrecisionList, modelNameList, sampleNum):
	modelNum = len(allModelRecallList)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	markerList = ["s", "*", "d", "o", "p", "x"]
	linestyleList = ["+", "o", "x", "-", "-."]
	colorList = ['b', 'r', 'g', 'm', "#FFD700", "#b22222"]


	recallList = allModelRecallList[0]
	totalNum = len(recallList)
	sampleIndexList = list(np.arange(0, totalNum, 1))
	sampleIndexList = [1, 40, 200, 500, 1000, 1300, 1800, 2000, 2300, 2600, 2896]

	print "sampleLen\t", len(sampleIndexList), "totalNum\t", totalNum

	for modelIndex in range(modelNum):
		recallList = allModelRecallList[modelIndex]
		precisionList = allModelPrecisionList[modelIndex]

		sampleRecallList = []
		samplePrecisionList = []

		# sampleIndexList = sorted(list(np.random.randint(0, len(recallList), sampleNum)))

		# sampleRecallList.append(recallList[0])
		# samplePrecisionList.append(precisionList[0])

		for sampleIndex in sampleIndexList:
			sampleRecallList.append(recallList[sampleIndex])
			samplePrecisionList.append(precisionList[sampleIndex])

		modelName = modelNameList[modelIndex]
		plt.plot(sampleRecallList, samplePrecisionList, linewidth=0.5, label=modelName, color=colorList[modelIndex], marker=markerList[modelIndex])

		# plt.plot(sampleRecallList, samplePrecisionList, linewidth=1, label=modelName, color=colorList[modelIndex], linestyle=linestyleList[modelIndex])
	major_ticks = np.arange(0.5, 1.1, 0.1)
	ax.set_yticks(major_ticks)
	plt.ylim([0.48, 1.02])
	plt.tick_params(axis='x', labelsize=12)
	plt.tick_params(axis='y', labelsize=12)	
	plt.title("Spam Comments Detection", fontsize=12)
	plt.xlabel("recall", fontsize=12)
	plt.ylabel("precision", fontsize=12)
	plt.legend(prop={'size':12})
	# fig.set_size_inches([4, 3.3])
	# fig.savefig("normalDetection.png", format="png", dpi=400)
	plt.show()


spamCommentFile = ""
threshold = 0.1
# print "threshold\t", threshold
normalFile = "annotatedFile.txt"

allModelRecallList = []
allModelPrecisionList = []
modelNameList = []

corpusObj = _corpus()
LDA_simFile = "topChild4Parent_LDA.txt"
readNormalFile(normalFile, corpusObj)
spamByThreshold(corpusObj, threshold, LDA_simFile)
recallList, precisionList = precisionRecall(corpusObj)
allModelRecallList.append(recallList)
allModelPrecisionList.append(precisionList)
modelNameList.append("LDA")

corpusObj = _corpus()
CorrLDA_simFile = "topChild4Parent_CorrLDA.txt"
readNormalFile(normalFile, corpusObj)
spamByThreshold(corpusObj, threshold, CorrLDA_simFile)
recallList, precisionList = precisionRecall(corpusObj)
allModelRecallList.append(recallList)
allModelPrecisionList.append(precisionList)
modelNameList.append("Corr-LDA")

corpusObj = _corpus()
PriorCorrLDA_simFile = "topChild4Parent_priorCorrLDA_2.txt"
readNormalFile(normalFile, corpusObj)
spamByThreshold(corpusObj, threshold, PriorCorrLDA_simFile)
recallList, precisionList = precisionRecall(corpusObj)
allModelRecallList.append(recallList)
allModelPrecisionList.append(precisionList)
modelNameList.append("PriorCorrLDA")

corpusObj = _corpus()
SCTM_simFile = "topChild4Parent_SCTM_2.txt"
readNormalFile(normalFile, corpusObj)
spamByThreshold(corpusObj, threshold, SCTM_simFile)
recallList, precisionList = precisionRecall(corpusObj)
allModelRecallList.append(recallList)
allModelPrecisionList.append(precisionList)
modelNameList.append("SCTM")


# recallOrPrecision(corpusObj)

# corpusObj = _corpus()
# DCMCorrLDA_simFile = "topChild4Parent_DCMCorrLDA.txt"
# readNormalFile(normalFile, corpusObj)
# spamByThreshold(corpusObj, threshold, DCMCorrLDA_simFile)
# recallList, precisionList = precisionRecall(corpusObj)
# allModelRecallList.append(recallList)
# allModelPrecisionList.append(precisionList)
# modelNameList.append("DCMCorrLDA")

corpusObj = _corpus()
CorrDCMLDA_simFile = "topChild4Parent_CorrDCMLDA.txt"
readNormalFile(normalFile, corpusObj)
spamByThreshold(corpusObj, threshold, CorrDCMLDA_simFile)
recallList, precisionList = precisionRecall(corpusObj)
allModelRecallList.append(recallList)
allModelPrecisionList.append(precisionList)
modelNameList.append("CorrDCMLDA")

corpusObj = _corpus()
DCMDMMCorrLDA_simFile = "topChild4Parent_CCTM_2.txt"

# DCMDMMCorrLDA_simFile = "topChild4Parent_DCMDMMCorrLDA_2.txt"
readNormalFile(normalFile, corpusObj)
spamByThreshold(corpusObj, threshold, DCMDMMCorrLDA_simFile)
recallList, precisionList = precisionRecall(corpusObj)
allModelRecallList.append(recallList)
allModelPrecisionList.append(precisionList)
modelNameList.append("CCTM")


sampleNum = 30
plotAllModelCurve(allModelRecallList, allModelPrecisionList, modelNameList, sampleNum)
 


