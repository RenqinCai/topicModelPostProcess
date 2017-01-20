import numpy as np
from collections import Counter

##29
####relevance score: 0--bad, 1--fair, 2--good, 3--Excellent, 4--Perfect
class _comment:
	def __init__(self):
		self.m_name = ""
		self.m_stnList = []

class _stn:
	def __init__(self):
		self.m_name = ""
		self.m_commentMap = {}  ###commentID:[relevanceScore]

class _parentDoc:
	def __init__(self):
		self.m_name = ""
		self.m_commentMap = {}
		self.m_stnMap = {} 

class _corpus:
	def __init__(self):
		self.m_parentMap = {}


def readFile(answerFile, corpusObj):
	f = open(answerFile)

	commaNum = 0

	firstLineFlag = True
	for rawLine in f:
		if firstLineFlag:
			commaNum = len(rawLine.strip().split("\t"))
			firstLineFlag = False
			print commaNum
			continue

#"109_1019_14	4	"
		line = rawLine.strip().split("\"")
		line = [lineEle for lineEle in [lineEle.strip() for lineEle in line] if lineEle]

		answerContext = line[len(line)-1]
		answerContext = answerContext.split("\t")
		# print answerContext
		answerNum = len(answerContext)/2
		for answerIndex in range(answerNum):
			commentStn = answerContext[answerIndex*2]
			# print commentStn
			if "sanity" in commentStn:
				commentStnSplited = commentStn.split("_")
				parentID = commentStnSplited[0]
				commentID = commentStnSplited[0]+"_"+commentStnSplited[1]
				relativeOrder = int(answerContext[answerIndex*2+1])

				parentObj = corpusObj.m_parentMap[parentID]
				commentObj = parentObj.m_commentMap[commentID]
				stn1Relevance2Comment = commentObj.m_stnList[0].m_commentMap[commentID]
				stn2Relevance2Comment = commentObj.m_stnList[1].m_commentMap[commentID]

				# if stn1Relevance2Comment > stn2Relevance2Comment:
				# 	if relativeOrder != 0:

				# if stn1Relevance2Comment < stn2Relevance2Comment:
				#  	if relativeOrder != 1:

				# if stn1Relevance2Comment == stn2Relevance2Comment:
				# 	if relativeOrder != 2 or relativeOrder !=3:

			else:

				commentStnSplited = commentStn.split("_")
				parentID = commentStnSplited[0]
				commentID = commentStnSplited[0]+"_"+commentStnSplited[1]
				stnID = commentStnSplited[2]
				relevanceScore = 2
				if "empty" in answerContext[answerIndex*2+1]:
					relevanceScore = 2
				else:
					relevanceScore = int(answerContext[answerIndex*2+1])

				parentObj = None
				if parentID not in corpusObj.m_parentMap.keys():
					parentObj = _parentDoc()
					corpusObj.m_parentMap.setdefault(parentID, parentObj)
				else:
					parentObj = corpusObj.m_parentMap[parentID]

				stnObj = None
				if stnID not in parentObj.m_stnMap.keys():
					stnObj = _stn()
					parentObj.m_stnMap.setdefault(stnID, stnObj)
				else:
					stnObj = parentObj.m_stnMap[stnID]

				commentObj = None
				if commentID not in parentObj.m_commentMap.keys():
					commentObj = _comment()
					parentObj.m_commentMap.setdefault(commentID, commentObj)
				else:
					commentObj = parentObj.m_commentMap[commentID]
				commentObj.m_stnList.append(stnObj)

				if commentID not in stnObj.m_commentMap.keys():
					stnObj.m_commentMap.setdefault(commentID, [])
					stnObj.m_commentMap[commentID].append(relevanceScore)
				else:
					stnObj.m_commentMap[commentID].append(relevanceScore)

	f.close()

def statistics(corpusObj, statisticsFile):
	f = open(statisticsFile, "w")

	for parentID in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentID]

		print parentID, "\t", len(parentObj.m_stnMap.keys())
		for stnID in parentObj.m_stnMap.keys():
			stnObj = parentObj.m_stnMap[stnID]

			for commentID in stnObj.m_commentMap.keys():
				relevanceScoreList = stnObj.m_commentMap[commentID]
				x = Counter(relevanceScoreList)
				majorRelevanceScore = x.most_common(1)[0][0]
				majorRelevanceNum = x.most_common(1)[0][1]
				print majorRelevanceNum
				majorProportion = majorRelevanceNum*1.0/len(relevanceScoreList)

				print stnID, "\t", commentID, "\t", majorRelevanceScore, "\t", len(relevanceScoreList), "\t", majorProportion
				f.write(str(stnID)+"\t"+str(commentID)+"\t")
				f.write(str(majorRelevanceScore)+"\t"+str(len(relevanceScoreList))+"\t"+str(majorProportion))
				f.write("\n")

corpusObj = _corpus()
answerFile = "answer.txt"
readFile(answerFile, corpusObj)
print "hello"

statisticsFile = "answerStatistics.txt"
statistics(corpusObj,statisticsFile)











