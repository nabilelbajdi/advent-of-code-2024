import re

# Step 1: Read the corrupted memory input
with open("input.txt", "r") as file:
    data = file.read()

# Step 2: Define regex patterns
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
control_pattern = r"(do\(\)|don't\(\))"
full_pattern = rf"{control_pattern}|{mul_pattern}"

# Extract all relevant instructions
instructions = re.findall(full_pattern, data)

# Step 3: Process instructions and track state
enabled = True
results = []

for instr in instructions:
    if instr[0] == "do()":
        enabled = True
    elif instr[0] == "don't()":
        enabled = False
    elif instr[1] and instr[2]:
        if enabled:
            x, y = int(instr[1]), int(instr[2])
            results.append(x * y)

# Step 4: Calculate the total sum of enabled multiplications
total_sum = sum(results)
print(f"Total sum of enabled multiplications: {total_sum}")
