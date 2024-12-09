#this is totally not good and is kind of broken but it will give you the right answer.
from common import load_input

input = load_input()

input_split = input.split('\n')

def make_grid(split_input):
    grid = []
    for line in split_input:
        line = list(line)
        grid += [line]
    return grid

grid = make_grid(input_split)

def find_2d_list(char, list_2d):
    for row_index, row in enumerate(list_2d):
        for col_index, element in enumerate(row):
            if element == char:
                location = [row_index, col_index]
    return location

def find_direction(grid):
    for row in grid:
        for item in row:
            if item == '^':
                return '^'
            if item == '>':
                return '>'
            if item == 'v':
                return 'v'
            if item == '<':
                return '<'
        
def valid_coordinate(x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid)
        
def find_and_execute_next_move(grid):
    direction = find_direction(grid)
    if direction == None:
        Break = 'break'
        return grid and Break
    position = find_2d_list(direction, grid)
    x = position[0]
    y = position[1]
    if direction == '<':
        if valid_coordinate(x, y - 1):
            if grid[x][y - 1] == '#':
                grid[x][y] = '^'
                return grid
            elif grid[x][y - 1] == '.' or 'X':
                grid[x][y] = 'X'
                grid[x][y - 1] = '<'
                return grid
        if x < 0 or y - 1 < 0 or x >= len(grid) or y - 1 >= len(grid):
            grid[x][y] = 'X'
            Break = 'break'
            return grid and Break
    if direction == '^':
        if valid_coordinate(x - 1, y):
            if grid[x - 1][y] == '#':
                grid[x][y] = '>'
                return grid
            elif grid[x - 1][y] == '.' or 'X':
                grid[x][y] = 'X'
                grid[x - 1][y] = '^'
                return grid
        if x - 1 < 0 or y < 0 or x - 1 >= len(grid) or y >= len(grid):
            grid[x][y] = 'X'
            Break = 'break'
            return grid and Break
    if direction == '>':
        if valid_coordinate(x, y + 1):
            if grid[x][y + 1] == '#':
                grid[x][y] = 'v'
                return grid
            elif grid[x][y + 1] == '.' or 'X':
                grid[x][y] = 'X'
                grid[x][y + 1] = '>'
                return grid
        if x < 0 or y + 1 < 0 or x >= len(grid) or y + 1 >= len(grid):
            grid[x][y] = 'X'
            Break = 'break'
            return grid and Break
    if direction == 'v':
        if valid_coordinate(x + 1, y):
            if grid[x + 1][y] == '#':
                grid[x][y] = '<'
                return grid
            elif grid[x + 1][y] == '.' or 'X':
                grid[x][y] = 'X'
                grid[x + 1][y] = 'v'
                return grid
        if x + 1 < 0 or y < 0 or x + 1 >= len(grid) or y >= len(grid):
            grid[x][y] = 'X'
            Break = 'break'
            return grid and Break

end = False

Break = ''

for i in range(0, 10000):
    find_and_execute_next_move(grid)

def find_all_in_2d_list(char, list_2d):
    locations = []
    for row_index, row in enumerate(list_2d):
        for col_index, element in enumerate(row):
            if element == char:
                coords = [row_index, col_index]
                coords = tuple(coords)
                locations.append(coords)
    return locations

all_Xs = find_all_in_2d_list('X', grid)

print(len(all_Xs))








        

            
            

