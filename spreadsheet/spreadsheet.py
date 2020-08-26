import numbers

# Read in the data
grid = []
with open("spreadsheet_formula.txt") as file:
    for l in file.readlines():
        grid.append(l.strip().split(","))

# Helper function to print out the grid
def print_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            # Use fixed width formating to make things more spreadsheet like
            print("{:11s}".format(str(grid[y][x])),end="")
        print()

#
# Solution goes here :)
# 
# Write code to scan and find the formulas and replace them with the 
# correct values.
def num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return 0

def vertical_sum(grid, row_num, col_num):
    if row_num == 0:
        return num(grid[row_num][col_num])
    return vertical_sum(grid, row_num-1, col_num) + num(grid[row_num][col_num])

for row_num in range(len(grid)):
    for col_num in range(len(grid[0])):
        if grid[row_num][col_num] == "*":
            grid[row_num][col_num] = num(grid[row_num][col_num-2]) * num(grid[row_num][col_num-1])
        if grid[row_num][col_num] == "+":
            grid[row_num][col_num] = vertical_sum(grid, row_num-1, col_num)

# Print out the grid so we see the answer
print_grid(grid)
