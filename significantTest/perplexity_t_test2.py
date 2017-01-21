from scipy.stats import ttest_ind
import numpy as np 

###1--10%, 2--80%



lda = "910.731	846.435	808.367	894.536	913.594	1027.867	992.233	982.272	1037.369	972.233"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

print np.mean(ldaPerplexity1)

corrlda = "1001.016	923.678	941.035	973.371	975.712	1131.698	1016.086	896.743	833.701	1029.503"
corrldaPerplexity1 = corrlda.split("\t")
corrldaPerplexity1 = [float(i) for i in corrldaPerplexity1]

print np.mean(corrldaPerplexity1)
(tVal10, pVal10) = ttest_ind(ldaPerplexity1, corrldaPerplexity1)
print tVal10, "\t DCMCorrLDA vs SCTM 20% \t", pVal10



acctm = "6324.666	5238.256	6175.371	5494.178	7018.791	6178.027	6168.456	5886.393	5688.116	5071.693"
acctmPerplexity1 = acctm.split("\t")
acctmPerplexity1 = [float(i) for i in acctmPerplexity1]

acctmc = "5882.665	6082.973	5755.444	5894.649	6305.495	5767.445	7045.238	5932.894	5203.607	6311.496"
acctmcPerplexity1 = acctmc.split("\t")
acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

acctmcz = "2418.374	2707.807	2761.191	2519.365	2390.034	2390.034	2662.6	2560.392	2884.636	2519.221";
acctmczPerplexity1 = acctmcz.split("\t")
acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]


(tVal10, pVal10) = ttest_ind(corrldaPerplexity1, acctmczPerplexity1)
print tVal10, "\t corrlda vs acctmcz 20% \t", pVal10

(tVal11, pVal11) = ttest_ind(ldaPerplexity1, acctmPerplexity1)
print tVal11, "\t lda vs acctm 20% \t", pVal11

(tVal12, pVal12) = ttest_ind(ldaPerplexity1, acctmcPerplexity1)
print tVal12, "\t lda vs acctmc 20% \t", pVal12

(tVal13, pVal13) = ttest_ind(ldaPerplexity1, acctmczPerplexity1)
print tVal13, "\t lda vs acctmcz 20% \t", pVal13

(tVal14, pVal14) = ttest_ind(acctmPerplexity1, acctmczPerplexity1)
print tVal14, "\t acctm vs acctmcz 20% \t", pVal14

(tVal15, pVal15) = ttest_ind(acctmcPerplexity1, acctmczPerplexity1)
print tVal15, "\t acctmc vs acctmcz 20% \t", pVal15

(tVal16, pVal16) = ttest_ind(acctmPerplexity1, acctmcPerplexity1)
print tVal16, "\t acctm vs acctmc 20% \t", pVal16

(tVal17, pVal17) = ttest_ind(corrldaPerplexity1, ldaPerplexity1)
print tVal17, "\t corrlda vs lda 20% \t", pVal17


lda = "3438.466	3244.523	2791.649	2918.671	4057.431	3700.888	3153.789	3426.829	3466.146	2866.775"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

corrlda = "2518.37	2440.162	2719.683	2740.862	2822.634	3167.415	2591.829	2371.179	2909.314	2606.224"
corrldaPerplexity1 = corrlda.split("\t")
corrldaPerplexity1 = [float(i) for i in corrldaPerplexity1]

acctm = "2342.3	3277.637	4078.22	2880.274	2698.128	3352.669	3203.365	3619.703	2484.29	3185.704"
acctmPerplexity1 = acctm.split("\t")
acctmPerplexity1 = [float(i) for i in acctmPerplexity1]

acctmc = "2185.481	3319.428	2895.209	3083.53	2863.583	2645.011	2775.595	2905.15	2817.392	2613.66"
acctmcPerplexity1 = acctmc.split("\t")
acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

acctmcz = "2513.241	2462.930	2554.896	2036.244	2792.613	2255.986	1880.408	 2687.309	1887.917	2254.668"
acctmczPerplexity1 = acctmcz.split("\t")
acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]


(tVal10, pVal10) = ttest_ind(corrldaPerplexity1, acctmczPerplexity1)
print tVal10, "\t corrlda vs acctmcz 90% \t", pVal10

(tVal11, pVal11) = ttest_ind(ldaPerplexity1, acctmPerplexity1)
print tVal11, "\t lda vs acctm 90% \t", pVal11

(tVal12, pVal12) = ttest_ind(ldaPerplexity1, acctmcPerplexity1)
print tVal12, "\t lda vs acctmc 90% \t", pVal12

(tVal13, pVal13) = ttest_ind(ldaPerplexity1, acctmczPerplexity1)
print tVal13, "\t lda vs acctmcz 90% \t", pVal13

(tVal14, pVal14) = ttest_ind(acctmPerplexity1, acctmczPerplexity1)
print tVal14, "\t acctm vs acctmcz 90% \t", pVal14

(tVal15, pVal15) = ttest_ind(acctmcPerplexity1, acctmczPerplexity1)
print tVal15, "\t acctmc vs acctmcz 90% \t", pVal15

(tVal16, pVal16) = ttest_ind(acctmPerplexity1, acctmcPerplexity1)
print tVal16, "\t acctm vs acctmc 90% \t", pVal16

(tVal17, pVal17) = ttest_ind(corrldaPerplexity1, ldaPerplexity1)
print tVal17, "\t corrlda vs lda 90% \t", pVal17
