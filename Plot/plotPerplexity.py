from matplotlib import pyplot as plt
from scipy.stats import ttest_ind

x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
perplexityStringMap = {} ##model:string

LDAPer = "5204.540+/-492.478, 4202.553+/-371.116,3679.524+/-270.311, 3268.194+/-144.888, 3164.817+/-238.925, 2966.182+/-320.171, 2768.850+/-315.183, 2681.183+/-132.442, 2462.954+/-203.327 "
perplexityStringMap.setdefault("LDA", LDAPer)

ACCTM_BasePer = "4480.966+/-476.489, 3673.481+/-290.974, 3326.933+/-279.426, 3081.747+/-270.336,2839.539+/-168.873, 2732.133+/-196.081, 2712.290+/-217.955, 2607.951+/-223.711, 2339.577+/-218.902"
perplexityStringMap.setdefault("ACCTM_Base", ACCTM_BasePer)


ACCTM_CPer = "4614.753+/-359.660, 3683.272+/-224.971, 3331.426+/-258.585, 3155.051+/-233.807, 2875.978+/-172.166, 2678.065+/-117.780,  2685.562+/-173.164,2557.271+/-185.938, 2310.575+/-153.590"
perplexityStringMap.setdefault("ACCTM_C", ACCTM_CPer)

ACCTM_C_HardPer = "4600.178+/-363.000, 3658.328+/-354.304, 3362.358+/-321.344, 3064.037+/-202.590, 2999.437+/-195.962, 2712.290+/-217.955,  2639.366+/-165.251,2683.320+/-269.776, 2415.051+/-252.606"
perplexityStringMap.setdefault("ACCTM_C_Hard", ACCTM_C_HardPer)

LDA_ArticlePer_Part = "4452.428+/-405.107, 3286.439+/-367.593, 2819.984+/-281.313, 2458.303+/-235.126, 2418.833+/-259.648, 2231.229+/-232.877, 2219.890+/-166.251, 2144.945+/-167.567, 2034.389+/-171.818"
perplexityStringMap.setdefault("LDA_Article_Part", LDA_ArticlePer_Part)

LDA_ArticlePer = "6039.012+/-748.980, 4697.115+/-352.270, 4142.006+/-399.492, 3744.460+/-202.068,	3423.418+/-195.854,	3311.942+/-273.573,	3147.439+/-271.876,	2980.651+/-249.187,	2648.103+/-187.461"

perplexityStringMap.setdefault("LDA_Article", LDA_ArticlePer)


perplexityMeanMap = {} ##model:value

perplexityErrorMap = {} ##model:error

for model in perplexityStringMap.keys():
	perplexityElement = perplexityStringMap[model]
	perplexityUnit = perplexityElement.strip().split(",")
	for i in range(len(perplexityUnit)):
		perplexityUnitList =perplexityUnit[i].split("+/-")
		perplexity = float(perplexityUnitList[0])
		perplexityError = float(perplexityUnitList[1])

		if model not in perplexityMeanMap.keys():
			perplexityMeanMap.setdefault(model, [])
			perplexityErrorMap.setdefault(model, [])

			perplexityMeanMap[model].append(perplexity)
			perplexityErrorMap[model].append(perplexityError)
		else:
			perplexityMeanMap[model].append(perplexity)
			perplexityErrorMap[model].append(perplexityError)

markerList = ["o", "v", "^", "p", "*", "s"]
colorList = ["r", "b", "y", "m", "k", "sienna"]

# modelList = perplexityMeanMap.keys()
# print modelList

modelList = ["LDA_Article_Part", "LDA_Article", "LDA", "ACCTM_Base", "ACCTM_C", "ACCTM_C_Hard"]

handles = []
i = 0
for model in modelList:
	perplexityList = perplexityMeanMap[model]
	perplexityErrorList = perplexityErrorMap[model]

	perplexity = plt.errorbar(x, perplexityList, perplexityErrorList, marker=markerList[i], label=model, color=colorList[i])
	handles.append(perplexity)
	i += 1
	print i

LDA_ArticleList = perplexityMeanMap["LDA_Article_Part"]
LDAList = perplexityMeanMap["LDA"]

tval,pval = ttest_ind(LDA_ArticleList, LDAList)
print "tVal\t", tval, "\t pVal\t", pval

plt.title("model perplexity")
plt.ylabel("perplexity")
plt.xlabel("observed data in test document(%)")
plt.legend(handles=handles)
plt.show()