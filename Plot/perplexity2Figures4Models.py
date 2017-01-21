###plot two proportion 20% and 90%
import numpy as np
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

corrlda = ax.errorbar(x, y_corrlda,y_corrldaError, color="b", marker="*", label="Corr-LDA")
handles.append(corrlda)

SCTM = "2222.41536+/-208.6	1995.016168+/-187.59	1833.849664+/-165.65	1742.580363+/-156.75"
SCTM = SCTM.split("\t")
y_sctm  = []
y_sctmError = []
for i in range(len(SCTM)):
	item = SCTM[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_sctm.append(meanVal)
	y_sctmError.append(varVal)

SCTM = ax.errorbar(x, y_sctm, y_sctmError, color="y",marker="s", label="SCTM")
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
major_ticks = np.arange(200,2400, 500)
ax.set_yticks(major_ticks)
# ax.set_yscale('log')
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
plt.ylim([200, 2400])
plt.title("ArsTechnia Science", fontsize=10)
plt.xlabel("number of topics", fontsize=10)
plt.ylabel("perplexity", fontsize=10)
plt.legend(handles=handles,prop={'size':10}, markerscale=0.8)

ax = fig.add_subplot(122)

x = [40, 60, 80, 100, 150]
handles = []

lda = "2087.559+/-109.309	1754.011+/-69.005	1560.463+/-51.219	1400.982+/-50.397	 1143.912+/-36.744"
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

corrlda = "4038.237+/-325.253	4093.704+/-334.952	3816.200+/-452.474	3811.403+/-363.772	3772.909+/-220.210"
corrlda = corrlda.split("\t")
y_corrlda  = []
y_corrldaError = []
for i in range(len(corrlda)):
	item = corrlda[i].split("+/-")
	meanVal = float(item[0])
	varVal = float(item[1])
	y_corrlda.append(meanVal)
	y_corrldaError.append(varVal)

corrlda = ax.errorbar(x, y_corrlda, y_corrldaError, color="b", marker="*", label="Corr-LDA")
handles.append(corrlda)

SCTM = "2994.340834+/-114.28	2768.870717+/-107.315	2622.284926+/-84.89	2487.440267+/-57.86	2282.820002+/-114.28"
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

cctm = "228.222+/-13.786	211.271+/-12.850	203.278+/-10.233	199.664+/-11.096	 197.418+/-6.010"
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
plt.ylim([100, 5000])
plt.xlim([40, 150])
major_ticks = [100, 2000, 3000, 5000]
ax.set_yticks(major_ticks)	
# ax.set_yscale('log')
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
plt.title("Yahoo! News", fontsize=10)
plt.xlabel("number of topics", fontsize=10)
plt.ylabel("perplexity", fontsize=10)
# plt.legend(handles=handles,prop={'size':10}, markerscale=0.8)

# fig.set_size_inches([9,3.4])
# fig.savefig("perplexity_tech_2.png", dpi=400)
plt.show()