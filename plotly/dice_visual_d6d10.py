from die import Die
import plotly.express as px

# Create a D6 and a D10

die_1 = Die()
die_2 = Die(10)

# Make some rolls and store the results
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


title = "Result of Rolling two D6 and D10 50,000 times"
labels = {"x": "Result", "y": "Frequency of Result"}
# Visualize the results
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customizing the chart
fig.update_layout(xaxis_dtick=1)
fig.show()
