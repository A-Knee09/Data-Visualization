from random import choice


class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of the walk"""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, axis="x"):
        """Generate a step in a direction"""
        direction = choice([-1, 1])
        distance = choice([1, 2, 3, 4]) if axis == "x" else choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Calculate all the points of the walk"""

        # Keep taking the steps until walk reaches desired length
        while len(self.x_values) < self.num_points:
            x_step = self.get_step("x")
            y_step = self.get_step("y")

            # Rejecting moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
