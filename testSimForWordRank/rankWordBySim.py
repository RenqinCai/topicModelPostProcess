import numpy as np
import os
import matplotlib.pyplot as plt

class _Corpus:
	def __init__(self):
		self.m_rawFeatureMap = {} ##rawFature:rawFeatureIndex
		self.m_simMatrix = {} ## rawFeatureIndex: featureObj
		self.m_articleObjMap = {} ##articleName: articleObj
		self.m_topicWordProbMap = {} ##topic:{word:prob}
		self.m_stemFeatureTTFMap = {}  ##stemmedFeature: TTF
		self.m_topicNum = 0
		self.m_beta = 0.001
		self.m_totalFeatureSize = 0
		self.m_normalizedBeta = self.m_totalFeatureSize*self.m_beta
		self.m_maxSim = 1.0000000000000002 ###1.0000000000000002
		self.m_minSim = -0.6729050813045061 ###-0.638035462628903 , -0.6729050813045061
		self.m_rawFeature2FeatureMap = {}  ###string: string
		self.m_rawFeatureTTFMap = {}  #rawFeature:TTF

class _RawFeature:
	def __init__(self, name):
		self.m_name = name
		self.m_featureSimMap = {} ## rawFeatureIndex:sim
		self.m_tid = 0
		self.m_stemFeature = ""
		self.m_fId = 0
		self.m_totalSim = 0 ###vec sim
		self.m_simRatioList = []

class _Article:
	def __init__(self, name):
		self.m_name = name
		self.m_wordMap = {}  ###topicIndex:[rawFeatureObj]
		self.m_commentObjList = []
		self.m_topicNormalizedTerm = {} ###topicIndex:topicNormalizedTerm

class _Comment:
	def __init__(self, name):
		self.m_name = name
		self.m_wordMap = {}  ###topicIndex:[rawFeatureObj]
		self.m_relevant = False
		self.m_rareTopicWordMap = {}  #topic: wordList
		self.m_rareWordByUniformList = []
		self.m_rareWordByTopicList = []

def loadSimText(fileName, corpusObj):
	f = open(fileName)

	firstLineFlag = True

	rawLine = f.readline()
	line = rawLine.strip().split("\t")
	lineLen = len(line)

	for rawFeatureIndex in range(lineLen):
		rawFeature = line[rawFeatureIndex]
		corpusObj.m_rawFeatureMap.setdefault(rawFeature, rawFeatureIndex)

		featureObj = _RawFeature(rawFeature)
		corpusObj.m_simMatrix.setdefault(rawFeatureIndex, featureObj)

	corpusObj.m_totalFeatureSize = len(corpusObj.m_rawFeatureMap)
	print "corpus total Feature\t", corpusObj.m_totalFeatureSize

	rowFeatureIndex = 0
	for rawLine in f:
		line = rawLine.strip().split("\t")
		lineLen = len(line)
	
		for colFeatureIndex in range(lineLen):
			sim = float(line[colFeatureIndex])
			sim = (sim-corpusObj.m_minSim)/(corpusObj.m_maxSim-corpusObj.m_minSim)
			# sim = np.exp(sim)

			rowFeatureObj = corpusObj.m_simMatrix[rowFeatureIndex]
			rowFeatureObj.m_featureSimMap.setdefault(colFeatureIndex, sim)
			rowFeatureObj.m_totalSim += sim
		rowFeatureIndex += 1

def loadArticle(dirName, fileName, corpusObj):
	f = open(os.path.join(dirName, fileName))

	articleName = ""
	if fileName.endswith(".txt"):
		articleName = fileName[:-4]
	else:
		print "error"
		articleName = "error"

	print "load article\t",articleName

	articleObj = _Article(articleName)
	for rawLine in f:
		line = rawLine.strip().split("\t")

		lineLen = len(line)
		for unitIndex in range(lineLen):
			unit = line[unitIndex]
			unit = unit.strip().split(":")

			rawFeature = unit[0]
			rawFeatureObj = _RawFeature(rawFeature)
			topicIndex = int(unit[2])

			rawFeatureIndex = corpusObj.m_rawFeatureMap.get(rawFeature)
			rawFeatureObj.m_fId = rawFeatureIndex

			if topicIndex not in articleObj.m_wordMap.keys():
				articleObj.m_wordMap.setdefault(topicIndex,[])
			else:
				articleObj.m_wordMap[topicIndex].append(rawFeatureObj)

	f.close()
	corpusObj.m_topicNum = 15
	corpusObj.m_articleObjMap.setdefault(articleName, articleObj)

