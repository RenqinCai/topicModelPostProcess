
import numpy as np
import matplotlib.pyplot as plt

class ParentDoc:
	def __init__(self):
		self.m_name = ""
		###modelIndex:[topicProportionList]
		self.m_topicProportion = {}
		###modelIndex:entropyVal
		self.m_entropyVal = {}

class Corpus:
	def __init__(self):
		self.m_docNum = 0
		self.m_docMap = {} ###docName:docObj

def loadEntropyFile(fileName, modelIndex, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		parentName = line[0]

		if parentName not in corpusObj.m_docMap.keys():
			parentObj = ParentDoc()
			corpusObj.m_docMap.setdefault(parentName, parentObj)
		else:
			parentObj = corpusObj.m_docMap[parentName]

		lineLen = len(line)

		if modelIndex not in parentObj.m_topicProportion.keys():
			parentObj.m_topicProportion.setdefault(modelIndex, [])

		entropyVal = 0

		alpha = 1e-20

		for i in range(2, 31):
			
			lineUnit = float(line[i])

			lineUnit = (alpha+lineUnit)/(1+30*alpha*1.0)

			parentObj.m_topicProportion[modelIndex].append(lineUnit)


			entropyVal += lineUnit*np.log(lineUnit)

		entropyVal = -entropyVal
		parentObj.m_entropyVal.setdefault(modelIndex, entropyVal)

def plotEntropyVal(corpusObj, modelIndex1, modelIndex2, modelIndex3, modelIndex4, modelIndex5, modelIndex6):
	docIndexList = []
	docEntropyValList1 = []
	docEntropyValList2 = []
	docEntropyValList3 = []
	docEntropyValList4 = []
	docEntropyValList5 = []
	docEntropyValList6 = []

	i = 0
	for parentName in corpusObj.m_docMap.keys():
		docIndexList.append(i)
		i += 1
		print parentName
		parentObj = corpusObj.m_docMap[parentName]
		entropyVal = parentObj.m_entropyVal[modelIndex1]
		docEntropyValList1.append(entropyVal)

		entropyVal = parentObj.m_entropyVal[modelIndex2]
		docEntropyValList2.append(entropyVal)

		entropyVal = parentObj.m_entropyVal[modelIndex3]
		docEntropyValList3.append(entropyVal)

		entropyVal = parentObj.m_entropyVal[modelIndex4]
		docEntropyValList4.append(entropyVal)

		entropyVal = parentObj.m_entropyVal[modelIndex5]
		docEntropyValList5.append(entropyVal)

		entropyVal = parentObj.m_entropyVal[modelIndex6]
		docEntropyValList6.append(entropyVal)

	handle1, = plt.plot(docIndexList, docEntropyValList1, "g-", label=str(modelIndex1)+ "\tcomments")
	handle2, = plt.plot(docIndexList, docEntropyValList2, "r-", label=str(modelIndex2)+ "\tcomments")
	handle3, = plt.plot(docIndexList, docEntropyValList3, "y-", label=str(modelIndex3)+ "\tcomments")
	handle4, = plt.plot(docIndexList, docEntropyValList4, "b-", label=str(modelIndex4)+ "\tcomments")
	handle5, = plt.plot(docIndexList, docEntropyValList5, "m-", label=str(modelIndex5)+ "\tcomments")
	handle6, = plt.plot(docIndexList, docEntropyValList6, "#03ED3A", label=str(modelIndex6)+ "\tcomments")

	handles = []
	handles.append(handle1)
	handles.append(handle2)
	handles.append(handle3)
	handles.append(handle4)
	handles.append(handle5)
	handles.append(handle6)

	plt.xlabel("parent document index")
	plt.ylabel("entropy")
	plt.title("ACCTM_C-entropy w.r.t the size of child documents")
	plt.legend(handles=handles)
	plt.show()

	
corpusObj = Corpus()

for num in range(0, 30):
	file = "./ACCTM_C_dynamic/testParentParameter_"+str(num)+".txt"
	loadEntropyFile(file, num, corpusObj)

plotEntropyVal(corpusObj, 0, 1, 3, 15, 25, 29)


