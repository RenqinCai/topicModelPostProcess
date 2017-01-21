class _ParentDoc:
	def __init__(self, a_ID):
		self.m_ID = a_ID
		self.m_spamCommentList = []
		self.m_normalCommentList = []
		self.m_commentList = []
		self.m_stnList = []
		self.m_stnMap = {}
		self.m_predictSpamList = []
		self.m_predictNormalList = []
		#ID:childObj
		self.m_childMap = {}
		#childID:sim
		self.m_simMap = {}

	def addStn2Parent(self, stnIndex, stnObj):
		self.m_stnMap.setdefault(stnIndex, stnObj)
		self.m_stnList.append(stnIndex)

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

class _Stn:
	def __init__(self, name):
		self.m_name = name
		self.m_parent = None
		self.m_groundTruthChildList = []
		self.m_childDocMap = {} ##modelIndex:childName:likelihood
		self.m_APMap = {} ###modelIndex:AP
		
	def getName(self):
		return self.m_name

	def addChild2Stn(self, childName, likelihood):
		if childName not in self.m_childDocMap.keys():
			self.m_childDocMap.setdefault(childName, likelihood)
		else:
			self.m_childDocMap[childName] = likelihood

	# def addChild2Stn(self, childName, likelihood, modelIndex):
	# 	if modelIndex not in self.m_childDocMap.keys():
	# 		self.m_childDocMap.setdefault(modelIndex, {})
	# 		self.m_childDocMap[modelIndex].setdefault(childName, likelihood)
	# 	else:
	# 		self.m_childDocMap[modelIndex].setdefault(childName, likelihood)

	def setParent2Stn(self, parentObj):
		self.m_parent = parentObj

	def addChild2Ground(self, childName):
		self.m_groundTruthChildList.append(childName)

class _ChildDoc:
	def __init__(self, name):
		self.m_name = name
		self.m_parent = None
		# self.m_stnMap = {} 
		self.m_APMap = {} ###modelIndex:AP
		self.m_groundTruthStnList=[]

	def getName(self):
		return self.m_name

	def addStn2Child(self, stnIndex, sim, modelIndex):
		if modelIndex not in self.m_stnMap.keys():
			self.m_stnMap.setdefault(modelIndex, {})
			self.m_stnMap[modelIndex].setdefault(stnIndex, sim)
		else:
			self.m_stnMap[modelIndex].setdefault(stnIndex, sim)

	def setParent2Child(self, parentObj):
		self.m_parent = parentObj

	def addStn2Ground(self, stnIndex):
		self.m_groundTruthStnList.append(stnIndex)

class _Corpus:
	def __init__(self):
		##parentName:parentObj
		self.m_parentMap = {}
		self.m_simMap={}
		self.m_spamMAP = {}
		self.m_spamNum = 0

	def addParent2Corpus(self, parentName, parentObj):
		self.m_parentMap.setdefault(parentName, parentObj)

