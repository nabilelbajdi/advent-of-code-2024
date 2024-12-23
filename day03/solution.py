import re

# Read the corrupted memory input
with open("input.txt", "r") as file:
    data = file.read()

# Define a regex pattern to find valid mul instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Extract all matches
matches = re.findall(pattern, data)
print(f"Found {len(matches)} valid mul instructions.")
