import matplotlib.pyplot as plt

from structure import _Corpus
from structure import _ParentDoc
from structure import _ChildDoc
from structure import _Stn

import os
import numpy as np

def readCommentSimFile(commentSimFile, corpusObj, t_threshold):
	f = open(commentSimFile)

	for rawLine in f:
		line = rawLine.strip().split("\t")

		parentID = line[0]

		lineLen = len(line)

		parentObj = _ParentDoc(parentID)

		corpusObj.m_parentMap.setdefault(parentID, parentObj)

		for lineIndex in range(1, lineLen):
			unitLine = line[lineIndex].split(":")
			childID = unitLine[0]
			childSim = float(unitLine[1])

			parentObj.m_simMap.setdefault(childID, childSim)

			corpusObj.m_simMap.setdefault(childID, childSim)
			# parentObj.addPredictNormal(childID)

			if childSim > t_threshold:
				parentObj.addPredictNormal(childID)
			else:
				parentObj.addPredictSpam(childID)

			parentObj.addComment(childID)

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

		if childName not in parentObj.m_childMap.keys():
			continue
			
		childObj = parentObj.m_childMap[childName]

		if stnName not in parentObj.m_stnMap.keys():
			# print "stnName\t", stnName
			continue

		stnObj = parentObj.m_stnMap[stnName]
		if childName in parentObj.m_commentList:
			stnObj.addChild2Ground(childName)

	f.close()

def readCommentLikelihoodFile(commentLikelihoodFile, corpusObj):
	f = open(commentLikelihoodFile)

	parentObj = None

	stnIndex = 0
	for rawLine in f:
		line = rawLine.strip().split("\t")

		if stnIndex == 0:
			parentName = line[0]
			stnNum = float(line[1])

			parentObj = corpusObj.m_parentMap[parentName]

			stnIndex += 1
		else:
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

				parentObj.m_childMap.setdefault(childName, childObj)
				stnObj.addChild2Stn(childName, childLikelihood)

			stnIndex += 1

			if stnNum < stnIndex:
				stnIndex = 0

	f.close()

def rankNormalComment4Stn(corpusObj, proportionOfNormal):
	totalStnNum = 0
	totalAP = 0
	totalCorrespondingStnNum = 0

	orderedCommentListBySim4Corpus = sorted(corpusObj.m_simMap, key=corpusObj.m_simMap.__getitem__, reverse=True)
	normalCommentList4Corpus = []

	for i in range(int(len(orderedCommentListBySim4Corpus)*proportionOfNormal)):
		commentName = orderedCommentListBySim4Corpus[i]
		normalCommentList4Corpus.append(commentName)

	for parentID in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentID]

		# orderedCommentListBySim = sorted(parentObj.m_simMap, key=parentObj.m_simMap.__getitem__, reverse=True)

		print "parentName:", parentID, "\t",

		rankCommentList = []
		for comment in parentObj.m_commentList:
			if comment in normalCommentList4Corpus:
				rankCommentList.append(comment)

		# rankCommentList = []
		# rankCommentLen = int(proportionOfNormal*len(orderedCommentListBySim))
		# print rankCommentLen
		# for i in range(rankCommentLen):
		# 	commentName = orderedCommentListBySim[i]
		# 	rankCommentList.append(commentName)

		for stnIndex in parentObj.m_stnList:
			stnObj = parentObj.m_stnMap[stnIndex]

			# print stnIndex
			totalStnNum += 1

			if not len(stnObj.m_groundTruthChildList):
				continue

			AP = computeAP(stnObj, rankCommentList)

			print "stnIndex\t", stnIndex, "\t", AP, "\t"

			totalAP += AP
			totalCorrespondingStnNum += 1

	MAP = totalAP*1.0/totalCorrespondingStnNum
	print "totalAP\t", totalAP, "totalCorrespondingStnNum\t", totalCorrespondingStnNum, "MAP\t", MAP
	print "totalStnNum\t", totalStnNum

def computeAP(stnObj, normalCommentList):
	# print "stn\t",stnObj.m_name
	groundTruthChildRankList = stnObj.m_groundTruthChildList
 	
 	childLikelihood4StnMAP = {}
	for childName in stnObj.m_childDocMap.keys():
		if childName not in normalCommentList:
			continue
		childLikelihood = float(stnObj.m_childDocMap[childName])
		# print childName
		childLikelihood4StnMAP[childName] = childLikelihood

	modelChildRankList = sorted(childLikelihood4StnMAP, key=childLikelihood4StnMAP.__getitem__, reverse=True)

	# random.shuffle(modelChildRankList)

	# print "stnName\t", stnObj.getName()
	# print "modelChildRankList\t", modelChildRankList
	# print "groundTruthChildRankList\t", groundTruthChildRankList

	print modelChildRankList
	print groundTruthChildRankList
	AP = 0
	hit = 0
	precisionK = 0
	# if len(modelChildRankList) == 0:
	# 	print "zero len GT\t", groundTruthChildRankList
	# 	return 0
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

	# AP = AP/len(modelChildRankList)

	# if not AP:
		# print "AP is 0"

		# print debug

	return AP

