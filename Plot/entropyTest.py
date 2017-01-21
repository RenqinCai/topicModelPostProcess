import numpy as np
line = [0.1, 0.9]

entropyVal = 0
for lineUnit in line:
	entropyVal += lineUnit*np.log(lineUnit)

entropyVal = -entropyVal

print 'entropyVal 1\t', entropyVal

line = [1.0/30 for i in range(30)]

entropyVal = 0
for lineUnit in line:
	entropyVal += lineUnit*np.log(lineUnit)

entropyVal = -entropyVal
print 'entropyVal 2\t', entropyVal
