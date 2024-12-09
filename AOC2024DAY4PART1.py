from common import load_input

import numpy as np

input = load_input()

def find_XMAS(string):
    counter = 0
    counter += string.count('XMAS')
    counter += string.count('SAMX')
    return counter

horizontal_inputs = input.split('\n')

grid = []

for row in horizontal_inputs:
    row = list(row)
    grid += [row]

final_count = 0

vertical_inputs = []

for row in horizontal_inputs:
    final_count += find_XMAS(row)

print(final_count)

def column_finder(horizontal_inputs, iteration):
    column = ''
    for row in horizontal_inputs:
        column += row[iteration]
    return column

for iteration in enumerate(horizontal_inputs):
    iteration = iteration[0]
    vertical_inputs += column_finder(horizontal_inputs, iteration)
    vertical_inputs += '\n'

joined_vertical_inputs = "".join(vertical_inputs)

split_vertical_inputs = joined_vertical_inputs.split('\n')

for column in split_vertical_inputs:
    final_count += find_XMAS(column)

print(final_count)

def find_2d_list(char, list_2d):
    locations = []
    for row_index, row in enumerate(list_2d):
        for col_index, element in enumerate(row):
            if element == char:
                coords = [row_index, col_index]
                coords = tuple(coords)
                locations.append(coords)
    return locations

def valid_coordinate(x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid)


all_Xs_location = find_2d_list('X', grid)
for X in all_Xs_location:
    x = X[0]
    y = X[1]
    if valid_coordinate(x - 1, y - 1) and valid_coordinate(x - 2, y - 2) and valid_coordinate(x - 3, y - 3):
        if grid[x - 1][y - 1] == 'M' and grid[x - 2][y - 2] == 'A' and grid[x - 3][y - 3] == 'S':
            final_count += 1
    if valid_coordinate(x + 1, y + 1) and valid_coordinate(x + 2, y + 2) and valid_coordinate(x + 3, y + 3):
        if grid[x + 1][y + 1] == 'M' and grid[x + 2][y + 2] == 'A' and grid[x + 3][y + 3] == 'S':
            final_count += 1
    if valid_coordinate(x - 1, y + 1) and valid_coordinate(x - 2, y + 2) and valid_coordinate(x - 3, y + 3):
        if grid[x - 1][y + 1] == 'M' and grid[x - 2][y + 2] == 'A' and grid[x - 3][y + 3] == 'S':
            final_count += 1
    if valid_coordinate(x + 1, y - 1) and valid_coordinate(x + 2, y - 2) and valid_coordinate(x + 3, y - 3):
        if grid[x + 1][y - 1] == 'M' and grid[x + 2][y - 2] == 'A' and grid[x + 3][y - 3] == 'S':
            final_count += 1

print(final_count)