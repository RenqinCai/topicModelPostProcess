import numpy as np
import random
import matplotlib.pyplot as plt
import os

class _Corpus:
	def __init__(self):
		self.m_articleList = [] ###article Obj
		self.m_validArticleList = []
		self.m_invalidArticleList = []

class _Article:
	def __init__(self, name):
		self.m_name = name
		self.m_wordMap = {} ####vocabulary
		self.m_wordList = []
		self.m_totalSim = 0
		self.m_avgSim = 0
		self.m_maxSim = 1.0000000000000002 ###1.0000000000000002
		self.m_minSim = -0.6729050813045061 ###-0.638035462628903 (after stemming), -0.6729050813045061 (before stemming)

		self.m_articleWordList = []

class _Word:
	def __init__(self, name):
		self.m_name = name
		self.m_wordSimMap = {}
		self.m_articleTotalSim = 0

class _ArticleWord:
	def __init__(self, name):
		self.m_name = name
		self.m_simList = []

def obtainTokenList(fileName, articleObj):
	f = open(fileName)

	rawLine = f.readline()

	line = rawLine.strip().split("\t")
	lineLen = len(line)
	for i in range(1, lineLen):
		simUnit = line[i]
		simUnit = simUnit.split(":")

		articleObj.m_articleWordList.append(simUnit[0])

	f.close()

def readFile(fileName, articleObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		word = line[0]

		wordObj = _Word(word)
		articleObj.m_wordMap.setdefault(word, wordObj)
		articleObj.m_wordList.append(word)
		
		lineLen = len(line)
		for i in range(1, lineLen):
			simUnit = line[i]
			simUnit = simUnit.split(":")

			wordObj.m_wordSimMap.setdefault(simUnit[0], float(simUnit[1]))

			# wordObj.m_articleTotalSim += (float(simUnit[1])-corpusObj.m_minSim)/(corpusObj.m_maxSim-corpusObj.m_minSim)
			# wordObj.m_articleTotalSim += float(simUnit[1])
	f.close()

def simStatistics(corpusObj, threshold):
	
	totalSim = 0
	avgSim = 0

	for articleObj in corpusObj.m_articleList:
		articleSimRatioList = []
		wordNuminArticle = 0
		firstWordFlag = True

		for articleWordStr in articleObj.m_articleWordList:
			totalSim = 0
			for wordStr in articleObj.m_wordMap.keys():
				wordObj = articleObj.m_wordMap[wordStr]

				wordObj.m_articleTotalSim = (wordObj.m_wordSimMap[articleWordStr]-articleObj.m_minSim)/(articleObj.m_maxSim-articleObj.m_minSim)

				# wordObj.m_articleTotalSim = wordObj.m_wordSimMap[articleWordStr]

				if firstWordFlag:
					wordNuminArticle = len(wordObj.m_wordSimMap.keys())
					firstWordFlag = False
				else:
					if wordNuminArticle != len(wordObj.m_wordSimMap.keys()):
						print "wordStr========"
						print "error wordNuminArticle\t", wordNuminArticle, "\t", len(wordObj.m_wordSimMap.keys())

				totalSim += wordObj.m_articleTotalSim

			for wordStr in articleObj.m_wordMap.keys():
				wordObj = articleObj.m_wordMap[wordStr]
				simRatio = wordObj.m_articleTotalSim/totalSim
				articleSimRatioList.append(simRatio)

		sortedArticleSimRatioList = sorted(articleSimRatioList)
		minArticleSim = sortedArticleSimRatioList[0]
		maxArticleSim = sortedArticleSimRatioList[-1]
		if minArticleSim < threshold and threshold < maxArticleSim:
			corpusObj.m_validArticleList.append(articleObj)
		else:
			corpusObj.m_invalidArticleList.append(articleObj)

	# avgSim = totalSim/(len(corpusObj.m_wordMap.keys())*1.0)

	# print "totalSim\t", totalSim
	# print "word num\t", len(corpusObj.m_wordMap.keys())
	# print "avgTotalSim\t", avgSim
	# print "article sim ratio list\t", articleSimRatioList
	print "valid article obj =============="
	for articleObj in corpusObj.m_validArticleList:
		print articleObj.m_name

	print "invalid article obj =============="
	for articleObj in corpusObj.m_invalidArticleList:
		print articleObj.m_name 

def plotStatistics(articleSimRatioList):
	sortedArticleSimRatioList = sorted(articleSimRatioList)

	print "min \t", sortedArticleSimRatioList[0]
	print "max \t", sortedArticleSimRatioList[-1]

	H, X1 = np.histogram(articleSimRatioList, bins=10, normed=True)
	dx = X1[1]-X1[0]
	F1 = np.cumsum(H)*dx

	plt.plot(X1[1:], F1)
	plt.xlabel("total sim")
	plt.ylabel("cdf")
	plt.title("total sim for word before stemming")
	plt.show()

def readDir(dirName, corpusObj, threshold):
	for fileName in os.listdir(dirName):
		if fileName.endswith(".txt"):
			articleObj = _Article(fileName)
			corpusObj.m_articleList.append(articleObj)
			obtainTokenList(os.path.join(dirName, fileName), articleObj)
			readFile(os.path.join(dirName, fileName), articleObj)
	simStatistics(corpusObj, threshold)

fileName = "444_article_beforeStemming.txt"
corpusObj = _Corpus()

threshold = 1.0/5745
dirName = "./articleSim"
readDir(dirName, corpusObj, threshold)
