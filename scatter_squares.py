import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

plt.style.use("seaborn-v0_8")

values = list(range(1, 1001))
squares = [value**2 for value in values]

fig, ax = plt.subplots()

# Pass simple x and y values to plot
# ax.scatter(2, 4, s=200)

# ax.scatter(values, squares, color="#693466", s=10)

ax.scatter(values, squares, c=squares, cmap=plt.cm.GnBu, s=10)

# Set chart title and label size
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of the value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis
# .axis(x_min, x_max, y_min, y_max)
ax.axis((0, 1100, 0, 1_100_000))
ax.ticklabel_format(style="plain")


plt.savefig("squares_scatter_plot.png", bbox_inches="tight", dpi=600)
plt.show()
