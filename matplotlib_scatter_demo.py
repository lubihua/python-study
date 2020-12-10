import matplotlib.pyplot as plt

x_value = range(1, 1000)
y_value = [x ** 2 for x in x_value]

plt.style.use("seaborn")
fig, ax = plt.subplots()
#ax.scatter(x_value, y_value, s=10, c='red')
ax.scatter(x_value, y_value, c=x_value, cmap=plt.cm.Blues,s=10)
#ax.axis([0, 1100, 0, 1100000])
#plt.show()
plt.savefig("text_folder/scatter_1.png")
