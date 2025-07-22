import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
plt.style.use("bmh")

values = list(range(1, 6))
cubes = [value**3 for value in values]

fig, ax = plt.subplots(1, 2, figsize=(15, 5))

ax[0].plot(values, cubes)
ax[0].set_title("Cubes using plot")

ax[1].scatter(values, cubes, c=cubes, cmap=plt.cm.GnBu, s=200)
ax[1].set_title("Cubes using scatter")
plt.show()
