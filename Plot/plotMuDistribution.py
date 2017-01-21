###plot mu distribution

import matplotlib.pyplot as plt
import numpy as np

fileName = "childMu_2.txt"
f = open(fileName)

muList = []

for rawLine in f:
	line = rawLine.strip().split()
	childName = (line[0])
	muVal = float(line[1])
	muList.append(muVal)


###plot cdf
# counts, bin_edges = np.histogram(muList, bins=20, normed=True)
# dx = bin_edges[1]-bin_edges[0]
# cdf = np.cumsum(counts)*dx
# print cdf
# plt.plot(bin_edges[1:], cdf)
# plt.title("mu")
# plt.show()


####plot histogram
maxVal = max(muList)
minVal = min(muList)
print "max mu\t", maxVal, "min val\t", minVal, "avg val\t", np.average(muList)
plt.hist(muList, bins=20, normed=False)
plt.title("mu distribution")
plt.xlabel("value of mu")
plt.ylabel("count")
plt.show()