import matplotlib.pyplot as plt

a = [0.01, 0.05, 0.1, 0.5, 0.8, 0.9, 0.99,1]
# b = [16.68-5.51, 16.68-5.18, 16.68-5.12, 16.68-4.91, 16.68-4.87, 16.68-4.57, 16.68-2.37, 16.68]
# b = [i/16.68 for i in b]
b=[0.670, 0.689, 0.693, 0.706, 0.708, 0.726, 0.858, 1.0]
print b 

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(a, b, "r-", a, b, "o")
plt.title("CDF of the probability sampling from phi^p")
plt.xlabel("probability")
plt.ylabel("proportion")

for xy in zip(a,b):
	ax.annotate('(%s, %s)'%xy, xy=xy, textcoords="data")

plt.show()