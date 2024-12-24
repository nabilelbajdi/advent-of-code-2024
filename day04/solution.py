# Step 1: Read the puzzle input
with open("input.txt", "r") as file:
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

# Step 3: Define directions as (row_step, column_step)
DIRECTIONS = [
    (0, 1),   # Horizontal right
    (0, -1),  # Horizontal left
    (1, 0),   # Vertical down
    (-1, 0),  # Vertical up
    (1, 1),   # Diagonal down right
    (1, -1),  # Diagonal down left
    (-1, 1),  # Diagonal up right
    (-1, -1), # Diagonal up left
]

# Display the directions
print(f"Defined Search Directions: {DIRECTIONS}")

# Function to check if "XMAS" exists starting from a position
def find_word(grid, word, start_row, start_col):
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0])

    for direction in DIRECTIONS:
        dr = direction[0]
        dc = direction[1]

        found = True
        for k in range(word_length):
            r = start_row + k * dr
            c = start_col + k * dc

            if r < 0 or r >= rows or c < 0 or c >= cols:
                found = False
                break

            if grid[r][c] != word[k]:
                found = False
                break

        if found:
            return True

    return False