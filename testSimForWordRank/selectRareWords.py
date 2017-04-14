class _Corpus:
	def __init__(self):
		self.m_stemFeatureTTFMap = {}  ###string:double

def loadTTF(fileName, corpusObj, threshold):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		word = line[0]
		wordTTF = float(line[10])

		corpusObj.m_stemFeatureTTFMap.setdefault(word, wordTTF)

		if wordTTF < threshold:
			print word, "\t", wordTTF

threshold = 50
corpusObj = _Corpus()
TTFFile = "fv_1gram_stat_Tech_LDAGibbs4AC_test.txt"
loadTTF(TTFFile, corpusObj, threshold)