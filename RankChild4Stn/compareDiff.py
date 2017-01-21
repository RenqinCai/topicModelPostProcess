from structure import _Corpus
from structure import _ParentDoc
from structure import _ChildDoc
from structure import _Stn
import os
import random

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
					stnObj.addChild2Stn(childName, childLikelihood, modelIndex)
				else:
				
					childObj = parentObj.m_childDocMap[childName]
					stnObj.addChild2Stn(childName, childLikelihood, modelIndex)

			stnIndex += 1
			if stnNum < stnIndex:
				stnIndex = 0

def outputDiff(corpusObj, modelIndex1, modelIndex2):
	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]

		for stnName in parentObj.m_stnMap.keys():
			stnObj = parentObj.m_stnMap[stnName]

			model1ChildList = stnObj.m_childDocMap[modelIndex1].keys()
			model2ChildList = stnObj.m_childDocMap[modelIndex2].keys()

			if len(model1ChildList) == len(model2ChildList):
				continue
			else:
				print "model1\t", model1ChildList
				print "model2\t", model2ChildList

annotatedFile = "./annotatedFile.txt"
corpusObj = _Corpus()

sctmFile = "./SCTM/topChild4Stn_SCTM.txt"
DCMCorrLDAFile = "./DCMCorrLDA/topChild4Stn_11.txt"

loadModel(sctmFile, corpusObj, 0)
addModel(DCMCorrLDAFile, corpusObj, 1)

outputDiff(corpusObj, 0, 1)