import numpy as np
import random
import matplotlib.pyplot as plt


class _Corpus:
	def __init__(self):
		self.m_wordMap = {}
		self.m_wordList = []

class _Word:
	def __init__(self, name):
		self.m_name = name
		self.m_wordSimMap = {}

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

	f.close()

def printMaxSimWord(corpusObj):
	# print len(corpusObj.m_wordMap)
	# print corpusObj.m_wordList
	for word in corpusObj.m_wordList:
		# print word
		wordObj = corpusObj.m_wordMap[word]
		# print wordObj.m_name
		simList4OneWord = []
		for simWord in corpusObj.m_wordMap[word].m_wordSimMap.keys():
			simList4OneWord.append(corpusObj.m_wordMap[word].m_wordSimMap[simWord])

		orderedWordList = sorted(wordObj.m_wordSimMap, key=wordObj.m_wordSimMap.__getitem__, reverse=True)
		# print orderedWordList
		print "============="
		print "\t", wordObj.m_name, "\t--->\t", orderedWordList[0], "\t sim\t", wordObj.m_wordSimMap[orderedWordList[0]]
		print "mean+/-variance\t", np.mean(simList4OneWord), "\t", np.var(simList4OneWord)


def plotStatistics(corpusObj):
	wordIndex = random.randint(0, len(corpusObj.m_wordList)-1)
	word = corpusObj.m_wordList[wordIndex]
	word = "respiratori"
	word = "electron"

	simList4OneWord = []
	for simWord in corpusObj.m_wordMap[word].m_wordSimMap.keys():
		simList4OneWord.append(corpusObj.m_wordMap[word].m_wordSimMap[simWord])
	print word

	orderedXList = sorted(simList4OneWord)
	print orderedXList

	H, X1 = np.histogram(simList4OneWord, bins=10, normed=True)
	dx = X1[1]-X1[0]
	F1 = np.cumsum(H)*dx

	plt.plot(X1[1:], F1)
	plt.xlabel("sim")
	plt.ylabel("cdf")
	plt.title("sim for word")
	plt.show()

fileName = "444_3_2.txt"
corpusObj = _Corpus()
readFile(fileName, corpusObj)
# plotStatistics(corpusObj)

printMaxSimWord(corpusObj)


