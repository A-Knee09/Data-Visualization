import matplotlib.pyplot as plt
import matplotlib
from random_walk import RandomWalk

matplotlib.use("TkAgg")

# Make a random walk, as long as program is active
while True:

    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk

    plt.style.use("seaborn-v0_8")

    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)

    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.RdPu,
        edgecolors="none",
        s=1,
    )
    ax.set_aspect("equal")

    # Emphasize the first and last points
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk (y/n): ").lower()
    if keep_running == "n":
        break
