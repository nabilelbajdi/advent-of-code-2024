from collections import Counter

# Read input
with open("../input.txt", "r") as file:
    left = []
    right = []
    for line in file:
        numbers = line.strip().split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

# Count occurrences in the right list
right_counts = Counter(right)

# Calculate the similarity score
similarity_score = 0
for num in left:
    count_in_right = right_counts.get(num, 0)
    similarity_score += num * count_in_right

# Print the final similarity score
print("Similarity Score:", similarity_score)