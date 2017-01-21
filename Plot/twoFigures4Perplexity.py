###plot two proportion 20% and 90%

from matplotlib import pyplot as plt
from scipy.stats import ttest_ind

fig = plt.figure()

ax = fig.add_subplot(121)

x = [20, 40, 60, 80]
handles = []

lda = "1563.610+/-94.191	1385.824+/-62.740	1284.095+/-71.494	1191.013+/-52.857"
lda = lda.split("\t")
y_lda  = []
y_ldaError = []
for i in range(len(lda)):
	item = lda[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_lda.append(meanVal)
	y_ldaError.append(varVal)

lda = ax.errorbar(x, y_lda, y_ldaError, color="r", marker="d", label="LDA")
handles.append(lda)

corrlda = "1638.888+/-87.527	1485.189+/-84.784	1389.655+/-69.013	1306.409+/-51.576"
corrlda = corrlda.split("\t")
y_corrlda  = []
y_corrldaError = []
for i in range(len(corrlda)):
	item = corrlda[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_corrlda.append(meanVal)
	y_corrldaError.append(varVal)

corrlda = ax.errorbar(x, y_corrlda, y_corrldaError, color="b", marker="*", label="CorrLDA")
handles.append(corrlda)

SCTM = "248.550+/-6.710	263.647+/-8.877	272.474+/-8.715	281.743+/-8.821"
SCTM = SCTM.split("\t")
y_sctm  = []
y_sctmError = []
for i in range(len(SCTM)):
	item = SCTM[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_sctm.append(meanVal)
	y_sctmError.append(varVal)

SCTM = ax.errorbar(x, y_sctm, y_sctmError, color="y", marker="s", label="SCTM")
handles.append(SCTM)

cctm = "248.550+/-6.710	263.647+/-8.877	272.474+/-8.715	281.743+/-8.821"
cctm = cctm.split("\t")
y_cctm  = []
y_cctmError = []
for i in range(len(cctm)):
	item = cctm[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_cctm.append(meanVal)
	y_cctmError.append(varVal)

cctm = ax.errorbar(x, y_cctm, y_cctmError, color="m", marker="o", label="CCTM")
handles.append(cctm)

ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
plt.title("perplexity of topic models", fontsize=8)
plt.xlabel("proportion of observed words", fontsize=8)
plt.ylabel("perplexity", fontsize=8)
plt.legend(handles=handles,prop={'size':8}, markerscale=0.8)

ax = fig.add_subplot(122)

x = [40, 60, 80, 100, 150]
handles = []

lda = "1754.011+/-69.005	1560.463+/-51.219	1400.982+/-50.397	 1143.912+/-36.744"
lda = lda.split("\t")
y_lda  = []
y_ldaError = []
for i in range(len(lda)):
	item = lda[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_lda.append(meanVal)
	y_ldaError.append(varVal)

lda = ax.errorbar(x, y_lda, y_ldaError, color="r", marker="d", label="LDA")
handles.append(lda)

corrlda = "4038.237+/-325.253	4544.245	3816.200+/-452.474	3811.403+/-363.772	3772.909"
corrlda = corrlda.split("\t")
y_corrlda  = []
y_corrldaError = []
for i in range(len(corrlda)):
	item = corrlda[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_corrlda.append(meanVal)
	y_corrldaError.append(varVal)

corrlda = ax.errorbar(x, y_corrlda, y_corrldaError, color="b", marker="*", label="CorrLDA")
handles.append(corrlda)

SCTM = ""
SCTM = SCTM.split("\t")
y_sctm  = []
y_sctmError = []
for i in range(len(SCTM)):
	item = SCTM[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_sctm.append(meanVal)
	y_sctmError.append(varVal)

SCTM = ax.errorbar(x, y_sctm, y_sctmError, color="y", marker="s", label="SCTM")
handles.append(SCTM)

cctm = "225.7518	219.604"
cctm = cctm.split("\t")
y_cctm  = []
y_cctmError = []
for i in range(len(cctm)):
	item = cctm[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_cctm.append(meanVal)
	y_cctmError.append(varVal)

cctm = ax.errorbar(x, y_cctm, y_cctmError, color="m", marker="o", label="CCTM")
handles.append(cctm)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
plt.title("Yahoo", fontsize=8)
plt.xlabel("proportion of observed words", fontsize=8)
plt.ylabel("perplexity", fontsize=8)
plt.legend(handles=handles,prop={'size':8}, markerscale=0.8)

fig.set_size_inches([9, 3.4])
fig.savefig("perplexity_tech.png", dpi=400)
plt.show()