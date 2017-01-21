from scipy.stats import ttest_ind
import numpy as np 

###1--10%, 2--80%

print "#######################################"
print "#######################################"

lda = "0.5162924303	0.4905355289	0.4454049844	0.4629394749	0.4972963952	0.4877948376	0.5297507788	0.5031597686	0.4879394749	0.489678831	0.4833704198"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

corrlda = "0.4628615932	0.4698	0.4755	0.4619	0.4676	0.4837	0.4976	0.4905	0.5272	0.3982	0.4797"
corrldaPerplexity1 = corrlda.split("\t")
corrldaPerplexity1 = [float(i) for i in corrldaPerplexity1]

acctm = "0.4846573209	0.4392449192	0.4746884735	0.521517579	0.4669225634	0.4849688474	0.4780485091	0.4690071611	0.4553404539	0.4720998368	0.4906319537"
acctmPerplexity1 = acctm.split("\t")
acctmPerplexity1 = [float(i) for i in acctmPerplexity1]

acctmc = "0.5392751496	0.5312739349	0.5338962754	0.5465113179	0.5397573383	0.5409437276	0.5486170325	0.5265733233	0.542270936	0.5317168858"
acctmcPerplexity1 = acctmc.split("\t")
acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

acctmcz = "0.5213677926	0.5272727266	0.5083290616	0.5126436425	0.5274969162	0.521903417	0.5168509145	0.5158633537	0.5117142068	0.530670197"
acctmczPerplexity1 = acctmcz.split("\t")
acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]

LM = "0.453682688	0.453682688	0.453682688	0.453682688	0.453682688	0.453682688	0.453682688	0.453682688	0.453682688	0.453682688	0.453682688"
LM = LM.split("\t")
LM = [float(i) for i in LM]

randomModel = "0.4493584038	0.4288384513	0.4592679128	0.4708024841	0.4694963655	0.4612928349	0.4160102359	0.4155577807	0.4596610295	0.4398642635	0.4463992394"
randomModel = randomModel.split("\t")
randomModel = [float(i) for i in randomModel]

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

(tVal19, pVal19) = ttest_ind(randomModel, acctmPerplexity1)
print tVal19, "\t randomModel vs acctm 20% \t", pVal19, "\t average", np.average(randomModel), "\t", np.average(acctmPerplexity1)

(tVal20, pVal20) = ttest_ind(randomModel, acctmcPerplexity1)
print tVal20, "\t randomModel vs acctmc 20% \t", pVal20, "\t average", np.average(randomModel), "\t", np.average(acctmcPerplexity1)

(tVal21, pVal21) = ttest_ind(randomModel, acctmczPerplexity1)
print tVal21, "\t randomModel vs acctmz 20% \t", pVal21, "\t average", np.average(randomModel), "\t", np.average(acctmczPerplexity1)

(tVal22, pVal22) = ttest_ind(randomModel, corrldaPerplexity1)
print tVal22, "\t randomModel vs corrlda 20% \t", pVal22, "\t average", np.average(randomModel), "\t", np.average(corrldaPerplexity1)


print "#######################################"
print "#######################################"

lda = "0.4759386252	0.5194744508	0.4551846907	0.4328033337	0.4627540424	0.4599948079	0.468246551	0.4404205607	0.4865264798	0.4508789497	0.4973854028"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

corrlda = "0.4771139297	0.4353	0.4687	0.4742	0.4232	0.4517	0.4632	0.4371	0.4562	0.4183	0.4337"
corrldaPerplexity1 = corrlda.split("\t")
corrldaPerplexity1 = [float(i) for i in corrldaPerplexity1]

acctm = "0.5078033337	0.4136444552	0.4580032636	0.4316681501	0.4630102763	0.5014908767	0.4417705088	0.4337561193	0.4837449933	0.4720404984	0.4136444552"
acctmPerplexity1 = acctm.split("\t")
acctmPerplexity1 = [float(i) for i in acctmPerplexity1]

acctmc = "0.4682394708	0.504242694	0.5070204717	0.4541388518	0.4786418929	0.4800956831	0.4116636997	0.4625500668	0.4398308856	0.5032376502	0.4317018651"
acctmcPerplexity1 = acctmc.split("\t")
acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

acctmcz = "0.473164219	0.4628059635	0.4437027147	0.4255451713	0.4222407655	0.4424158137	0.430529595	0.4144451862	0.468858478	0.3917668002	0.4515687583"
acctmczPerplexity1 = acctmcz.split("\t")
acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]

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

