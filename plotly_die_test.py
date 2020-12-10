from plotly_die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

count = 1000
result = []

for roll_number in range(count):
    result.append(die.roll())

print(result)

frequency = []

for value in range(1,die.num_sides+1):
    frequency.append(result.count(value))

print(frequency)
print(sum(frequency))

data = [Bar(x=list(range(1,die.num_sides+1)), y=frequency)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency'}
my_layout = Layout(title='Becky Testing', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='bar.html')
