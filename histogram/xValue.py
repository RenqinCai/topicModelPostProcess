import numpy as np
import os
import matplotlib.pyplot as plt

class _Corpus:
	def __init__(self):
		self.m_proportionMap = {} ##proportion:Num
		self.m_proportionWordsMap = {} ##proportion:wordsList

		self.m_wordTTFMap = {} ###word:TTF

def readFile(fileName, corpusObj):
	f = open(fileName)
	# print fileName

	for rawLine in f:
		line = rawLine.strip().split("\t")

		for lineEle in line:
			wordEle = lineEle.split(":")
			word = wordEle[0]
			wordXProportion = float(wordEle[2])

			if wordXProportion not in corpusObj.m_proportionMap.keys():
				corpusObj.m_proportionMap.setdefault(wordXProportion, 1)
				corpusObj.m_proportionWordsMap.setdefault(wordXProportion, [])
			else:
				corpusObj.m_proportionMap[wordXProportion] += 1
				corpusObj.m_proportionWordsMap[wordXProportion].append(word)

	f.close()

def readTTFFile(TTFFile, corpusObj):
	f = open(TTFFile)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		word = line[0]
		wordTTF = float(line[10])

		corpusObj.m_wordTTFMap.setdefault(word, wordTTF)


def plotXStatistics(corpusObj):
	xList = corpusObj.m_proportionMap.keys()
	yList = []

	totalWordNum = 0
	for xProportion in xList:
		totalWordNum +=	corpusObj.m_proportionMap[xProportion]

	print totalWordNum

	orderedXList = sorted(xList)
	last = 0
	for xProportion in orderedXList:
		ratio = (corpusObj.m_proportionMap[xProportion]+last) / (totalWordNum*1.0)
		yList.append(ratio)
		last += corpusObj.m_proportionMap[xProportion]

		avgTTF = 0
		for word in corpusObj.m_proportionWordsMap[xProportion]:
			if word not in corpusObj.m_wordTTFMap.keys():
				# print word
				continue
			else:
				avgTTF += corpusObj.m_wordTTFMap[word]

		avgTTF = avgTTF/len(corpusObj.m_proportionWordsMap[xProportion])

		print xProportion
		print avgTTF
		# print corpusObj.m_proportionWordsMap[xProportion] 
		print "================"
	# plt.plot(orderedXList, yList)
	# plt.show()


fileDir = "./xAssignment_ACCTMGlobalC"

corpusObj = _Corpus()

TTFFile = "fv_1gram_stat_Tech_LDAGibbs4AC_test.txt"

for fileName in os.listdir(fileDir):
	if fileName.endswith(".txt"):
		readFile(os.path.join(fileDir, fileName), corpusObj)

readTTFFile(TTFFile, corpusObj)

plotXStatistics(corpusObj)





			

