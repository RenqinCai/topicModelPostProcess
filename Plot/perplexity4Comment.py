###plot two proportion 20% and 90%
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import ttest_ind

fig = plt.figure()

ax = fig.add_subplot(121)

x = [20, 40, 60, 80]
handles = []

lda = "2332.320+/-135.511	2372.920+/-153.215	2402.682+/-152.236	2433.154+/-192.111"
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

corrlda = "2288.987+/-129.869	2282.149+/-112.774	2269.138+/-145.860	2302.830+/-120.247"
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


cctm = "1543.171+/-64.919	1578.027+/-109.746	1612.004+/-133.136	1648.472+/-101.946"
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
# major_ticks = np.arange(200, 2400, 500)
# ax.set_yticks(major_ticks)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
# plt.ylim([200, 2400])
plt.title("ArsTechnia Science", fontsize=10)
plt.xlabel("number of topics", fontsize=10)
plt.ylabel("perplexity", fontsize=10)
plt.legend(handles=handles,prop={'size':10}, markerscale=0.8)

ax = fig.add_subplot(122)

x = [40, 60, 80, 100, 150]
handles = []

lda = "7323.138+/-588.641	7874.239+/-695.386	8298.437+/-700.450	8199.951+/-802.839	8291.032+/-298.897"
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

corrlda = "4758.881+/-187.040	4830.359+/-177.488	4730.596+/-372.388	4688.513+/-199.349	4709.390+/-259.650"
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


cctm = "4793.266+/-217.775	4944.026+/-362.889	4990.550+/-401.363	5172.790+/-419.117	5468.680+/-484.872"
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
# plt.ylim([100, 5000])
# major_ticks = [100, 2000, 3000, 5000]
# ax.set_yticks(major_ticks)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
plt.title("Yahoo! News", fontsize=10)
plt.xlabel("number of topics", fontsize=10)
plt.ylabel("perplexity", fontsize=10)
plt.legend(handles=handles,prop={'size':10}, markerscale=0.8)

# fig.set_size_inches([9,3.4])
# fig.savefig("perplexity_tech_2.png", dpi=400)
plt.show()