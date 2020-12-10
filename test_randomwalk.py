import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
point_number = range(rw.num_point)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_value, rw.y_value, c=point_number, cmap=plt.cm.Blues, s=15, edgecolors='none')
ax.scatter(0, 0, c='green', s=100, edgecolors='none')
ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', s=100,edgecolors='none')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
