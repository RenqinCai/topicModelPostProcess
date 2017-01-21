from structure import _Corpus
from structure import _ParentDoc
from structure import _ChildDoc
from structure import _Stn
import os
import matplotlib.pyplot as plt
import numpy as np

def loadBM25Val(fileName, corpusObj, modelIndex):
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
				simVal = child[1]

				childObj = _ChildDoc(childName)
				childObj.setParent2Child(parentObj)

				parentObj.addChild2Parent(childName, childObj)
				stnObj.addChild2Stn(childName, simVal, modelIndex)

			stnIndex += 1
			if stnNum < stnIndex:
				stnIndex = 0

	f.close() 

def loadAnnotatedData(fileName, corpusObj):
	f = open(fileName, "r")

	for rawLine in f:
		line = rawLine.strip().split("\t")

		parentName = line[0]
		stnName = line[1]
		childName = line[2]

		if parentName not in corpusObj.m_parentMap.keys():
			continue

		parentObj = corpusObj.m_parentMap[parentName]

		if childName not in parentObj.m_childDocMap.keys():
			continue
			
		childObj = parentObj.m_childDocMap[childName]

		if stnName not in parentObj.m_stnMap.keys():
			continue

		stnObj = parentObj.m_stnMap[stnName]
		stnObj.addChild2Ground(childName)
		childObj.addStn2Ground(stnName)

	f.close()

def statisticsBM25Distribution(corpusObj, modelIndex):
	print "modelIndex\t", modelIndex

	BM25ValList = []

	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]

		print "annotating\t",parentName,
		for stnName in parentObj.m_stnMap.keys():
			print stnName,
			stnObj = parentObj.m_stnMap[stnName]

			correspondingChildList = stnObj.m_groundTruthChildList
			for childName in correspondingChildList:
				simVal = float(stnObj.m_childDocMap[modelIndex][childName])

				BM25ValList.append(simVal)

		print "\n"
		
	print "max\t", max(BM25ValList)
	print "min\t", min(BM25ValList)

	sortedBM25ValList = sorted(BM25ValList)

	stnNum = len(sortedBM25ValList)
	BM25Threshold = sortedBM25ValList[int(stnNum*0.3)]
	print "20 percent thresholdVal\t", BM25Threshold

	return BM25ValList

def separateQueryByBM25(corpusObj, thresholdVal, modelIndex, newAnnotatedFile):
	f = open(newAnnotatedFile, "w")

	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]

		stnFlag = True
		for stnName in parentObj.m_stnMap.keys():
			stnObj = parentObj.m_stnMap[stnName]

			correspondingChildList = stnObj.m_groundTruthChildList
			for childName in correspondingChildList:
				simVal = float(stnObj.m_childDocMap[modelIndex][childName])

				if simVal > thresholdVal:
					stnFlag = False

			if stnFlag == False:
				continue
			for childName in correspondingChildList:	
				f.write(parentName+"\t")
				f.write(stnName+"\t")
				f.write(childName+"\n")
				simVal = float(stnObj.m_childDocMap[modelIndex][childName])
				print "parentName\t", parentName, "\tstnName\t", stnName, "\tchildName\t", childName, "\t",simVal
	f.close()


def loadCopiedStnFile(copiedStnFile):
	f = open(copiedStnFile)

	copiedStnMap = {}
	copiedStnBM25ValList = []

	for rawLine in f:
		line = rawLine.strip().split("_")
		parentName = line[0]
		parentObj = corpusObj.m_parentMap[parentName]

		stnName = line[1].split(":")[1]
		childName = line[1].split(":")[0]
		childName = parentName+"_"+childName
		stnObj = parentObj.m_stnMap[stnName]

		simVal = float(stnObj.m_childDocMap[modelIndex][childName])
		copiedStnBM25ValList.append(simVal)
		if parentName in copiedStnMap.keys():
			copiedStnMap[parentName].append(stnName)
		else:
			copiedStnMap.setdefault(parentName, [])
			copiedStnMap[parentName].append(stnName)

	print "avg copied stn BM25 val\t", np.average(copiedStnBM25ValList)
	print "minimum copied stn BM25 val\t", np.amin(copiedStnBM25ValList)
	print "maximum copied stn BM25 val\t", np.amax(copiedStnBM25ValList)

	f.close()

	return copiedStnMap, copiedStnBM25ValList

def separateQueryByCopiedStn(corpusObj, copiedStnMap, modelIndex, newAnnotatedFile):
	f = open(newAnnotatedFile, "w")

	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]

		stnFlag = True

		copiedStnList4Parent = []
		if parentName in copiedStnMap.keys():
			copiedStnList4Parent = copiedStnMap[parentName]

		for stnName in parentObj.m_stnMap.keys():
			stnObj = parentObj.m_stnMap[stnName]

			if stnName in copiedStnList4Parent:
				continue

			correspondingChildList = stnObj.m_groundTruthChildList
			for childName in correspondingChildList:	
				f.write(parentName+"\t")
				f.write(stnName+"\t")
				f.write(childName+"\n")
	f.close()

def averageBM25Val4CopiedStn(corpusObj, copiedStnFile, modelIndex):
	f = open(copiedStnFile)

	copiedStnBM25ValList = []

	for rawLine in f:
		line = rawLine.strip().split("_")
		parentName = line[0]
		parentObj = corpusObj.m_parentMap[parentName]

		stnName = line[1].split(":")[1]
		childName = line[1].split(":")[0]
		childName = parentName+"_"+childName
		stnObj = parentObj.m_stnMap[stnName]

		simVal = float(stnObj.m_childDocMap[modelIndex][childName])
		copiedStnBM25ValList.append(simVal)

	f.close()

	print "avg copied stn BM25 val\t", np.average(copiedStnBM25ValList)
	print "minimum copied stn BM25 val\t", np.amin(copiedStnBM25ValList)
	print "maximum copied stn BM25 val\t", np.amax(copiedStnBM25ValList)

	return copiedStnBM25ValList

def plotHistogram(BM25ValList):
	maxVal = max(BM25ValList)
	minVal = min(BM25ValList)
	# bins = 20
	counts, bin_edges = np.histogram(BM25ValList, bins=20, normed=True)
	dx = bin_edges[1]-bin_edges[0]
	cdf = np.cumsum(counts)*dx
	print "cdf"
	print cdf
	print "edges"
	print bin_edges[1:]
	plt.plot(bin_edges[1:], cdf)
	plt.title("BM25")
	plt.show()
	
if __name__ == '__main__':
	corpusObj = _Corpus()

	modelIndex = 1
	modelNum = 5

	thresholdVal = 0.0776205455089
	# thresholdVal = 0

	BM25File = "./BM25_topChild4Stn_v2.txt"
	annotatedFile = "./annotatedFile.txt"
	newAnnotatedFile = "./topicalQueryFile_%d.txt"%(thresholdVal*100)
	copiedStnFile = "./copiedStn.txt"

	loadBM25Val(BM25File, corpusObj, modelIndex)
	
	loadAnnotatedData(annotatedFile, corpusObj)

	# (copiedStnMap, copiedStnBM25ValList) = loadCopiedStnFile(copiedStnFile)

	BM25ValList=statisticsBM25Distribution(corpusObj, modelIndex)

	# separateQueryByCopiedStn(corpusObj, copiedStnMap, modelIndex, newAnnotatedFile);
	# copiedStnBM25ValList = averageBM25Val4CopiedStn(corpusObj, copiedStnFile, modelIndex)
	separateQueryByBM25(corpusObj, thresholdVal, 1, newAnnotatedFile)
	# plotHistogram(copiedStnBM25ValList)