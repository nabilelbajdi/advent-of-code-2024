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

differences = []

# Use zip to pair elements from both sorted lists
for left_num, right_num in zip(sorted_left, sorted_right):
    # Calculate the absolute difference between the pair
    difference = abs(left_num - right_num)
    
    # Add the difference to the list
    differences.append(difference)

# Calculate the total distance by summing up all differences
total_distance = sum(differences)

# Print the result
print("Total Distance:", total_distance)

