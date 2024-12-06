""" 
First part of the Advent of Code exercise

Day 3 --> https://adventofcode.com/2024/day/3#part2

Made by Matjoeee
"""

import re

def solveCorruption(memory):
    # Initialize variables
    totalSum = 0
    mulEnabled = True

    # Regular expression patterns for valid mul and control instructions
    mulPattern = r"mul\((\d+),(\d+)\)"
    doPattern = r"do\(\)"
    dontPattern = r"don't\(\)"

    # Scan through the memory for instructions
    instructions = re.finditer(rf"{mulPattern}|{doPattern}|{dontPattern}", memory)

    for match in instructions:
        if match.group(0).startswith("mul"):
            # Process `mul` instruction if enabled
            if mulEnabled:
                x, y = int(match.group(1)), int(match.group(2))
                totalSum += x * y
        elif match.group(0) == "do()":
            mulEnabled = True
        elif match.group(0) == "don't()":
            mulEnabled = False

    return totalSum

# Load the corrupted memory from a file
filePath = "input.txt"

with open(filePath, 'r') as file:
    corruption = file.read()

# Calculate the result
result = solveCorruption(corruption)

print(result)
