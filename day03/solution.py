import re

# Read the corrupted memory input
with open("input.txt", "r") as file:
    data = file.read()

# Define a regex pattern to find valid mul instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Extract all matches
matches = re.findall(pattern, data)
print(f"Found {len(matches)} valid mul instructions.")

# Compute the products of valid instructions
results = []
for x, y in matches:
    product = int(x) * int(y)
    results.append(product)

print(f"First 5 results: {results[:5]}")

# Calculate the total sum of products
total_sum = sum(results)
print(f"Total sum of all valid multiplications: {total_sum}")