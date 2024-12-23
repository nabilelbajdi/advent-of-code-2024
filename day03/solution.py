# Read the corrupted memory input
with open("input.txt", "r") as file:
    data = file.read()

# Print data to confirm it's loaded correctly
print(f"Loaded data: {data[:100]}...")
