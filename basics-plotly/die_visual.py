from die import Die
import plotly.express as px

# Create a die
die1 = Die()
die2 = Die()
# Make some rolls, and store results in a list

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the result
frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

title = "Result of Rolling two D6 1000 times"
labels = {"x": "Result", "y": "Frequency of Result"}
# Visualize the results
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customizing the chart
fig.update_layout(xaxis_dtick=1)
fig.show()