(tVal19, pVal19) = ttest_ind(randomModel, acctmPerplexity1)
print tVal19, "\t randomModel vs acctm 20% \t", pVal19, "\t average", np.average(randomModel), "\t", np.average(acctmPerplexity1)

(tVal20, pVal20) = ttest_ind(randomModel, acctmcPerplexity1)
print tVal20, "\t randomModel vs acctmc 20% \t", pVal20, "\t average", np.average(randomModel), "\t", np.average(acctmcPerplexity1)

(tVal21, pVal21) = ttest_ind(randomModel, acctmczPerplexity1)
print tVal21, "\t randomModel vs acctmz 20% \t", pVal21, "\t average", np.average(randomModel), "\t", np.average(acctmczPerplexity1)

(tVal22, pVal22) = ttest_ind(randomModel, corrldaPerplexity1)
print tVal22, "\t randomModel vs corrlda 20% \t", pVal22, "\t average", np.average(randomModel), "\t", np.average(corrldaPerplexity1)

(tVal24, pVal24) = ttest_ind(randomModel, ldaPerplexity1)
print tVal24, "\t randomModel vs lda 20% \t", pVal24, "\t average", np.average(randomModel), "\t", np.average(ldaPerplexity1)

###############################################
###############################################
print "#######################################"
print "#######################################"

lda = "0.440976858	0.5207205567	0.4544058745	0.4228233604	0.465090491	0.4539200415	0.4736092568	0.4502336449	0.4888629283	0.454643228	0.5027369826"
ldaPerplexity1 = lda.split("\t")
ldaPerplexity1 = [float(i) for i in ldaPerplexity1]

corrlda = "0.4609145527	0.4342	0.4182	0.4257	0.4639	0.4455	0.4201	0.4686	0.475	0.438	0.4524"
corrldaPerplexity1 = corrlda.split("\t")
corrldaPerplexity1 = [float(i) for i in corrldaPerplexity1]

acctm = "0.4254784157	0.4800178015	0.4575359739	0.4389890224	0.4588046689	0.5033600356	0.4315012609	0.4455162439	0.4758010681	0.479517134	0.4190961686"
acctmPerplexity1 = [float(i) for i in acctmPerplexity1]

acctmc = "0.5114597241	0.5086448598	0.4609924344	0.4820686842	0.473776146	0.4088599614	0.4534379172	0.4407543391	0.4932576769	0.4298327062	0.4430796618"
acctmcPerplexity1 = acctmc.split("\t")
acctmcPerplexity1 = [float(i) for i in acctmcPerplexity1]

acctmcz = "0.4209612817	0.4621829105	0.4415331553	0.429517134	0.4132064976	0.4551883993	0.43605919	0.4180277407	0.4662883845	0.3933244326	0.4475300401"
acctmczPerplexity1 = acctmcz.split("\t")
acctmczPerplexity1 = [float(i) for i in acctmczPerplexity1]

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

(tVal19, pVal19) = ttest_ind(randomModel, acctmPerplexity1)
print tVal19, "\t randomModel vs acctm 20% \t", pVal19, "\t average", np.average(randomModel), "\t", np.average(acctmPerplexity1)

(tVal20, pVal20) = ttest_ind(randomModel, acctmcPerplexity1)
print tVal20, "\t randomModel vs acctmc 20% \t", pVal20, "\t average", np.average(randomModel), "\t", np.average(acctmcPerplexity1)

(tVal21, pVal21) = ttest_ind(randomModel, acctmczPerplexity1)
print tVal21, "\t randomModel vs acctmz 20% \t", pVal21, "\t average", np.average(randomModel), "\t", np.average(acctmczPerplexity1)

(tVal22, pVal22) = ttest_ind(randomModel, corrldaPerplexity1)
print tVal22, "\t randomModel vs corrlda 20% \t", pVal22, "\t average", np.average(randomModel), "\t", np.average(corrldaPerplexity1)

(tVal23, pVal23) = ttest_ind(randomModel, LM)
print tVal23, "\t randomModel vs LM 20% \t", pVal23, "\t average", np.average(randomModel), "\t", np.average(LM)

(tVal24, pVal24) = ttest_ind(randomModel, ldaPerplexity1)
print tVal24, "\t randomModel vs lda 20% \t", pVal24, "\t average", np.average(randomModel), "\t", np.average(ldaPerplexity1)
