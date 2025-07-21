import matplotlib.pyplot as plt
import matplotlib
from random_walk import RandomWalk

matplotlib.use("TkAgg")

# Make a random walk, as long as program is active
while True:

    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk

    plt.style.use("seaborn-v0_8")

    fig, ax = plt.subplots()

    ax.scatter(rw.x_values, rw.y_values, s=6)
    ax.set_aspect("equal")
    plt.show()

    keep_running = input("Make another walk (y/n): ").lower()
    if keep_running == "n":
        break
