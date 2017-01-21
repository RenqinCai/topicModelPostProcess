from scipy.stats import ttest_ind
import numpy as np 

###1--10%, 2--80%

print "#######################################"
print "#######################################"

lda = "0.6217256648	0.6167353687	0.6200537191	0.6138409327	0.6269693229	0.6198218357	0.6113471134	0.6259375451	0.6189104202	0.6315265109"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

corrlda = "0.526	0.524	0.522	0.536	0.522	0.526	0.527	0.524	0.522	0.513"
corrldaPerplexity1 = corrlda.split("\t")
corrldaPerplexity1 = [float(i) for i in corrldaPerplexity1]

acctm = "0.6231232238	0.6360557743	0.6324370248	0.6281603729	0.62364396	0.6373253167	0.6213803333	0.6301724413	0.6289640792	0.6200305329"
acctmPerplexity1 = acctm.split("\t")
acctmPerplexity1 = [float(i) for i in acctmPerplexity1]

acctmc = "0.6160436887	0.6191414109	0.6255209272	0.6240716553	0.6039431734	0.6137345756	0.6182262002	0.6131480829	0.6138417676	0.6111828514"
acctmcPerplexity1 = acctmc.split("\t")
acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

acctmcz = "0.5213677926	0.5272727266	0.5083290616	0.5126436425	0.5274969162	0.521903417	0.5168509145	0.5158633537	0.5117142068	0.530670197";
acctmczPerplexity1 = acctmcz.split("\t")
acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]

LM = "0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961"
LM = LM.split("\t")
LM = [float(i) for i in LM]

(tVal10, pVal10) = ttest_ind(corrldaPerplexity1, acctmczPerplexity1)
print tVal10, "\t corrlda vs acctmcz 20% \t", pVal10, "\t average", np.average(corrldaPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal11, pVal11) = ttest_ind(ldaPerplexity1, acctmPerplexity1)
print tVal11, "\t lda vs acctm 20% \t", pVal11, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmPerplexity1)

(tVal12, pVal12) = ttest_ind(ldaPerplexity1, acctmcPerplexity1)
print tVal12, "\t lda vs acctmc 20% \t", pVal12, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmcPerplexity1)

(tVal13, pVal13) = ttest_ind(ldaPerplexity1, acctmczPerplexity1)
print tVal13, "\t lda vs acctmcz 20% \t", pVal13, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal14, pVal14) = ttest_ind(acctmPerplexity1, acctmczPerplexity1)
print tVal14, "\t acctm vs acctmcz 20% \t", pVal14, "\t average", np.average(acctmPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal15, pVal15) = ttest_ind(acctmcPerplexity1, acctmczPerplexity1)
print tVal15, "\t acctmc vs acctmcz 20% \t", pVal15, "\t average", np.average(acctmcPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal16, pVal16) = ttest_ind(acctmPerplexity1, acctmcPerplexity1)
print tVal16, "\t acctm vs acctmc 20% \t", pVal16, "\t average", np.average(acctmPerplexity1), "\t", np.average(acctmcPerplexity1)

(tVal17, pVal17) = ttest_ind(corrldaPerplexity1, ldaPerplexity1)
print tVal17, "\t corrlda vs lda 20% \t", pVal17, "\t average", np.average(corrldaPerplexity1), "\t", np.average(ldaPerplexity1)

(tVal18, pVal18) = ttest_ind(LM, ldaPerplexity1)
print tVal18, "\t LM vs lda 20% \t", pVal18, "\t average", np.average(LM), "\t", np.average(ldaPerplexity1)

print "#######################################"
print "#######################################"

lda = "0.7456348238	0.7465724912	0.7278737575	0.7451871065	0.744998362	0.7363384332	0.7453425445	0.7411697385	0.7459527706	0.7427893685"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

corrlda = "0.762	0.76	0.765	0.763	0.765	0.76	0.763	0.762	0.761	0.765"
corrldaPerplexity1 = corrlda.split("\t")
corrldaPerplexity1 = [float(i) for i in corrldaPerplexity1]

acctm = "0.7426239462	0.7497301058	0.7461798286	0.7431423706	0.7481059607	0.7452324614	0.7462814826	0.7516887819	0.7499687763	0.7392424642"
acctmPerplexity1 = acctm.split("\t")
acctmPerplexity1 = [float(i) for i in acctmPerplexity1]

acctmc = "0.7078026657	0.7083086397	0.7093317612	0.7067795907	0.7121796779	0.7065874338	0.70917613	0.7102863001	0.7133854941	0.708568252"
acctmcPerplexity1 = acctmc.split("\t")
acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

acctmcz = "0.7389425949	0.7316838436	0.7285191694	0.7296792042	0.7318090347	0.7338748053	0.7303247675	0.7242702508	0.7307268146	0.7332131728"
acctmczPerplexity1 = acctmcz.split("\t")
acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]

LM = "0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961"
LM = LM.split("\t")
LM = [float(i) for i in LM]

(tVal10, pVal10) = ttest_ind(corrldaPerplexity1, acctmczPerplexity1)
print tVal10, "\t corrlda vs acctmcz 90% \t", pVal10, "\t average", np.average(corrldaPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal11, pVal11) = ttest_ind(ldaPerplexity1, acctmPerplexity1)
print tVal11, "\t lda vs acctm 90% \t", pVal11, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmPerplexity1)

