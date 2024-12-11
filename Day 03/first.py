""" 
First part of the Advent of Code exercise

Day 3 --> https://adventofcode.com/2024/day/3

Made by Matjoeee
"""

import re

# Initialize variables
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
result = []

# Read data
with open("input.txt", "r") as file:
    text = file.read()
    
# Find and sum matches
match = re.findall(pattern, text)
res = [int(a) * int(b) for a, b in match]
res = sum(res)

print(res)
