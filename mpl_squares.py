"""
- Most of the matplots functionality is in pyplot
- squares is a list holding the actual data
- fig is the entire canvas on which plots will be displayed
- ax is an axes/subplot that will be displayed on the fig canvas
- subplots() allows us to generate one or more plots in the same collection of plots generated. It allows you generate mutiple plots on same canvas
- plot() tries to plot the data it is given
"""

import matplotlib
import matplotlib.pyplot as plt

# The line below is optional, since I'm using a terminal to execute Im using this, otherwise no need
matplotlib.use("TkAgg")

input_values = list(range(1, 6))
squares = [value**2 for value in range(1, 6)]

# Style
plt.style.use("fivethirtyeight")

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Sqaure Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of the value", fontsize=14)

# Set the size of the tick labels
ax.tick_params(labelsize=14)

plt.show()
