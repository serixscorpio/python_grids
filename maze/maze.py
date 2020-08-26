# Helper function to load the grid
def load_grid(filename):
    grid = []
    with open(filename) as file:
        for l in file.readlines():
            grid.append(list(l.strip()))

    return grid

# Helper function to print out the grid
def print_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            print(grid[y][x],end="")
        print()

# Helper function to find the location of a specific character
def find(grid, ch):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == ch:
                return (y,x)

    return None

def mark_next_steps(grid, nth, step, next_steps):
    for y, x in [(-1,0), (0, 1), (1,0), (0, -1)]:
        if grid[step[0]+y][step[1]+x] == " ":
            grid[step[0]+y][step[1]+x] = step
            next_steps.append((step[0]+y, step[1]+x))
        if grid[step[0]+y][step[1]+x] == "E":
            grid[step[0]+y][step[1]+x] = step
            next_steps.append((step[0]+y, step[1]+x))
            return

def figure_out_next_steps(grid, nth, steps):
    next_steps = []
    for step in steps:
        mark_next_steps(grid, nth, step, next_steps)
    return next_steps

def explore(grid, nth, steps, end):
    next_steps = figure_out_next_steps(grid, nth, steps)
    # logic to figure out current_steps_list
    if len(next_steps) == 0:
        # exploration finished
        return False
    if end in next_steps:
        # optionally run path retrieval logic
        return True
    return explore(grid, nth+1, next_steps, end)

def fill_path(solution_grid, output_grid, start, end):
    backtrack_step = solution_grid[end[0]][end[1]]
    if backtrack_step == start:
        # done filling path
        return
    output_grid[backtrack_step[0]][backtrack_step[1]] = "."
    fill_path(solution_grid, output_grid, start, backtrack_step)

# Find a solution.
# Two options, return true/false if you find a solution
# Extra credit: return the path you found in the maze so that
#               you can display the path.
def solve(grid, start, end,): # Add your parameters as needed    
    # Compute any path from start to end
    return explore(grid, 1, [start], end)

if __name__ == "__main__":
    # Allow for maze's to be passed in on the command line:
    # python maze.py maze.txt
    import sys
    maze = sys.argv[1] if len(sys.argv) > 1 else "maze.txt"

    # Load the grid
    grid = load_grid(maze)

    # compute a solution
    start = find(grid, "S")
    end = find(grid, "E")
    solution = solve(grid, start, end)

    # print_grid(grid)
    if solution:
        print ("Found solution!")
        output_grid = load_grid(maze)
        fill_path(grid, output_grid, start, end)
        print_grid(output_grid)
    else: 
        print ("No solution!")

    # Extra credit: print out the maze with your solution    
