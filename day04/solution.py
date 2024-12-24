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

# Function to check if "XMAS" exists starting from a position
def find_word(grid, word, start_row, start_col, direction):
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0])
    dr, dc = direction

    for k in range(word_length):
        r = start_row + k * dr
        c = start_col + k * dc
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != word[k]:
            return False
    return True

# Function to count occurrences of the word in the grid
def count_word_occurrences(grid, word):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            for direction in DIRECTIONS:
                if find_word(grid, word, row, col, direction):
                    count += 1
    return count

# Count all occurrences of "XMAS"
word_to_find = "XMAS"
occurrences = count_word_occurrences(grid, word_to_find)

# Display the total occurrences
print(f"Total occurrences of '{word_to_find}': {occurrences}")