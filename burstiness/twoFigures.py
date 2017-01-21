import matplotlib.pyplot as plt

class corpus:
	def __init__(self):
		self.m_wordFrequencyList = []
		self.m_wordAvgProbList = []
		self.m_wordVarList = []
		self.m_naturalWordFrequencyList = []
		self.m_naturalWordProbList = []

def readNaturalFile(fileName, c):
	f = open(fileName)

	timesMap = {}

	totalTimes = 0;

	for rawLine in f:
		line = rawLine.strip().split(":")
		wordTimes = float(line[0])
		timesProb = float(line[1])

		timesMap.setdefault(wordTimes, timesProb)

	
	wordTimesSortedList = sorted(timesMap.keys(), reverse=True)

	accumulateTimes = 0
	x = []
	y = []
	for wordTimes in wordTimesSortedList:
		timesProb = timesMap[wordTimes]
		# print wordTimes, timesProb

		x.append(wordTimes)
		y.append(timesProb)

	c.m_naturalWordFrequencyList = x
	c.m_naturalWordProbList = y


def readSyntheticFile(fileName):
	f = open(fileName)

	c = corpus()
	for rawLine in f:
		line = rawLine.strip().split("\t")
		wordFrequency = float(line[0])
		wordAvgProb = float(line[1])
		wordVar = float(line[2])

		c.m_wordFrequencyList.append(wordFrequency)
		c.m_wordAvgProbList.append(wordAvgProb)
		c.m_wordVarList.append(wordVar)

	return c

def plotCorpus(c1, c2):


	x11 = c1.m_naturalWordFrequencyList
	y11 = c1.m_naturalWordProbList

	x12 = c1.m_wordFrequencyList
	y12 = c1.m_wordAvgProbList
	y12ValList = c1.m_wordVarList

	fig = plt.figure()
	# fig.set_size_inches(15, 6)

	ax = fig.add_subplot(121)
	ax.set_yscale('log')
	ax.errorbar(x11, y11, label="genuine commented data")
	ax.errorbar(x12, y12,  linewidth=1, yerr=[y12ValList, y12ValList], label="synthetic commented data")
	ax.tick_params(axis='x', labelsize=8)
	ax.tick_params(axis='y', labelsize=8)
	plt.xlim([0, 50])
	plt.ylabel("probability", fontsize=10)
	plt.xlabel("a word occuring n times in an article and its comments", fontsize=10)
	plt.title("ArsTechnica Science Dataset", fontsize=10)
	plt.legend(prop={'size':10})


	x21 = c2.m_naturalWordFrequencyList
	y21 = c2.m_naturalWordProbList

	x22 = c2.m_wordFrequencyList
	y22 = c2.m_wordAvgProbList
	y22ValList = c2.m_wordVarList


	ax = fig.add_subplot(122)
	ax.set_yscale('log')
	ax.errorbar(x21, y21, label="genuine commented data")
	ax.errorbar(x22, y22, linewidth=1, yerr=[y22ValList, y22ValList], label="synthetic commented data")
	ax.tick_params(axis='x', labelsize=8)
	ax.tick_params(axis='y', labelsize=8)
	plt.xlim([0, 50])
	plt.ylabel("probability", fontsize=10)
	plt.xlabel("a word occuring n times in an article and its comments", fontsize=10)
	plt.title("Yahoo! News Dataset", fontsize=10)
	plt.legend(prop={'size':10})

	height = fig.get_figheight()
	print height

	width = fig.get_figwidth()
	print width
	# fig.set_size_inches([9, 3.4])
	# fig.savefig("burstiness.png", dpi=400)
	plt.show()

techSyntheticFile = "tech_burstiness.txt"
yahooSyntheticFile = "yahoo_burstiness.txt"

techCorpus = readSyntheticFile(techSyntheticFile)
yahooCorpus = readSyntheticFile(yahooSyntheticFile)

techNaturalFile = "20160913-2026-Burstiness-Tech_burstiness.txt"
yahooNaturalFile = "20160913-2038-Burstiness-Yahoo_burstiness.txt"

readNaturalFile(techNaturalFile, techCorpus)
readNaturalFile(yahooNaturalFile, yahooCorpus)

plotCorpus(techCorpus, yahooCorpus)
