""" 
Second part of the Advent of Code exercise

Day 4 --> https://adventofcode.com/2024/day/4#part2

Made by Matjoeee
"""

def countPatterns(grid):
    rows, cols = len(grid), len(grid[0])
    pattern = "MAS"
    reversedPattern = pattern[::-1]
    count = 0

    # Check if a pattern exists
    def Xmas(x, y):
        if (
            x - 1 >= 0 and x + 1 < rows and
            y - 1 >= 0 and y + 1 < cols
        ):
            # Diagonal 1: top-left to bottom-right
            topL = grid[x - 1][y - 1:y + 2]
            botR = grid[x + 1][y - 1:y + 2]
            if (topL == list(pattern) and botR[::-1] == list(pattern)) or \
               (topL == list(reversedPattern) and botR[::-1] == list(reversedPattern)): 
                return True 
            
            # Diagonal 2: bottom-left to top-right
            botL = [grid[x + 1][y - 1], grid[x][y], grid[x - 1][y + 1]]
            topR = [grid[x - 1][y - 1], grid[x][y], grid[x + 1][y + 1]]
            if (botL == list(pattern) and topR[::-1] == list(pattern)) or \
               (botL == list(reversedPattern) and topR[::-1] == list(reversedPattern)):
                return True

        return False

    # Iterate over every cell as the center of the X
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == "A" and Xmas(i, j):
                count += 1
                
    return count

# Read input file
def getGrid(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

filename = 'input.txt'
grid = getGrid(filename)
for row in grid:
    print(row)

# Count the X-MAS patterns
count = countPatterns(grid)
print(f"Number of X-MAS patterns: {count}")









