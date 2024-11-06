import json, pylab; import numpy as np

# str to dict
with open('cars.txt') as f:
    data = f.read()
    cars_data = json.loads(data)

# Creating lists
x = np.array(list(cars_data.keys()))
y = np.array(list(cars_data.values()))

xy = np.array([list(cars_data.keys()), list(cars_data.values())])

# Result
x_data = xy[0]
y_data = xy[1]

pylab.bar(x_data, y_data)
pylab.show()