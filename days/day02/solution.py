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

# Function to check if a report can become safe by removing one level
def can_be_safe_with_one_removal(report):
    for i in range(len(report)):
        # Create a new report with the ith level removed
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

# Count reports that are safe or can become safe
safe_count = 0

for report in reports:
    if is_safe(report) or can_be_safe_with_one_removal(report):
        safe_count += 1

# Print the result
print(f"Number of safe reports (with Problem Dampener): {safe_count}")
