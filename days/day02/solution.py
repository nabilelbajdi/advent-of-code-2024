reports = []

with open("input.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.strip().split())))

print("Parsed Reports:", reports)