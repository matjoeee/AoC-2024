""" 
Second part of the Advent of Code exercise

Day 5 --> https://adventofcode.com/2024/day/5#part2

Made by Matjoeee
"""

# This function checks whether the update rule is being followed
def isOrdered(update, relevantRules):
    for X, Y in relevantRules:
        if update.index(X) > update.index(Y):  # Is X coming before Y?
            return False
    return True

# This function performs a simple greedy sort for the pages
def greedySort(pages, rules):
    sortedPages = []
    unsortedPages = pages[:]
    
    while unsortedPages:
        for page in unsortedPages:
            # Check if the page can be placed at the current position
            valid = True
            for X, Y in rules:
                if X == page and Y in unsortedPages:
                    valid = False  # Rule violation
                    break
            if valid:
                sortedPages.append(page)
                unsortedPages.remove(page)
                break
        else:
            return []
    
    return sortedPages

# Read the file line by line
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Variables
rules = []
updates = []
correctUpdates = []
incorrectUpdates = []
correctedUpdates = []
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
    # Filter relevant rules for this update
    relevantRules = [(X, Y) for (X, Y) in rules if X in update and Y in update]
    
    # Check for correctly ordered updates
    if isOrdered(update, relevantRules):
        correctUpdates.append(update)
    # Otherwise, keep them for later to be sorted
    else:
        incorrectUpdates.append(update)

# Correct each incorrectly ordered update using greedy sort
for update in incorrectUpdates:
    sortedUpdate = greedySort(update, rules)
    if sortedUpdate:
        correctedUpdates.append(sortedUpdate)

# Look for middle pages and calculate sum
middlePage = [update[len(update) // 2] for update in correctedUpdates]
totalSum = sum(middlePage)

print("Sum of Middle Pages (Corrected):", totalSum)