def loadComment(dirName, fileName, corpusObj):
	f = open(os.path.join(dirName, fileName))

	commentName = fileName[:-4]
	commentObj = _Comment(commentName)

	print "commentName\t", commentName

	articleName = ""
	if fileName.endswith(".txt"):
		articleName = fileName.strip().split("_")[0]
	else:
		print "error"
		articleName = "error"

	for rawLine in f:
		line = rawLine.strip().split("\t")

		lineLen = len(line)
		for unitIndex in range(lineLen):
			unit = line[unitIndex]
			unit = unit.strip().split(":")

			rawFeature = unit[0]
			stemFeature = unit[1]
			topicIndex = int(unit[2])

			rawFeatureObj = _RawFeature(rawFeature)
			rawFeatureObj.m_stemFeature = stemFeature
			rawFeatureIndex = corpusObj.m_rawFeatureMap.get(rawFeature)
			rawFeatureObj.m_fId = rawFeatureIndex

			if topicIndex not in commentObj.m_wordMap.keys():
				commentObj.m_wordMap.setdefault(topicIndex,[])
				commentObj.m_wordMap[topicIndex].append(rawFeatureObj)
			else:
				commentObj.m_wordMap[topicIndex].append(rawFeatureObj)

	articleObj = corpusObj.m_articleObjMap[articleName]
	articleObj.m_commentObjList.append(commentObj)

