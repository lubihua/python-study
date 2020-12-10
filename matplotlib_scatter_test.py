import matplotlib.pyplot as plt

x_value = range(1,5000)
y_value = [x**3 for x in x_value]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x_value,y_value,c=x_value,cmap=plt.cm.Reds,s=10)
plt.show()
