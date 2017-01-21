import numpy as np

lda = "0.01	0.11	0.16	0.01	0	0.02	0.05	0.05	0	0	0	0.02	0	0.01	0	0.01	0.03	0	0.01	0.03	0.07	0	0.07	0.05	0	0	0.05	0	0	0.22"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

alpha = 1e-20
entropyVal = 0
for i in ldaPerplexity1:
	line = (alpha+i)/(1+30*alpha*1.0)
	entropyVal += line*np.log(line)

print "entropyVal\t", entropyVal
