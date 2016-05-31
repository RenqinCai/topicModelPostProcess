from structure import _Corpus
from structure import _ParentDoc
from structure import _ChildDoc
from structure import _Stn
import os

def loadModel(fileName, corpusObj, modelIndex):
	print "modelIndex\t", modelIndex
	f = open(fileName)

	parentObj = None

	stnIndex = 0
	for rawLine in f:
		line = rawLine.strip().split("\t")

		if stnIndex == 0:
			parentName = line[0]
			stnNum = float(line[1])

			parentObj = _ParentDoc(parentName)
			corpusObj.m_parentMap.setdefault(parentName, parentObj)
			stnIndex += 1 
		else:
			# stnName = str(int(line[0])+1)
			stnName = line[0]
			stnObj = _Stn(stnName)
			stnObj.setParent2Stn(parentObj)

			parentObj.addStn2Parent(stnName, stnObj)

			lineLen = len(line)
			for i in range(1, lineLen):
				child = line[i].split(":")
				childName = child[0]
				childLikelihood = child[1]

				childObj = _ChildDoc(childName)
				childObj.setParent2Child(parentObj)

				parentObj.addChild2Parent(childName, childObj)
				stnObj.addChild2Stn(childName, childLikelihood, modelIndex)

			stnIndex += 1
			if stnNum < stnIndex:
				stnIndex = 0

	f.close() 

def addModel(fileName, corpusObj, modelIndex):
	
	f = open(fileName)

	parentObj = None

	likelihoodList = []

	stnIndex = 0
	for rawLine in f:
		line = rawLine.strip().split("\t")

		if stnIndex == 0:
			parentName = line[0]
			stnNum = float(line[1])

			if parentName not in corpusObj.m_parentMap.keys():
				parentObj = _ParentDoc(parentName)
				corpusObj.m_parentMap.setdefault(parentName, parentObj)
				print "previous model no parentName"
			else:
				parentObj = corpusObj.m_parentMap[parentName]
			stnIndex += 1 
		else:
			# stnName = str(int(line[0])+1)
			stnName = line[0]
			stnObj = None
			if not parentObj.existStnInParent(stnName):
				stnObj = _Stn(stnName)

				stnObj.setParent2Stn(parentObj)

				parentObj.addStn2Parent(stnName, stnObj)
			else:
				stnObj = parentObj.m_stnMap[stnName]


			lineLen = len(line)
			for i in range(1, lineLen):
				child = line[i].split(":")
				childName = child[0]
				childLikelihood = float(child[1])

				if not parentObj.existChildInParent(childName):
					print "missing parent"
					childObj = _ChildDoc(childName)
					childObj.setParent2Child(parentObj)
					parentObj.addChild2Parent(childName, childObj)
					stnObj.addChild2Stn(childName, childLikelihood)
				else:
				
					childObj = parentObj.m_childDocMap[childName]
					stnObj.addChild2Stn(childName, childLikelihood, modelIndex)

			stnIndex += 1
			if stnNum < stnIndex:
				stnIndex = 0


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
	totalStnNum = 0
	totalCorrespondingStnNum = 0

	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]

		for stnName in parentObj.m_stnMap.keys():
			stnObj = parentObj.m_stnMap[stnName]

			totalStnNum += 1
			if not len(stnObj.m_groundTruthChildList):
				continue

			AP = computeAP(stnObj, modelIndex)
			
			if modelIndex not in stnObj.m_APMap.keys():
				stnObj.m_APMap.setdefault(modelIndex, AP)
			else:
				stnObj.m_APMap[modelIndex] = AP

			totalAP += AP
			totalCorrespondingStnNum += 1

	MAP = totalAP*1.0/totalCorrespondingStnNum
	print "totalAP\t", totalAP, "totalCorrespondingStnNum\t", totalCorrespondingStnNum, "MAP\t", MAP
	print "totalStnNum\t", totalStnNum

def computeAP(stnObj, modelIndex):
	groundTruthChildRankList = stnObj.m_groundTruthChildList
 
 	# print stnObj.m_childDocMap[modelIndex].keys()
	for childName in stnObj.m_childDocMap[modelIndex].keys():
		childLikelihood = float(stnObj.m_childDocMap[modelIndex][childName])
		stnObj.m_childDocMap[modelIndex][childName] = childLikelihood

	modelChildRankList = sorted(stnObj.m_childDocMap[modelIndex], key=stnObj.m_childDocMap[modelIndex].__getitem__, reverse=True)

	print "stnName\t", stnObj.getName()
	print "modelChildRankList\t", modelChildRankList
	print "groundTruthChildRankList\t", groundTruthChildRankList

	AP = 0
	hit = 0
	precisionK = 0
	for i in range(len(modelChildRankList)):
		
		# if i > 9:
		# 	break
	# for i in range(10):
		childName = modelChildRankList[i]
		if childName in groundTruthChildRankList:
			# print "childName\t", childName

			hit += 1
			precisionK = hit*1.0/(i+1)
			AP += precisionK

	AP = AP/len(groundTruthChildRankList)

	# if not AP:
		# print "AP is 0"

		# print debug

	return AP

