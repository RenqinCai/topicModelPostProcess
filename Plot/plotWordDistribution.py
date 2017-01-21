import matplotlib.pyplot as plt
import numpy as np

fileName = "fv_1gram_stat_topicmodel_Tech.txt"
f = open(fileName)

DFList = []
TTFList = []

for rawLine in f:
	line = rawLine.strip().split()
	DFVal = int(line[1])
	TTFVal = int(line[6])
	DFList.append(DFVal)
	TTFList.append(TTFVal)

# counts, bin_edges = np.histogram(DFList, bins=20, normed=True)

# dx = bin_edges[1]-bin_edges[0]
# cdf = np.cumsum(counts)*dx
# print cdf
# plt.plot(bin_edges[1:], cdf)
# plt.title("DF")
# plt.show()


####plot histogram
bins = 50
plt.hist(TTFList, bins=bins)
plt.title("TTF distribution")
plt.xlabel("value of TTF")
plt.ylabel("count")
plt.show()


wordNum = len(DFList)
wordIndexList = [i for i in range(wordNum)]

print "maximum DF\t", max(DFList), "minimum DF\t", min(DFList), "average DF\t", np.average(DFList)

print "maximum TTF\t", max(TTFList), "minimum TTF\t", min(TTFList), "average TTF\t", np.average(TTFList)
# plt.hist(DFList, bins=20)
# plt.hist(TTFList, bins=20)

# plt.plot(wordIndexList, DFList, 'r-', wordIndexList, TTFList, 'b--')
# plt.plot(wordIndexList, TTFList, "b--")
# plt.show()