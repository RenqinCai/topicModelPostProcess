import numpy as np
import random 

class _ParentDoc:
	def __init__(self):
		self.m_name = ""
		self.m_childDocs = []

class _ChildDoc:
	def __init__(self):
		self.m_trueLabel = -1
		self.m_predictLabel = -1
		self.m_name = ""
		self.m_xProportion = 0

def loadFile(fileName, corpusObj):
	f = open(fileName)
	
	for rawLine in f:
		line = rawLine.strip().split("\t")
		parentName = line[0]
		childName = line[1]
		x0 = float(line[2])
		x1 = float(line[3])
		
		childDocObj = _ChildDoc()
		childDocObj.m_name = childName
		
		if parentName not in corpusObj.keys():
			parentObj = _ParentDoc()
			parentObj.m_name = parentName
			parentObj.m_childDocs.append(childDocObj)
			corpusObj.setdefault(parentName, parentObj)
		else:
			parentObj = corpusObj[parentName]
			parentObj.m_childDocs.append(childDocObj)
		
		
		###1 spam, 0 not spam
		childDocObj.m_xProportion = x0
		
		trueParentName = childName.strip().split("_")[0]
		childIndex = childName.strip().split("_")[1]
		# if trueParentName == parentName:
		# 	childDocObj.m_trueLabel = 0
		# else:
		# 	childDocObj.m_trueLabel = 1

		if childIndex == "100":
			childDocObj.m_trueLabel = 1
			print trueParentName, "\t", parentName

def calMAP(corpusObj):
	totalParentNum = 0
	totalAP = 0
	for parentName in corpusObj.keys():
		totalParentNum += 1
		parentObj = corpusObj[parentName]
		
		childLen = len(parentObj.m_childDocs)
		childProportionMap = {}
		for i in range(childLen):
			childDocObj = parentObj.m_childDocs[i]
			xProportion = childDocObj.m_xProportion
			childProportionMap.setdefault(childDocObj, xProportion)
			
		##descending order
		sortedList = sorted(childProportionMap, key=childProportionMap.__getitem__, reverse=True)
		# random.shuffle(sortedList)
		# print "parentName\t", parentName
		spamNum = 0
		AP = 0
		for index in range(childLen):
			childDocObj = sortedList[index]
			#print childDocObj.m_xProportion,
			if childDocObj.m_trueLabel == 1:
				spamNum += 1
			
				AP += spamNum*1.0/(index+1)
		
		# print spamNum, parentName
		AP = AP/spamNum
		#print "################"
		totalAP += AP
		#print "AP\t",AP,"########"
	
	MAP = totalAP*1.0/totalParentNum
	print "MAP\t", MAP
			
corpusObj = {}

XFile = "testChildXProportion_CZ_fake_v6.txt"
XFile = "testChildXProportion.txt"
loadFile(XFile, corpusObj)
calMAP(corpusObj)	