def compareAP(corpusObj, modelIndex1, modelIndex2):
	model1LargeStn = {} ##name:AP1-AP2 difference
	model2LargeStn = {} ##name:AP2-AP1 difference

	for parentName in corpusObj.m_parentMap.keys():
		parentObj =  corpusObj.m_parentMap[parentName]

		for stnName in parentObj.m_stnMap.keys():
			stnObj = parentObj.m_stnMap[stnName]

			if not len(stnObj.m_groundTruthChildList):
				continue

			AP1 = stnObj.m_APMap[modelIndex1]
			AP2 = stnObj.m_APMap[modelIndex2]

			name = parentName+"_"+stnObj.getName()

			if AP1 > AP2:
				AP = str(AP1)+">"+str(AP2)
				APDiff = AP1-AP2
				# print name, "AP1\t", AP1, ">", "AP2\t", AP2
				model1LargeStn.setdefault(name, APDiff)
			else:
				AP =  str(AP1)+"<"+str(AP2)
				APDiff = AP2-AP1
				# print name, "AP1\t", AP1, "<", "AP2\t", AP2
				model2LargeStn.setdefault(name, APDiff)

	model1LargestDiffList = sorted(model1LargeStn, key=model1LargeStn.__getitem__, reverse=True)
	model2LargestDiffList = sorted(model2LargeStn, key=model2LargeStn.__getitem__, reverse=True)

	print "AP1 > AP2"
	for i in range(len(model1LargestDiffList)):
		stnName = model1LargestDiffList[i]
		APDiff = model1LargeStn[stnName]
		print "stnName\t", stnName, "APDiff\t", APDiff

	print "AP2 > AP1"
	for i in range(len(model2LargestDiffList)):
		stnName = model2LargestDiffList[i]
		APDiff = model2LargeStn[stnName]

		print "stnName\t", stnName, "APDiff\t", APDiff

	# for name in model1LargeStn.keys():
	# 	print name, "\t", model1LargeStn[name]

	# for name in model2LargeStn.keys():
	# 	print name, "\t", model2LargeStn[name]
	

if __name__ == '__main__':
	groundTruthDir = "../rawArsTechnicaComments/"
	corpusObj = _Corpus()

	modelNum = 5

	BM25File = "./BM25_topChild4Stn_v1.txt"
	ldaFile = "./LDA_topChild4Stn_v2.txt"
	corrLDAFile = "./corrlda/topChild4Stn_v1.txt"
	sctmFile = "./sctm_topChild4Stn_v2.txt"
	pcFile = "./PCB_topChild4Stn_v6.txt"
	pcFile2 = "./PCBP_topChild4Stn_v3.txt"
	lmFile = "./languageModel_topChild4Stn_v1.txt";

	# loadModel(sctmFile, corpusObj)
	# loadModel(pcFile, corpusObj)
	# loadModel(BM25File, corpusObj, 0)
	loadModel(ldaFile, corpusObj, 1)
	# loadModel(corrLDAFile, corpusObj, 2)
	# loadModel(sctmFile, corpusObj, 3)
	# loadModel(pcFile, corpusObj, 4)

	loadGroundTruth(groundTruthDir, corpusObj)
	# debugGroundTruthChild(corpusObj)
	# for i in range(modelNum):
	computeMAP(corpusObj, 1)

	# addModel(corrLDAFile, corpusObj, 0)
	# computeMAP(corpusObj, 0)

	addModel(pcFile, corpusObj, 2)
	computeMAP(corpusObj, 2)

	addModel(pcFile2, corpusObj, 3)
	computeMAP(corpusObj, 3)

	# addModel(BM25File, corpusObj, 3)
	# computeMAP(corpusObj, 3)

	# addModel(sctmFile, corpusObj, 4)
	# computeMAP(corpusObj, 4)

	# addModel(lmFile, corpusObj, 5)
	# computeMAP(corpusObj, 5)

	compareAP(corpusObj, 2, 3)

