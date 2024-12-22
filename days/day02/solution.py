# Parse the input file into a list of reports
reports = []

with open("input.txt", "r") as file:
    for line in file:
        # Convert each line into a list of integers
        reports.append(list(map(int, line.strip().split())))

# Function to check if a report is safe
def is_safe(report):
    # Calculate the differences between adjacent levels
    differences = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
    # Check if all differences are between 1 and 3
    valid_differences = all(1 <= diff <= 3 for diff in differences)
    # Check if the levels are strictly increasing
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    # Check if the levels are strictly decreasing
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    # A report is safe if it has valid differences and is either increasing or decreasing
    return valid_differences and (increasing or decreasing)

# Count the number of safe reports
safe_count = sum(1 for report in reports if is_safe(report))

# Print the result
print(f"Number of safe reports: {safe_count}")
