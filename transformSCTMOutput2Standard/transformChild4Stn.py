import numpy as np
from structure import _Corpus
from structure import _ParentDoc
from structure import _ChildDoc
from structure import _Stn
import os

def readSelectedStns(selectedStnFile, corpusObj):
	selectedStnF = open(selectedStnFile)

	totalStnNum = 0
	for rawLine in selectedStnF:
		line = rawLine.strip().split("\t")

		parentID = line[0]
		stnNum = int(line[1])

		pDocObj = None
		if parentID not in corpusObj.m_parentMap.keys():
			pDocObj = _ParentDoc(parentID)
			corpusObj.m_parentMap.setdefault(parentID, pDocObj)
			corpusObj.m_parentList.append(parentID)
			print "new parentObj"
		else:
			pDocObj = corpusObj.m_parentMap[parentID]

		lineLen = len(line)

		for lineIndex in range(2, lineLen):
			stnIndex = line[lineIndex]

			stnObj = _Stn(stnIndex)
			pDocObj.m_stnList.append(stnObj)


	selectedStnF.close()

def readSelectedComments(commentFile, corpusObj):
	f = open(commentFile)

	for rawLine in f:
		line = rawLine.strip().split("\t")

		parentID = line[0]

		pDocObj = None
		if parentID not in corpusObj.m_parentMap.keys():
			pDocObj = _ParentDoc(parentID)
			corpusObj.m_parentMap.setdefault(parentID, pDocObj)
			print "new parentObj"
		else:
			pDocObj = corpusObj.m_parentMap[parentID]

		lineLen = len(line)
		for lineIndex in range(1, lineLen):
			childName = line[lineIndex]

			childObj = _ChildDoc(childName)
			pDocObj.m_childDocMap.setdefault(childName, childObj)
			pDocObj.m_childList.append(childName)

	f.close()

def readSCTMOutput(likelihoodFile, corpusObj):
	f = open(likelihoodFile)

	stnIndex = 0		
	pDocObj = None
	stnNum = 0
	for rawLine in f:

		line = rawLine.strip().split(" ")

		if stnIndex == 0:
			parentNameIndex = int(line[0])
			stnNum = int(line[1])

			parentName = corpusObj.m_parentList[parentNameIndex-1]
			# if parentName not in corpusObj.m_parentMap.keys():
			# 	pDocObj = _ParentDoc(parentName)
			# 	corpusObj.m_parentMap.setdefault(parentName, pDocObj)
			# 	print "new parentObj"
			# else:
			pDocObj = corpusObj.m_parentMap[parentName]

			stnIndex += 1 
		else:
			stnNameIndex = int(line[0])
			print "parentName\t",pDocObj.m_name
			print stnNameIndex
			stnObj = pDocObj.m_stnList[stnNameIndex-1]

			lineLen = len(line)
			for i in range(1, lineLen):
				childElement = line[i]
				childElementSplitted = childElement.split(":")
				childNameIndex = int(childElementSplitted[0])
				childLikelihood = float(childElementSplitted[1])

				childName = pDocObj.m_childList[childNameIndex-1]
				# childObj = parentObj.m_childDocMap[childName]
				if 0 not in stnObj.m_childDocMap.keys():
					stnObj.m_childDocMap.setdefault(0, {})
				
				stnObj.m_childDocMap[0].setdefault(childName, childLikelihood)

			stnIndex += 1
			if stnNum < stnIndex:
				stnIndex = 0
	f.close()

def outputSCTM2Standard(outputFile, corpusObj):
	f = open(outputFile, "w")

	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]

		f.write(parentName+"\t"+str(len(parentObj.m_stnList))+"\n")
		for stnObj in parentObj.m_stnList:
			f.write(stnObj.m_name+"\t")
			for childName in stnObj.m_childDocMap[0].keys():
				childLikelihood = stnObj.m_childDocMap[0][childName]
				f.write(childName+":"+str(childLikelihood)+"\t")

			f.write("\n")

	f.close()


selectedStnFile = "selected_Stn.txt"

selectedCommentFile = "selected_Comments.txt"

corpusObj = _Corpus()

inputFile = "childLikelihood_SCTM"
outputFile = "topChild4Stn_SCTM.txt"

readSelectedStns(selectedStnFile, corpusObj)
readSelectedComments(selectedCommentFile, corpusObj)


readSCTMOutput(inputFile, corpusObj)

outputSCTM2Standard(outputFile, corpusObj)
