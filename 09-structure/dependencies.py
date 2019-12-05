# Version 1

def read_csv(filename):
    data = []
    with open(filename, 'r') as data_file:
        for line in data_file:
            row = [float(token) for token in line.split(",")]
            data.append(row)
    return data

def average(rows):
    # Assume all rows have same length!
    number_of_rows = len(rows)
    number_of_columns = len(rows[0])
    result =[]
    for i in range(number_of_columns):
        column_average = sum([row[i] for row in rows]) / number_of_rows
        result.append(column_average)
    return result

data = read_csv("my_data.csv")
output = average(data)

#########

# Version 2

import numpy as np
import pandas as pd

data = pd.read_csv("my_data.csv")
output = np.mean(data, axis=0)