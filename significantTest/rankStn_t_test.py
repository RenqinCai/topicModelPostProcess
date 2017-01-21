from scipy.stats import ttest_ind
import numpy as np

ACCTM_C = "0.6217256648	0.6167353687	0.6200537191	0.6138409327	0.6269693229	0.6198218357	0.6113471134	0.6259375451	0.6189104202	0.6315265109"
ACCTM_CZ = "0.6160436887	0.6191414109	0.6255209272	0.6240716553	0.6039431734	0.6137345756	0.6182262002	0.6131480829	0.6138417676	0.6111828514"

# acctmc = "0.5392751496	0.5312739349	0.5338962754	0.5465113179	0.5397573383	0.5409437276	0.5486170325	0.5265733233	0.542270936	0.5317168858"
# acctmcPerplexity1 = acctmc.split("\t")
# acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

# acctmcz = "0.5213677926	0.5272727266	0.5083290616	0.5126436425	0.5274969162	0.521903417	0.5168509145	0.5158633537	0.5117142068	0.530670197"
# acctmczPerplexity1 = acctmcz.split("\t")
# acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]

# ACCTM_CZ= "0.7647	0.6984	0.6923	0.6952	0.7231	0.7058	0.7133	0.7362	0.761	0.739"

ACCTM_CMAP = ACCTM_C.split("\t")
ACCTM_CMAP = [float(i) for i in ACCTM_CMAP]

ACCTM_CZMAP = ACCTM_CZ.split("\t")
ACCTM_CZMAP = [float(i) for i in ACCTM_CZMAP]

print "ACCTM_C avg\t", np.average(ACCTM_CMAP)
print "ACCTM_CZ avg\t", np.average(ACCTM_CZMAP)

(tVal, pVal) = ttest_ind(ACCTM_CMAP, ACCTM_CZMAP)

print "tVal%.3f, pVal%.3f"%(tVal, pVal)


