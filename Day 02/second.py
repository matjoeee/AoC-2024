""" 
Second part of the Advent of Code exercise

Day 2 --> https://adventofcode.com/2024/day/2#part2

Made by Matjoeee
"""

# Calculate difference
def safety(report):
    diff = [report[i+1] - report[i] for i in range(len(report) - 1)]
    incr = all(1 <= diff <= 3 for diff in diff)
    decr = all(-3 <= diff <= -1 for diff in diff)
    
    return incr or decr

# Apply Problem Dampener
def dampener(report):
    for i in range(len(report)):
        new = report[:i] + report[i+1:]
        if safety(new):
            return True
    return False

# Count reports
def safeCount(reports):
    safeCountRep = 0
    for report in reports:
        if safety(report) or dampener(report):
            safeCountRep += 1
    return safeCountRep

# Read data
with open("input.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file]

# Solution
safeRep = safeCount(reports)
print(safeRep)