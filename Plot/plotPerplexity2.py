###plot two proportion 20% and 90%

from matplotlib import pyplot as plt
from scipy.stats import ttest_ind

x = [20, 90]

handles = []

lda = "5878.168+/-557.880	3306.517+/-375.875"
lda = lda.split("\t")
y_lda  = []
y_ldaError = []
for i in range(len(lda)):
	item = lda[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_lda.append(meanVal)
	y_ldaError.append(varVal)

lda = plt.errorbar(x, y_lda, y_ldaError, color="r", marker="o", label="lda")
handles.append(lda)

corrlda = "2628.399+/-210.986	2463.210+/-250.096"
corrlda = corrlda.split("\t")
y_corrlda  = []
y_corrldaError = []
for i in range(len(corrlda)):
	item = corrlda[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_corrlda.append(meanVal)
	y_corrldaError.append(varVal)

corrlda = plt.errorbar(x, y_corrlda, y_corrldaError, color="b", marker="o", label="corrlda")
handles.append(corrlda)

acctm = "5924.395+/-546.356	3112.229+/-500.193"
acctm = acctm.split("\t")
y_acctm  = []
y_acctmError = []
for i in range(len(acctm)):
	item = acctm[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_acctm.append(meanVal)
	y_acctmError.append(varVal)

acctm = plt.errorbar(x, y_acctm, y_acctmError, color="y", marker="o", label="acctm")
handles.append(acctm)

acctmc = "6018.191+/-454.308	2810.404+/-284.702"
acctmc = acctmc.split("\t")
y_acctmc  = []
y_acctmcError = []
for i in range(len(acctmc)):
	item = acctmc[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_acctmc.append(meanVal)
	y_acctmcError.append(varVal)

acctmc = plt.errorbar(x, y_acctmc, y_acctmcError, color="m", marker="o", label="acctmc")
handles.append(acctmc)

acctmcz = "2602.059+/-146.348	2318.563+/-269.640"
acctmcz = acctmcz.split("\t")
y_acctmcz  = []
y_acctmczError = []
for i in range(len(acctmcz)):
	item = acctmcz[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_acctmcz.append(meanVal)
	y_acctmczError.append(varVal)

acctmcz = plt.errorbar(x, y_acctmcz, y_acctmczError, color="k", marker="o", label="acctmcz")
handles.append(acctmcz)

# plt.plot(x, y_lda, 'ro', label="lda")
# plt.legend()
# plt.show()

# lda, = plt.plot(x, y_lda, "ro", label="lda")
# handles.append(lda)

# corrlda, = plt.plot(x, y_corrlda, "bo", label="corrlda")
# handles.append(corrlda)

# acctm, = plt.plot(x, y_acctm, label="acctm", color='y', marker="o")
# handles.append(acctm)

# acctmc, = plt.plot(x, y_acctmc, label="acctmc", color='k', marker="o")
# handles.append(acctmc)

# acctmcz, = plt.plot(x, y_acctmcz, label="acctmcz", color='sienna', marker="o")
# handles.append(acctmcz)

plt.title("perplexity of topic models")
plt.xlabel("proportion of observed words")
plt.ylabel("perplexity")
plt.legend(handles=handles)


plt.show()
