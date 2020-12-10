import matplotlib.pyplot as plt


x_value=[1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(x_value,squares, linewidth=3)
ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square Value", fontsize=24)
ax.tick_params(axis='both', labelsize=14)

plt.show()
