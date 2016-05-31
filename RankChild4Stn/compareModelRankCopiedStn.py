from structure import _Corpus
from structure import _ParentDoc
from structure import _ChildDoc
from structure import _Stn
import os

def loadCopiedStn(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split(":")
		childName = line[0]
		stnName = line[1]

		parentName = line[0].split("_")[0]

		parentObj = corpusObj.m_parentMap[parentName]

		parentObj.m_copiedStn4ChildList.append(childName)

	f.close()


def loadModel(fileName, corpusObj, modelIndex):
	print "modelIndex\t", modelIndex
	f = open(fileName)

	parentObj = None

	childIndex = 0
	for rawLine in f:
		line = rawLine.strip().split("\t")

		if childIndex == 0:
			parentName = line[0]
			childNum = float(line[1])

			parentObj = _ParentDoc(parentName)
			corpusObj.m_parentMap.setdefault(parentName, parentObj)
			childIndex += 1 
			if childNum < childIndex:
				childIndex = 0
		else:
			# stnName = str(int(line[0])+1)
			childName = line[0]
			childObj = _ChildDoc(childName)
			childObj.setParent2Child(parentObj)

			parentObj.addChild2Parent(childName, childObj)

			lineLen = len(line)
			for i in range(1, lineLen):
				stn = line[i].split(":")			
				stnName = stn[0]
				stnSim = stn[1]
				# print debug

				stnObj = _Stn(stnName)
				stnObj.setParent2Stn(parentObj)

				parentObj.addStn2Parent(stnName, stnObj)
				childObj.addStn2Child(stnName, stnSim, modelIndex)

			childIndex += 1
			if childNum < childIndex:
				childIndex = 0

	f.close() 

def addModel(fileName, corpusObj, modelIndex):
	
	f = open(fileName)

	parentObj = None

	likelihoodList = []

	childIndex = 0
	for rawLine in f:
		line = rawLine.strip().split("\t")

		if childIndex == 0:
			parentName = line[0]
			childNum = float(line[1])

			if parentName not in corpusObj.m_parentMap.keys():
				parentObj = _ParentDoc(parentName)
				corpusObj.m_parentMap.setdefault(parentName, parentObj)
				print "previous model no parentName"
			else:
				parentObj = corpusObj.m_parentMap[parentName]
			childIndex += 1 
			if childNum < childIndex:
				childIndex = 0
		else:
			# stnName = str(int(line[0])+1)
			childName = line[0]
			# childObj = _ChildDoc(childName)
			# childObj.setParent2Child(parentObj)
			childObj = None

			if not parentObj.existChildInParent(childName):
				childObj = _ChildDoc(childName)
				childObj.setParent2Child(parentObj)

				parentObj.addChild2Parent(childName, childObj)
			else:
				childObj = parentObj.m_childDocMap[childName]

			lineLen = len(line)
			for i in range(1, lineLen):
				stn = line[i].split(":")
				stnName = stn[0]
				stnSim = float(stn[1])

				if not parentObj.existStnInParent(stnName):
					print "missing parent"
					stnObj = _Stn(stnName)
					stnObj.setParent2Stn(parentObj)
					parentObj.addStn2Parent(stnName, stnObj)
					childObj.addStn2Child(stnName, stnSim)
				else:
				
					stnObj = parentObj.m_stnMap[stnName]
					childObj.addStn2Child(stnName, stnSim, modelIndex)

			childIndex += 1
			if childNum < childIndex:
				childIndex = 0

	f.close()

def loadGroundTruth(dir, corpusObj):
	totalCorrspondenceStnNumGroundTruth = 0

	for fileName in os.listdir(dir):
		if fileName.endswith(".txt"):
			totalCorrspondenceStnNumGroundTruth += readGroundTruthFile(corpusObj, dir, fileName)

	print "totalCorrspondenceStnNumGroundTruth\t", totalCorrspondenceStnNumGroundTruth

##fill childObj with stnObj and stnObj with childObj
def readGroundTruthFile(corpusObj, dir,fileName):

	totalGroundStnNum = 0
	groundStnSet = set()

	parentName = fileName.replace("Comments", "").replace(".txt", "")

	parentObj = None
	if parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]
	else:
		print "missing parent"

	absoluteFileName = os.path.join(dir, fileName)
	f = open(absoluteFileName, "r")

	lineNum = 1

	for rawLine in f:
		childName = parentName+"_"+str(lineNum)
		lineNum += 1
		#print rawLine
####if the first string not {}, ignore this child doc
		if rawLine[0] is not "{" :
			continue

###use } to split stn
		line = rawLine.strip().split("}")

		sentenceNumList = line[0].strip("{").strip().split(",")

###no corresponding stns, ignore this child
		if len(sentenceNumList) is 0:
			continue

		if childName not in parentObj.m_childDocMap.keys():
			continue

		childObj = parentObj.m_childDocMap[childName]
		for i in range(len(sentenceNumList)):
			##if not number
			if not sentenceNumList[i]:
				continue

			sentenceID = (sentenceNumList[i].strip())
			groundStnSet.add(sentenceID)

			if sentenceID in parentObj.m_stnMap.keys():
				stnObj = parentObj.m_stnMap[sentenceID]
				stnObj.addChild2Ground(childName)
				childObj.addStn2Ground(sentenceID)
	f.close()

	return len(groundStnSet)

