import numpy as np
from sklearn.cluster import KMeans

def loadProportion(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")

		parentName = line[0]
		lineLen = len(line)

		parentTopicProportion = []

		for i in range(2, lineLen):
			lineElement = line[i]
			if "sentence" in lineElement:
				break
			parentTopicProportion.append(float(line[i]))



		corpusObj.setdefault(parentName, parentTopicProportion)

	f.close()

def clusterDoc(corpusObj, labelMapObj):
	totalFeatureList = []
	labelList = []
	totalSample = 0
	for parentName in corpusObj.keys():
		parentTopicProportion = corpusObj[parentName]

		totalSample += 1
		labelList.append(parentName)
		totalFeatureList.append(parentTopicProportion)

	totalFeatureArray = np.array(totalFeatureList)
	estKMeans = KMeans(n_clusters=10)
	estKMeans.fit(totalFeatureArray)

	for i in range(totalSample):
		sampleLabel = estKMeans.labels_[i]
		parentName = labelList[i]

		if sampleLabel not in labelMapObj.keys():
			labelMapObj.setdefault(sampleLabel, [])

		labelMapObj[sampleLabel].append(parentName)

	for sampleLabel in labelMapObj.keys():
		parentNameList = labelMapObj[sampleLabel]

		print sampleLabel, "\t", parentNameList

###parentDoc:parentTopicProportion
corpusObj = {}

labelMapObj = {}

fileName = "parentParameter_lda.txt"
loadProportion(fileName, corpusObj)
clusterDoc(corpusObj, labelMapObj)