def loadTTF(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		word = line[0]
		wordTTF = float(line[10])

		corpusObj.m_stemFeatureTTFMap.setdefault(word, wordTTF)

def loadRawTTF(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		word = line[0]
		wordTTF = float(line[10])

		corpusObj.m_rawFeatureTTFMap.setdefault(word, wordTTF)


def loadTopicWordProb(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		tid = int(line[0])

		corpusObj.m_topicWordProbMap.setdefault(tid, {})
		lineLen = len(line)
		for i in range(1, lineLen):
			unit = line[i].split(":")
			stemFeature = unit[0]
			wordTopicProb = float(unit[1])

			corpusObj.m_topicWordProbMap[tid].setdefault(stemFeature, wordTopicProb)

	f.close()

def plotHistogram(x):
	# x = np.random.normal(size = 1000)
	plt.hist(x, bins=np.linspace(0, 1, 20))
	plt.ylabel('Probability');
	plt.show()

def loadWordSim(corpusObj):
	randomFeatureList = np.random.choice(corpusObj.m_totalFeatureSize, 30)

	for featureIndex in randomFeatureList:
		featureObj = corpusObj.m_simMatrix[featureIndex]
		if featureObj.m_name not in corpusObj.m_rawFeature2FeatureMap.keys():
			continue
		feature = corpusObj.m_rawFeature2FeatureMap[featureObj.m_name]
		TTF = corpusObj.m_stemFeatureTTFMap[feature]

		if TTF > 50:
			continue

		wordSimMap = {}

		simList = []
		for simWordIndex in featureObj.m_featureSimMap.keys():
			simWordObj = corpusObj.m_simMatrix[simWordIndex]
			if simWordObj.m_name not in corpusObj.m_rawFeature2FeatureMap.keys():
				continue
			feature = corpusObj.m_rawFeature2FeatureMap[simWordObj.m_name]
			TTF = corpusObj.m_stemFeatureTTFMap[feature]
			if TTF > 50:
				continue

			sim = featureObj.m_featureSimMap[simWordIndex]
			simList.append(sim)
			wordSimMap.setdefault(simWordIndex, sim)

		plotHistogram(simList)
		print "========="
		print featureObj.m_name
		print "sim mean+/-var %f+/-%f\t"%(np.mean(simList), np.var(simList))
		wordList = sorted(wordSimMap, key=wordSimMap.__getitem__, reverse=True)
		# print featureObj.m_name
		for simWordIndex in wordList[:20]:
			simFeatureObj = corpusObj.m_simMatrix[simWordIndex]
			print simFeatureObj.m_name, "\t",
		print "\n"
		
def rankWord4TopicSim(corpusObj):
	corpusObj.m_topicNum = len(corpusObj.m_topicWordProbMap.keys())
	for topicIndex in range(corpusObj.m_topicNum):
		print "==========topicIndex\t", topicIndex
		simRatioMap = {}
		simRatioList = []
		topicWordProb = corpusObj.m_topicWordProbMap[topicIndex]	
		sortedWordList = sorted(topicWordProb, key=topicWordProb.__getitem__, reverse=True)

		normalizedSim = 0
		for rawFeatureIndex in range(corpusObj.m_totalFeatureSize):
			rawFeatureSim = 0
			for word in sortedWordList[:20]:
				wordIndex = corpusObj.m_rawFeatureMap[word]
				rawFeatureSim += corpusObj.m_simMatrix.get(rawFeatureIndex).m_featureSimMap[wordIndex]
			normalizedSim +=rawFeatureSim

		print sortedWordList[:20]
		print "*********************"

		for rawFeatureIndex in range(corpusObj.m_totalFeatureSize):
			rawFeature = corpusObj.m_simMatrix[rawFeatureIndex].m_name
			rawTTF = corpusObj.m_rawFeatureTTFMap[rawFeature]

			if rawTTF > 50:
				continue

			if topicIndex not in corpusObj.m_topicWordProbMap.keys():
				simRatio = corpusObj.m_beta/corpusObj.m_normalizedBeta;
				simRatioMap.setdefault(rawFeatureIndex, simRatio)
				simRatioList.append(simRatio)
				print "error missing topic"
			else:
				maxRawFeatureSim = 0
				for word in sortedWordList[:20]:
					wordIndex = corpusObj.m_rawFeatureMap[word]
					rawFeatureSim = corpusObj.m_simMatrix[rawFeatureIndex].m_featureSimMap[wordIndex]

					if rawFeatureSim > maxRawFeatureSim:
						maxRawFeatureSim = rawFeatureSim

				simRatio = (rawFeatureSim+corpusObj.m_beta)/(normalizedSim+corpusObj.m_normalizedBeta)
				simRatioMap.setdefault(rawFeatureIndex, simRatio)
				simRatioList.append(simRatio)

		featureList4Sim = sorted(simRatioMap, key=simRatioMap.__getitem__, reverse=True)

		# plotHistogram(simRatioList)
		# print simRatioList
		print "mean+/-variance\t %f+/-%f"%(np.mean(simRatioList), np.var(simRatioList))

		for featureIndex in featureList4Sim[:30]:
			feature = corpusObj.m_simMatrix[featureIndex].m_name
			print feature,":", simRatioMap[featureIndex], "\t", 
		print "\n"

def simStatistics(corpusObj, TTFThreshold):
	# TTFThreshold = 40

	print debug
	for articleName in corpusObj.m_articleObjMap.keys():
		articleObj = corpusObj.m_articleObjMap[articleName]

		computeSimNormalizedTerm(articleObj)

		for commentObj in articleObj.m_commentObjList:
			commentWordList = []
			for topicIndex in commentObj.m_wordMap.keys():
				for rawFeatureObj in commentObj.m_wordMap[topicIndex]:
					commentWordList.append(rawFeatureObj)

			for rawFeatureObj in commentWordList:
				stemFeature = rawFeatureObj.m_stemFeature
				rawFeatureIndex = rawFeatureObj.m_fId

				stemFeatureTTF = corpusObj.m_stemFeatureTTFMap[stemFeature]
				if stemFeatureTTF > TTFThreshold:
					continue

				allSmallFlag = True
				for topicIndex in range(corpusObj.m_topicNum):
					rawFeatureSim = 0
					if topicIndex not in articleObj.m_wordMap.keys():
						simRatio = corpusObj.m_beta/corpusObj.m_normalizedBeta;
						rawFeatureObj.m_simRatioList.append(simRatio)
					else:
						for pRawFeatureObj in articleObj.m_wordMap[topicIndex]:
							pRawFeatureIndex = pRawFeatureObj.m_fId
							rawFeatureSim += corpusObj.m_simMatrix.get(rawFeatureIndex).m_featureSimMap[pRawFeatureIndex]

						simRatio = (rawFeatureSim+corpusObj.m_beta)/(articleObj.m_topicNormalizedTerm[topicIndex]+corpusObj.m_normalizedBeta)
						rawFeatureObj.m_simRatioList.append(simRatio)

						topicWordProb = 1.0/corpusObj.m_totalFeatureSize

						if topicWordProb < simRatio:
							allSmallFlag = False
							if topicIndex not in commentObj.m_rareTopicWordMap.keys():
								commentObj.m_rareTopicWordMap.setdefault(topicIndex, [])
							else:
								commentObj.m_rareTopicWordMap[topicIndex].append(rawFeatureObj)

							if rawFeatureObj not in commentObj.m_rareWordByTopicList:
								commentObj.m_rareWordByTopicList.append(rawFeatureObj)

				if allSmallFlag:
					commentObj.m_rareWordByUniformList.append(rawFeatureObj)

def computeSim4TwoWords(rawFeature1, articleObj, corpusObj, tid):
	articleRawFeatureObjList = articleObj.m_wordMap[tid]

	totalSim = 0
	for articleRawFeatureObj in articleRawFeatureObjList:
		articleRawFeatureIndex = articleRawFeatureObj.m_fId
		sim = corpusObj.m_simMatrix[articleRawFeatureIndex].m_featureSimMap[rawFeature1]
		totalSim += sim

	return totalSim

def computeSimNormalizedTerm(articleObj):

	for topicIndex in articleObj.m_wordMap.keys():
		wordObjList = articleObj.m_wordMap[topicIndex]
		normalizedSim = 0

		for articleWordObj in wordObjList:
			articleRawFeatureIndex = articleWordObj.m_fId
			normalizedSim += corpusObj.m_simMatrix[articleRawFeatureIndex].m_totalSim
		
		articleObj.m_topicNormalizedTerm.setdefault(topicIndex, normalizedSim)

def printWordStatisticsInComments(corpusObj):
	for articleName in corpusObj.m_articleObjMap.keys():
		articleObj = corpusObj.m_articleObjMap[articleName]
		print "============"
		print "articleName"
		for commentObj in articleObj.m_commentObjList:
			print "\t\t\t\t",commentObj.m_name

			for topicIndex in range(corpusObj.m_topicNum):
				print "\t\t\t\t", topicIndex
				if topicIndex not in commentObj.m_wordMap.keys():
					continue
				for wordObj in commentObj.m_wordMap[topicIndex]:
					print wordObj.m_name, "\t",
				print "\n"

			print "\t\t+++++++\t\t uniform"
			for rawFeatureObj in commentObj.m_rareWordByUniformList:
				print rawFeatureObj.m_name, "\t", rawFeatureObj.m_simRatioList

			print "\t\t+++++++\t\t uniform"
			for topicIndex in range(corpusObj.m_topicNum):
				print "\t\t\t\t\t", topicIndex
				probMap = {}  ###featureIndex, value
				for rawFeatureObj in commentObj.m_rareWordByTopicList:
					probMap.setdefault(rawFeatureObj, rawFeatureObj.m_simRatioList[topicIndex])

				wordList = sorted(probMap, key=probMap.__getitem__, reverse=True)

				for rawFeatureObj in wordList:
					feature = rawFeatureObj.m_name
					prob = probMap[rawFeatureObj]
					print "feature %s prob %f\t"%(feature, prob)

def loadFeatureMap(rawFeatureMapFile, corpusObj):
	f = open(rawFeatureMapFile)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		rawFeature = line[0]
		feature = line[1]

		corpusObj.m_rawFeature2FeatureMap.setdefault(rawFeature, feature)

	f.close()

corpusObj = _Corpus()
simFile = "./wordSim_Tech.txt"

TTFFile = "fv_1gram_stat_Tech_LDAGibbs4AC_test.txt"
loadTTF(TTFFile, corpusObj)

rawTTFFile = "fv_1gram_stat_Tech_LDAGibbs4ACWithRawToken_test.txt"
loadRawTTF(rawTTFFile, corpusObj)

rawFeatureMapFile = "rawFeature2FeatureMap.txt"
loadFeatureMap(rawFeatureMapFile, corpusObj)

loadSimText(simFile, corpusObj)

wordTopicProbFile = "topicWord.txt"
loadTopicWordProb(wordTopicProbFile, corpusObj)

# rankWordSim(corpusObj)
rankWord4TopicSim(corpusObj)



# articleFolder = "parentTopicAssignment/"
# commentFolder = "childTopicAssignment/"

# articleNum = 1
# articleIndex = 0
# for fileName in os.listdir(articleFolder):
# 	if articleIndex < articleNum:
# 		if fileName.endswith(".txt"):
# 			loadArticle(articleFolder, fileName, corpusObj)
# 			articleIndex += 1

# for fileName in os.listdir(commentFolder):
# 	if fileName.endswith(".txt"):
# 		loadComment(commentFolder, fileName, corpusObj)



# TTFThreshold = 50
# simStatistics(corpusObj, TTFThreshold)
# printWordStatisticsInComments(corpusObj)
