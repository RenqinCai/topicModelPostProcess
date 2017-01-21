from structure import _Corpus
from structure import _ParentDoc
from structure import _ChildDoc
from structure import _Stn
import os

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
		parentObj = _ParentDoc(parentName)
		corpusObj.m_parentMap.setdefault(parentName, parentObj)

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

		# if childName not in parentObj.m_childDocMap.keys():
		# 	continue

		childObj = None
		if childName not in parentObj.m_childDocMap.keys():
			childObj = _ChildDoc(childName)
			parentObj.m_childDocMap.setdefault(childName, childObj)
		else:
			childObj = parentObj.m_childDocMap[childName]
		
		for i in range(len(sentenceNumList)):
			##if not number
			if not sentenceNumList[i]:
				continue

			sentenceID = (sentenceNumList[i].strip())
			groundStnSet.add(sentenceID)

			stnObj = None
			if sentenceID in parentObj.m_stnMap.keys():
				stnObj = parentObj.m_stnMap[sentenceID]
			else:
				stnObj = _Stn(sentenceID)
				parentObj.m_stnMap.setdefault(sentenceID, stnObj)

			stnObj.addChild2Ground(childName)
			childObj.addStn2Ground(sentenceID)

	f.close()

	return len(groundStnSet)

def writeAnnotated2File(corpusObj, fileName):
	f = open(fileName, "w")

	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]

		for stnName in parentObj.m_stnMap.keys():
			stnObj = parentObj.m_stnMap[stnName]

			correspondingChildList = stnObj.m_groundTruthChildList
			for childName in correspondingChildList:
				f.write(parentName+"\t")
				f.write(stnName+"\t")
				f.write(childName+"\n")

	f.close()

if __name__ == '__main__':
	groundTruthDir = "../rawArsTechnicaComments/"
	corpusObj = _Corpus()

	annotatedFile = "./annotatedFile.txt"
	
	# loadModel(sctmFile, corpusObj)
	# loadModel(pcFile, corpusObj)
	# loadModel(BM25File, corpusObj, 0)
	# loadModel(ldaFile, corpusObj, 1)
	# loadModel(corrLDAFile, corpusObj, 2)
	# loadModel(sctmFile, corpusObj, 3)
	# loadModel(pcFile, corpusObj, 4)

	loadGroundTruth(groundTruthDir, corpusObj)
	
	writeAnnotated2File(corpusObj, annotatedFile)
	