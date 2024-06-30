import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.plot([1.1, 1.2, 1.4, 1.5, 1.5, 2, 3, 3.1, 3.3, 3.3, 3.4])
ax.tick_params(labelbottom=False, labelleft=False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.text(3, 2.5, "breakthrough")
plt.xlabel('time')   
plt.ylabel('progress')
plt.show()