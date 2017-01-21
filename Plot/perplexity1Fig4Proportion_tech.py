###plot two proportion 20% and 90%

from matplotlib import pyplot as plt
from scipy.stats import ttest_ind

x = [30, 50, 60, 80]

handles = []

lda = "2569.245+/-225.562	2350.163+/-101.90	2272.443+/-89.30	2272.443+/-89.306"
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

corrlda = "2943.343+/-186.989	2389.915+/-139.099	2258.150+/-121.514	2151.644+/-145.150"
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

priorCorrLDA = "2967.259+/-270.566	2633.816+/-153.915	2507.705+/-178.388	2323.492+/-130.471"
priorCorrLDA = priorCorrLDA.split("\t")
y_priorCorrDCMLDA  = []
y_priorCorrDCMLDAError = []
for i in range(len(priorCorrLDA)):
	item = priorCorrLDA[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_priorCorrDCMLDA.append(meanVal)
	y_priorCorrDCMLDAError.append(varVal)

priorCorrLDA = plt.errorbar(x, y_priorCorrDCMLDA, y_priorCorrDCMLDAError, color="g", marker="o", label="priorCorrLDA")
handles.append(priorCorrLDA)

corrDCMLDA = "1120.566+/-44.739	974.965+/-57.052	904.933+/-38.894	812.048+/-42.923"
corrDCMLDA = corrDCMLDA.split("\t")
y_corrDCMLDA  = []
y_corrDCMLDAError = []
for i in range(len(corrDCMLDA)):
	item = corrDCMLDA[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_corrDCMLDA.append(meanVal)
	y_corrDCMLDAError.append(varVal)

corrDCMLDA = plt.errorbar(x, y_corrDCMLDA, y_corrDCMLDAError, color="y", marker="o", label="corrDCMLDA")
handles.append(corrDCMLDA)

x_sctm = [50, 60, 80]
sctm = "879.04095024 +/- 36.1888360365	726.656578578 +/- 31.3201179989	495.666540089 +/- 16.3030350396"
sctm = sctm.split("\t")
y_sctm  = []
y_sctmError = []
for i in range(len(sctm)):
	item = sctm[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_sctm.append(meanVal)
	y_sctmError.append(varVal)

sctm = plt.errorbar(x_sctm, y_sctm, y_sctmError, color="m", marker="o", label="sctm")
handles.append(sctm)

CCTM = "1141.683+/-64.406	968.812+/-67.901	903.702+/-46.231	810.686+/-49.366"
CCTM = CCTM.split("\t")
y_CCTM  = []
y_CCTMError = []
for i in range(len(CCTM)):
	item = CCTM[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_CCTM.append(meanVal)
	y_CCTMError.append(varVal)

CCTM = plt.errorbar(x, y_CCTM, y_CCTMError, color="k", marker="o", label="CCTM")
handles.append(CCTM)

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

plt.title("perplexity of topic models in ArsTechnica dataset")
plt.xlabel("proportion of observed words of documents in testing corpus")
plt.ylabel("perplexity")
plt.legend(handles=handles)


plt.show()
