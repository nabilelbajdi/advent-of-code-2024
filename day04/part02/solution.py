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

# Define the corner patterns to look for
CORNER_PATTERNS = ["MSMS", "MMSS", "SSMM", "SMSM"]

def count_corner_patterns(grid):
    """Count occurrences of 'A' with valid corner patterns."""
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == "A":
                corners = [
                    grid[row - 1][col - 1], # Top left
                    grid[row - 1][col + 1], # Top right
                    grid[row + 1][col - 1], # Bottom left
                    grid[row + 1][col + 1], # Bottom right
                ]

                if "".join(corners) in CORNER_PATTERNS:
                    count += 1
    return count

# Count all occurrences
occurrences_part2 = count_corner_patterns(grid)
print(f"Total occurrences of 'A' with matching corner patterns: {occurrences_part2}")