(tVal12, pVal12) = ttest_ind(ldaPerplexity1, acctmcPerplexity1)
print tVal12, "\t lda vs acctmc 90% \t", pVal12, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmcPerplexity1)

(tVal13, pVal13) = ttest_ind(ldaPerplexity1, acctmczPerplexity1)
print tVal13, "\t lda vs acctmcz 90% \t", pVal13, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal14, pVal14) = ttest_ind(acctmPerplexity1, acctmczPerplexity1)
print tVal14, "\t acctm vs acctmcz 90% \t", pVal14, "\t average", np.average(acctmPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal15, pVal15) = ttest_ind(acctmcPerplexity1, acctmczPerplexity1)
print tVal15, "\t acctmc vs acctmcz 90% \t", pVal15, "\t average", np.average(acctmcPerplexity1), "\t", np.average(acctmczPerplexity1)


(tVal16, pVal16) = ttest_ind(acctmPerplexity1, acctmcPerplexity1)
print tVal16, "\t acctm vs acctmc 90% \t", pVal16, "\t average", np.average(acctmPerplexity1), "\t", np.average(acctmcPerplexity1)

(tVal17, pVal17) = ttest_ind(corrldaPerplexity1, ldaPerplexity1)
print tVal17, "\t corrlda vs lda 90% \t", pVal17, "\t average", np.average(corrldaPerplexity1), "\t", np.average(ldaPerplexity1)

(tVal18, pVal18) = ttest_ind(LM, ldaPerplexity1)
print tVal18, "\t LM vs lda 20% \t", pVal18, "\t average", np.average(LM), "\t", np.average(ldaPerplexity1)

###############################################
###############################################
print "#######################################"
print "#######################################"

lda = "0.7386672354	0.7456629794	0.7455997794	0.7431113883	0.7357732155	0.7439922509	0.7464998179	0.7426021641	0.7267587352	0.7386672354"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

corrlda = "0.765	0.762	0.761	0.763	0.76	0.764	0.762	0.765	0.759	0.761"
corrldaPerplexity1 = corrlda.split("\t")
corrldaPerplexity1 = [float(i) for i in corrldaPerplexity1]

acctm = "0.7413178689	0.7482894331	0.7464921718	0.7427737015	0.747096661	0.7421546126	0.7456594748	0.7500498345	0.7482813368	0.7370267033"
acctmPerplexity1 = acctm.split("\t")
acctmPerplexity1 = [float(i) for i in acctmPerplexity1]

acctmc = "0.7086100671	0.7091431534	0.7102044136	0.7073522578	0.7104992976	0.7056915455	0.7103323295	0.7113360205	0.7127736493	0.7103206416"
acctmcPerplexity1 = acctmc.split("\t")
acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

acctmcz = "0.739077787	0.7321739736	0.7311427564	0.7243528991	0.7322678252	0.7362939904	0.7327027122	0.7310280172	0.7278835501	0.732613951"
acctmczPerplexity1 = acctmcz.split("\t")
acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]

LM = "0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961	0.767800961"
LM = LM.split("\t")
LM = [float(i) for i in LM]

(tVal10, pVal10) = ttest_ind(corrldaPerplexity1, acctmczPerplexity1)
print tVal10, "\t corrlda vs acctmcz 90% \t", pVal10, "\t average", np.average(corrldaPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal11, pVal11) = ttest_ind(ldaPerplexity1, acctmPerplexity1)
print tVal11, "\t lda vs acctm 90% \t", pVal11, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmPerplexity1)

(tVal12, pVal12) = ttest_ind(ldaPerplexity1, acctmcPerplexity1)
print tVal12, "\t lda vs acctmc 90% \t", pVal12, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmcPerplexity1)

(tVal13, pVal13) = ttest_ind(ldaPerplexity1, acctmczPerplexity1)
print tVal13, "\t lda vs acctmcz 90% \t", pVal13, "\t average", np.average(ldaPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal14, pVal14) = ttest_ind(acctmPerplexity1, acctmczPerplexity1)
print tVal14, "\t acctm vs acctmcz 90% \t", pVal14, "\t average", np.average(acctmPerplexity1), "\t", np.average(acctmczPerplexity1)

(tVal15, pVal15) = ttest_ind(acctmcPerplexity1, acctmczPerplexity1)
print tVal15, "\t acctmc vs acctmcz 90% \t", pVal15, "\t average", np.average(acctmcPerplexity1), "\t", np.average(acctmczPerplexity1)


(tVal16, pVal16) = ttest_ind(acctmPerplexity1, acctmcPerplexity1)
print tVal16, "\t acctm vs acctmc 90% \t", pVal16, "\t average", np.average(acctmPerplexity1), "\t", np.average(acctmcPerplexity1)

(tVal17, pVal17) = ttest_ind(corrldaPerplexity1, ldaPerplexity1)
print tVal17, "\t corrlda vs lda 90% \t", pVal17, "\t average", np.average(corrldaPerplexity1), "\t", np.average(ldaPerplexity1)

(tVal18, pVal18) = ttest_ind(LM, ldaPerplexity1)
print tVal18, "\t LM vs lda 20% \t", pVal18, "\t average", np.average(LM), "\t", np.average(ldaPerplexity1)

