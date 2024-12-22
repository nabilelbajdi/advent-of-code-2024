left = []
right = []

with open('input.txt', 'r') as file:
    for line in file:
        # Clean up the line to split it into two parts
        numbers = line.strip().split()
        
        # Add first number to the "left" list and the second to the "right" list
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

# Sort the left and right lists
sorted_left = sorted(left)
sorted_right = sorted(right)

# Print sorted lists to verify
print("Sorted Left:", sorted_left)
print("Sorted Right:", sorted_right)
