# Complete solution for Day 4 Part 1

# Step 1: Read the puzzle input
with open("../input.txt", "r") as file:
    puzzle_input = file.read().strip()

# Step 2: Convert the input into a grid (list of rows)
grid = []
for line in puzzle_input.splitlines():
    grid.append(list(line))

# Display the grid dimensions and a sample row
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0
print(f"Grid Dimensions: {rows} x {cols}")
if rows > 0:
    print(f"First Row: {grid[0]}")