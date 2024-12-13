""" 
First part of the Advent of Code exercise

Day 5 --> https://adventofcode.com/2024/day/5

Made by Matjoeee
"""

# This function checks whether the update rule is being followed
def isOrdered(update, relevantRules):
    for X, Y in relevantRules:
        if update.index(X) > update.index(Y):   # Is X coming before Y?
            return False
    return True

# Read the file line by line
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Variables
rules = []
updates = []
correctUpdate = []
isUpdateSection = False

# Processing file line by line
for line in lines:
    line = line.strip()
    if not line:  
        isUpdateSection = True
        continue
    
    # Splitting between rules section and update section
    if not isUpdateSection:
        X, Y = map(int, line.split('|'))
        rules.append((X, Y))
    else:
        updates.append(list(map(int, line.split(','))))

# Process each update
for update in updates:
    relevantRules = [(X, Y) for (X, Y) in rules if X in update and Y in update]
    # Check for correctly ordered updates
    if isOrdered(update, relevantRules):
        correctUpdate.append(update)

# Look for middle pages and calculate sum
middlePage = [update[len(update) // 2] for update in correctUpdate]
totalSum = sum(middlePage)

# Solution
print("Sum of Middle Pages:", totalSum)
