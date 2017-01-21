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

def readNormalFile(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split()

		parentID = line[0]
		childID = line[2]

		parentDocObj = None
		if parentID in corpusObj.keys():
			parentDocObj = corpusObj[parentID]
		else:
			parentDocObj = _ParentDoc(parentID)
			corpusObj.setdefault(parentID, parentDocObj)

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

	for rawLine in f:
		line = rawLine.strip().split()

		parentID = line[0]
		lineLen = len(line)

		parentDocObj = a_corpusObj[parentID]

		for index in range(1, lineLen):
			unitLine = line[index].split(":")
			childID = unitLine[0]
			childSim = float(unitLine[1])

			if childSim > a_threshold:
				parentDocObj.addPredictNormal(childID)
			else:
				parentDocObj.addPredictSpam(childID)

			parentDocObj.addComment(childID)

		commonNormalCommentSet= set(parentDocObj.m_commentList).intersection(parentDocObj.m_normalCommentList)
		parentDocObj.m_normalCommentList = list(commonNormalCommentSet)

		for commentID in parentDocObj.m_commentList:
			if commentID not in commonNormalCommentSet:
				parentDocObj.addSpam(commentID)

	f.close()

def recallOrPrecision(a_corpusObj):
	TP = 0
	FP = 0
	FN = 0
	TN = 0
	
	for parentID in a_corpusObj.keys():
		parentDocObj = a_corpusObj[parentID]

		# for predictSpamUnit in parentDocObj.m_predictSpamList:
		# 	if predictSpamUnit in parentDocObj.m_spamCommentList:
		# 		TP += 1
		# 	else:
		# 		FP += 1

		for predictSpamUnit in parentDocObj.m_predictSpamList:
			if predictSpamUnit in parentDocObj.m_spamCommentList:
				TN += 1
			else:
				FN += 1

		for predictNormalUnit in parentDocObj.m_predictNormalList:
			if predictNormalUnit in parentDocObj.m_normalCommentList:
				TP += 1
			else:
				FP += 1	

		# for predictNormalUnit in parentDocObj.m_predictNormalList:
		# 	if predictNormalUnit in parentDocObj.m_normalCommentList:
		# 		TN += 1
		# 	else:
		# 		FN += 1

	print TP, "\t", FP, "\t", FN, "\t", TN

	precision = TP*1.0/(TP+FP)
	recall = TP*1.0/(TP+FN)

	print "normal comments\t", (TP+FN)

	F1Score = 2*1.0/((1.0/precision)+(1/recall))

	print "precision\t", precision, "\t recall \t", recall, "\t F1Score\t", F1Score


spamCommentFile = ""

normalFile = "annotatedFile.txt"
simFile = "topChild4Parent_DCMCorrLDA_prior.txt"
# simFile = "topChild4Parent_LDA.txt"
# # simFile = "topChild4Parent_CorrLDA.txt"
# simFile = "topChild4Parent_SCTM_2.txt"
# simFile = "topChild4Parent_DCMDMMCorrLDA_3.txt"

corpusObj = {}
threshold = 0.8

print "threshold\t", threshold

readNormalFile(normalFile, corpusObj)
spamByThreshold(corpusObj, threshold, simFile)
recallOrPrecision(corpusObj)

