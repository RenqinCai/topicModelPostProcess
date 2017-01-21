from scipy.stats import ttest_ind
import numpy as np 

###1--10%, 2--80%


LDAPerplexity1 = [2652.739,2826.449, 2353.550, 2710.085, 2617.009, 2718.730, 2719.481, 2600.242, 2796.071,2817.472]

LDAArticle1 = [2979.956, 3147.118, 2828.492, 2861.312, 3472.010, 2811.031, 3234.388, 3011.774, 2512.447, 2947.979]

ACCTM_BasePerplexity1 = [2448.941, 2353.653, 3178.733, 2587.098, 2583.082, 2353.173, 2567.313, 2631.548, 2644.759, 2731.210]

HardPerplexity1 = [2386.059, 2428.471, 3004.444, 2880.590, 2915.360,2708.010,2306.746, 2885.318, 2347.489, 2970.716]



LDAPerplexity2 = [5084.235, 5056.168, 5736.533, 6305.298, 5126.044, 5299.694, 4802.055, 5392.617, 4648.176, 4594.583]

LDAArticle2 = [5606.643, 7677.547, 5460.473, 4996.635, 6558.341, 5818.603, 6457.249, 5741.603, 5430.274, 6642.747]

ACCTM_BasePerplexity2 = [5545.984, 4116.029, 4797.676, 4406.896, 3704.152, 4373.372, 4447.570, 4625.439, 4746.868, 4045.677]

HardPerplexity2 = [4269.604 , 4420.990, 4860.199, 5101.776, 4683.923,  5025.073,3983.238, 4255.735, 4426.660, 4974.579]

(tVal10, pVal10) = ttest_ind(HardPerplexity1, LDAPerplexity1)
(tVal11, pVal11) = ttest_ind(LDAArticle1, LDAPerplexity1)
(tVal12, pVal12) = ttest_ind(ACCTM_BasePerplexity1, HardPerplexity1)


(tVal20, pVal20) = ttest_ind(HardPerplexity2, LDAPerplexity2)
(tVal21, pVal21) = ttest_ind(LDAArticle2, LDAPerplexity2)
(tVal22, pVal22) = ttest_ind(ACCTM_BasePerplexity2, HardPerplexity2)


# print np.average(HardPerplexity1)
# print np.average(LDAPerplexity1)

# print np.average(LDAArticle1)

# print np.average(LDAArticle2)
# print np.average(LDAPerplexity2)

print tVal10, "\t10\t", pVal10

print tVal11, "\t11\t", pVal11

print tVal12, "\t12\t", pVal12

print tVal20, "\t20\t", pVal20

print tVal21, "\t21\t", pVal21

print tVal22, "\t22\t", pVal22