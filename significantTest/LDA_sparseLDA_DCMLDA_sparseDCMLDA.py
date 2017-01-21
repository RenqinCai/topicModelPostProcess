from scipy.stats import ttest_ind
import numpy as np 

###1--10%, 2--80%

print "#######################################"
print "#######################################"

lda = "0.6587116454	0.6701417549	0.6560200969	0.6540462946	0.6673604881	0.6625336444	0.6537412525	0.6677731922	0.6750583169	0.6774448233"
lda_accuracy = lda.split("\t")
lda_accuracy = [float(i) for i in lda_accuracy]

wordFeature = "0.677439623	0.6810720597	0.6689181229	0.6890830552	0.6678774789	0.6727469075	0.6827017475	0.6805222855	0.681425486	0.6811309641"
wordFeature_accuracy = wordFeature.split("\t")
wordFeature_accuracy = [float(i) for i in wordFeature_accuracy]

DCMLDA = "0.6474430289	0.6714157545	0.6801184281	0.6886416652	0.6812129912	0.6726179795	0.6893594114	0.6760272744	0.6595370537	0.7206352055"
DCMLDA_accuracy = DCMLDA.split("\t")
DCMLDA_accuracy = [float(i) for i in DCMLDA_accuracy]

sparseLDA = "0.7090615467	0.7066391531	0.7119684192	0.7352413422	0.7105867576	0.7459895927	0.7166517136	0.7266822178	0.7105867576	0.7257670913"
sparseLDA_accuracy = sparseLDA.split("\t")
sparseLDA_accuracy = [float(i) for i in sparseLDA_accuracy]

sparseDCMLDA = "0.6560739278664991	0.6473712542616183	0.6496321550331957	0.6479275076260542	0.6518033375201865	0.6550511394222143	0.6753992463664096	0.6723129373766374	0.6479275076260542"
sparseDCMLDA_accuracy = sparseDCMLDA.split("\t")
sparseDCMLDA_accuracy = [float(i) for i in sparseDCMLDA_accuracy]


(tVal10, pVal10) = ttest_ind(lda_accuracy, sparseLDA_accuracy)
print "\t lda vs sparseLDA \t(tVal", tVal10, ",\tpVal", pVal10, ")\t average", np.average(lda_accuracy), "\t", np.average(sparseLDA_accuracy)

print "#######################################"

(tVal11, pVal11) = ttest_ind(DCMLDA_accuracy, sparseDCMLDA_accuracy)
print "\t DCMLDA vs sparseDCMLDA \t(tVal", tVal11, ",\tpVal", pVal11, ")\t average", np.average(DCMLDA_accuracy), "\t", np.average(sparseDCMLDA_accuracy)

print "#######################################"

(tVal12, pVal12) = ttest_ind(lda_accuracy, DCMLDA_accuracy)
print "\t lda vs DCMLDA \t(tVal",tVal12,  ",\tpVal", pVal12, ")\t average", np.average(lda_accuracy), "\t", np.average(DCMLDA_accuracy)

print "#######################################"

(tVal13, pVal13) = ttest_ind(sparseLDA_accuracy, sparseDCMLDA_accuracy)
print "\t sparseLDA vs sparseDCMLDA \t(tVal",tVal13, ",\tpVal", pVal13, ")\t average", np.average(sparseLDA_accuracy), "\t", np.average(sparseDCMLDA_accuracy)

print "#######################################"

(tVal14, pVal14) = ttest_ind(lda_accuracy, wordFeature_accuracy)
print "\t lda vs wordFeature \t(tVal", tVal14, ",\tpVal", pVal14, ")\t average", np.average(lda_accuracy), "\t", np.average(wordFeature_accuracy)

print "#######################################"

(tVal15, pVal15) = ttest_ind(DCMLDA_accuracy, wordFeature_accuracy)
print "\t DCMLDA vs wordFeature \t(tVal",tVal15,  ",\tpVal", pVal15, ")\t average", np.average(DCMLDA_accuracy), "\t", np.average(wordFeature_accuracy)

print "#######################################"
print "#######################################"