def computePatK(corpusObj, K):

	totalPatK = 0
	totalStnNum = 0
	totalCorrespondingStnNum = 0

	for parentID in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentID]
		# print "parentName:", parentID, "\t", 

		for stnIndex in parentObj.m_stnList:
			stnObj = parentObj.m_stnMap[stnIndex]

			totalStnNum += 1

			if not len(stnObj.m_groundTruthChildList):
				continue

			childLikelihood4StnMAP={}
			for childName in stnObj.m_childDocMap.keys():
	
				childLikelihood = float(stnObj.m_childDocMap[childName])
				# print childName
				childLikelihood4StnMAP[childName] = childLikelihood

			orderedCommentListByLikelihood = sorted(childLikelihood4StnMAP, key=childLikelihood4StnMAP.__getitem__, reverse=True)

			if len(orderedCommentListByLikelihood) < K:
				continue

			PatK = PatK4Stn(stnObj, orderedCommentListByLikelihood, K)

			totalPatK += PatK
			totalCorrespondingStnNum += 1

	AvgPatK = totalPatK*1.0/totalCorrespondingStnNum
	print "avgPatK\t", AvgPatK, "\t totalPatK\t", totalPatK
	print "totalCorrespondingStnNum\t", totalCorrespondingStnNum, "\t", "totalStnNum\t", totalStnNum


def PatK4Stn(stnObj, rankCommentList, K):
	groundTruthChildRankList = stnObj.m_groundTruthChildList

	PatK = 0

	relevantNum = 0
	for indexInList in range(K):
		commentID = rankCommentList[indexInList]
		if commentID in groundTruthChildRankList:
			relevantNum += 1

	return relevantNum*1.0/K

def compuateNDCG(corpusObj):
	totalNDCG = 0
	totalStnNum = 0
	totalCorrespondingStnNum = 0

	for parentID in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentID]
		# print "parentName:", parentID, "\t", 

		for stnIndex in parentObj.m_stnList:
			stnObj = parentObj.m_stnMap[stnIndex]

			totalStnNum += 1

			if not len(stnObj.m_groundTruthChildList):
				continue

			childLikelihood4StnMAP={}
			for childName in stnObj.m_childDocMap.keys():
	
				childLikelihood = float(stnObj.m_childDocMap[childName])
				# print childName
				childLikelihood4StnMAP[childName] = childLikelihood

			orderedCommentListByLikelihood = sorted(childLikelihood4StnMAP, key=childLikelihood4StnMAP.__getitem__, reverse=True)

			# if len(orderedCommentListByLikelihood) < K:
			# 	continue

			ndcg = NDCG4Stn(stnObj, orderedCommentListByLikelihood)

			# print "stnIndex\t", stnIndex, "\t", ndcg, "\t"

			totalNDCG += ndcg
			totalCorrespondingStnNum += 1

		# print "\n"

	AvgNDCG = totalNDCG*1.0/totalCorrespondingStnNum
	print "avgNDCG\t", AvgNDCG, "\t totalNDCG\t", totalNDCG
	print "totalCorrespondingStnNum\t", totalCorrespondingStnNum, "\t", "totalStnNum\t", totalStnNum

def NDCG4Stn(stnObj, rankCommentList):
	groundTruthChildRankList = stnObj.m_groundTruthChildList
	ndcg = 0

	for commentID in groundTruthChildRankList:
		if commentID not in rankCommentList:
			print "error"

	# print rankCommentList
	for i in range(len(rankCommentList)):
		commentID = rankCommentList[i]

		dcg = 0
		if commentID in groundTruthChildRankList:
			dcg = 1.0/np.log(1+i+1)
		else:
			dcg = 0

		ndcg += dcg

	dcgGT = 0
	# print len(groundTruthChildRankList)
	# print "ndcg\t", ndcg

	# print groundTruthChildRankList
	for i in range(len(groundTruthChildRankList)):
		dcg = 1.0/np.log(1+i+1)

		dcgGT += dcg

	ndcg = ndcg*1.0/dcgGT


	# print "dcgGT\t", dcgGT

	return ndcg



if __name__ == '__main__':
	annotatedFile = "./annotatedFile.txt"
	corpusObj = _Corpus()

	
	simFile = "./LDA/topChild4Parent_LDA.txt"
	likelihoodFile = "./LDA/topChild4Stn_8.txt"

	# simFile = "./CorrLDA/topChild4Parent_CorrLDA.txt"
	# likelihoodFile = "./CorrLDA/topChild4Stn.txt"

	# simFile = "./SCTM/topChild4Parent_SCTM_2.txt"
	# likelihoodFile = "./SCTM/topChild4Stn_SCTM.txt"

	# simFile = "./DCMCorrLDA/topChild4Parent_DCMCorrLDA_prior.txt"
	# likelihoodFile = "./DCMCorrLDA/topChild4Stn_prior.txt"

	t_threshold = -0.1
	readCommentSimFile(simFile, corpusObj, t_threshold)
	readCommentLikelihoodFile(likelihoodFile, corpusObj)
	loadAnnotatedData(annotatedFile, corpusObj)

	# compuateNDCG(corpusObj)

	K = 1
	print "K\t", K
	computePatK(corpusObj, K)

	# proportionOfNormal = 1
	# rankNormalComment4Stn(corpusObj, proportionOfNormal)


