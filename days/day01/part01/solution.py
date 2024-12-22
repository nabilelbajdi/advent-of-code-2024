left = []
right = []

with open('input.txt', 'r') as file:
    for line in file:
        # Clean up the line to split it into two parts
        numbers = line.strip().split()
        
        # Add first number to the "left" list and the second to the "right" list
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

print("Left:", left)  # Shows all numbers from the first column
print("Right:", right)  # Shows all numbers from the second column
