import numpy as np
import random
import matplotlib.pyplot as plt

class _Corpus:
	def __init__(self):
		self.m_wordMap = {} ####vocabulary
		self.m_wordList = []
		self.m_totalSim = 0
		self.m_avgSim = 0
		self.m_maxSim = 1.0000000000000002 ###1.0000000000000002
		self.m_minSim = -0.6729050813045061 ###-0.638035462628903 , -0.6729050813045061

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

def obtainTokenList(fileName, corpusObj):
	f = open(fileName)

	rawLine = f.readline()

	line = rawLine.strip().split("\t")
	lineLen = len(line)
	for i in range(1, lineLen):
		simUnit = line[i]
		simUnit = simUnit.split(":")

		corpusObj.m_articleWordList.append(simUnit[0])

def readFile(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		word = line[0]

		wordObj = _Word(word)
		corpusObj.m_wordMap.setdefault(word, wordObj)
		corpusObj.m_wordList.append(word)
		
		lineLen = len(line)
		for i in range(1, lineLen):
			simUnit = line[i]
			simUnit = simUnit.split(":")

			wordObj.m_wordSimMap.setdefault(simUnit[0], float(simUnit[1]))

			wordObj.m_articleTotalSim += (float(simUnit[1])-corpusObj.m_minSim)/(corpusObj.m_maxSim-corpusObj.m_minSim)
			# wordObj.m_articleTotalSim += float(simUnit[1])

	f.close()

def simStatistics(corpusObj):
	articleTotalSimList = []

	wordNuminArticle = 0
	firstWordFlag = True

	totalSim = 0
	avgSim = 0

	for wordStr in corpusObj.m_wordMap.keys():
		wordObj = corpusObj.m_wordMap[wordStr]

		if firstWordFlag:
			wordNuminArticle = len(wordObj.m_wordSimMap.keys())
			firstWordFlag = False
		else:
			if wordNuminArticle != len(wordObj.m_wordSimMap.keys()):
				print "wordStr========"
				print "error wordNuminArticle\t", wordNuminArticle, "\t", len(wordObj.m_wordSimMap.keys())

		articleTotalSimList.append(wordObj.m_articleTotalSim)

		totalSim += wordObj.m_articleTotalSim

	avgSim = totalSim/(len(corpusObj.m_wordMap.keys())*1.0)

	print "totalSim\t", totalSim
	print "word num\t", len(corpusObj.m_wordMap.keys())
	print "avgTotalSim\t", avgSim

	H, X1 = np.histogram(articleTotalSimList, bins=10, normed=True)
	dx = X1[1]-X1[0]
	F1 = np.cumsum(H)*dx

	plt.plot(X1[1:], F1)
	plt.xlabel("total sim")
	plt.ylabel("cdf")
	plt.title("total sim for word before stemming")
	plt.show()

fileName = "444_article_beforeStemming.txt"
corpusObj = _Corpus()
readFile(fileName, corpusObj)

simStatistics(corpusObj)