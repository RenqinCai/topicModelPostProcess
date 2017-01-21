###we first compute MAP
class _algorithm:
	def __init__(self):
		self.m_index = 0
		self.m_commentMap = {}
		self.m_stnCommentRankingMap = {}


class _stn:
	def __init__(self):
		self.m_name = ""
		self.m_groundtruthRanking = {}

class _corpus:
	def __init__(self):
		self.m_stnMap = {} ###stnName:stnObj


def loadAnswer(answerFile, corpusObj):
	f = open(answerFile)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		stnIndex = line[0]
		commentName = line[1]
		relevanceScore = line[2]

		stnName = commentName.split("_")




def loadAlgorithm():