def computeMAP(corpusObj, modelIndex):
	print "modelIndex\t", modelIndex
	totalAP = 0
	totalChildNum = 0
	totalCorrespondingChildNum = 0

	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]

		copiedStn4ChildList = parentObj.m_copiedStn4ChildList

		for childName in parentObj.m_childDocMap.keys():
			childObj = parentObj.m_childDocMap[childName]

			totalChildNum += 1
			if not len(childObj.m_groundTruthStnList):
				continue

			if childName not in copiedStn4ChildList:
				continue
			# commentStnset = set(m_copiedStn4ChildList).intersection(set(childObj.m_groundTruthStnList))
			# if not len(commentStnset):
			# 	continue

			AP = computeAP(childObj, modelIndex)
			
			if modelIndex not in childObj.m_APMap.keys():
				childObj.m_APMap.setdefault(modelIndex, AP)
			else:
				childObj.m_APMap[modelIndex] = AP

			totalAP += AP
			totalCorrespondingChildNum += 1

	MAP = totalAP*1.0/totalCorrespondingChildNum
	print "totalAP\t", totalAP, "totalCorrespondingChildNum\t", totalCorrespondingChildNum, "MAP\t", MAP
	print "totalChildNum\t", totalChildNum

def computeAP(childObj, modelIndex):
	groundTruthStnRankList = childObj.m_groundTruthStnList
 
 	# print childObj.m_childDocMap[modelIndex].keys()
	for stnName in childObj.m_stnMap[modelIndex].keys():
		stnSim = float(childObj.m_stnMap[modelIndex][stnName])
		childObj.m_stnMap[modelIndex][stnName] = stnSim

	modelStnRankList = sorted(childObj.m_stnMap[modelIndex], key=childObj.m_stnMap[modelIndex].__getitem__, reverse=True)

	AP = 0
	hit = 0
	precisionK = 0
	for i in range(len(modelStnRankList)):
		
		# if i > 9:
		# 	break
	# for i in range(10):
		stnName = modelStnRankList[i]
		if stnName in groundTruthStnRankList:
			# print "childName\t", childName

			hit += 1
			precisionK = hit*1.0/(i+1)
			AP += precisionK

	AP = AP/len(groundTruthStnRankList)

	# if not AP:
		# print "AP is 0"

		# print debug

	if AP == 1:
		print "childName\t", childObj.getName()
		print "modelStnRankList\t", modelStnRankList
		print "groundTruthStnRankList\t", groundTruthStnRankList


	return AP

def compareAP(corpusObj, modelIndex1, modelIndex2):
	model1LargeChild = {} ##name:AP1-AP2 difference
	model2LargeChild = {} ##name:AP2-AP1 difference

	for parentName in corpusObj.m_parentMap.keys():
		parentObj =  corpusObj.m_parentMap[parentName]

		copiedStn4ChildList = parentObj.m_copiedStn4ChildList

		for childName in parentObj.m_childDocMap.keys():
			childObj = parentObj.m_childDocMap[childName]

			if not len(childObj.m_groundTruthStnList):
				continue

			if childName not in copiedStn4ChildList:
				continue

			AP1 = childObj.m_APMap[modelIndex1]
			AP2 = childObj.m_APMap[modelIndex2]

			name = childObj.getName()

			if AP1 > AP2:
				AP = str(AP1)+">"+str(AP2)
				APDiff = AP1-AP2
				# print name, "AP1\t", AP1, ">", "AP2\t", AP2
				model1LargeChild.setdefault(name, APDiff)
			else:
				AP =  str(AP1)+"<"+str(AP2)
				APDiff = AP2-AP1
				# print name, "AP1\t", AP1, "<", "AP2\t", AP2
				model2LargeChild.setdefault(name, APDiff)

	model1LargestDiffList = sorted(model1LargeChild, key=model1LargeChild.__getitem__, reverse=True)
	model2LargestDiffList = sorted(model2LargeChild, key=model2LargeChild.__getitem__, reverse=True)

	print "AP1 > AP2"
	for i in range(len(model1LargestDiffList)):
		stnName = model1LargestDiffList[i]
		APDiff = model1LargeChild[stnName]
		print "stnName\t", stnName, "APDiff\t", APDiff

	print "AP2 > AP1"
	for i in range(len(model2LargestDiffList)):
		stnName = model2LargestDiffList[i]
		APDiff = model2LargeChild[stnName]

		print "stnName\t", stnName, "APDiff\t", APDiff

	# for name in model1LargeStn.keys():
	# 	print name, "\t", model1LargeStn[name]

	# for name in model2LargeStn.keys():
	# 	print name, "\t", model2LargeStn[name]
	
if __name__ == '__main__':
	groundTruthDir = "../rawArsTechnicaComments/"
	corpusObj = _Corpus()

	modelNum = 5

	BM25File = "./bm25_likelihood.txt"
	ldaFile = "./LDA_topStn4Child_est_childP_v2.txt"
	corrLDAFile = "./corrLDAtopStn4Child.txt"
	sctmFile = "./sctm_likelihood.txt"
	pcFile = "./ACCTM_topStn4Child_symmetric_v2.txt"
	pc2File = "./ACCTM_topStn4Child_est_childP_v2.txt"

	copiedStnFile = "./copiedStn.txt"

	# loadModel(sctmFile, corpusObj)
	# loadModel(pcFile, corpusObj, 4)
	# loadModel(BM25File, corpusObj, 0)
	loadModel(ldaFile, corpusObj, 1)
	# loadModel(corrLDAFile, corpusObj, 2)
	# loadModel(sctmFile, corpusObj, 3)
	# loadModel(pcFile, corpusObj, 4)

	loadGroundTruth(groundTruthDir, corpusObj)

	loadCopiedStn(copiedStnFile, corpusObj)
	# debugGroundTruthChild(corpusObj)
	# for i in range(modelNum):
	computeMAP(corpusObj, 1)

	# addModel(ldaFile, corpusObj, 1)
	# computeMAP(corpusObj, 1)

	# addModel(pcFile, corpusObj, 4)

	addModel(pc2File, corpusObj, 4)
	computeMAP(corpusObj, 4)

	compareAP(corpusObj, 1, 4)

