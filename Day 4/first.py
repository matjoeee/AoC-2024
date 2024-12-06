""" 
First part of the Advent of Code exercise

Day 4 --> https://adventofcode.com/2024/day/4

Made by Matjoeee
"""

def positionValidation(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def countXmas(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Down-Right Diagonal
        (1, -1), # Down-Left Diagonal
        (-1, 1), # Up-Right Diagonal
        (-1, -1) # Up-Left Diagonal
    ]
    
    def searchWord(x, y, word):
        count = 0
        for dx, dy in directions:
            nx, ny = x, y
            found = True
            for k in range(word_length):
                if not positionValidation(nx, ny, rows, cols) or grid[nx][ny] != word[k]:
                    found = False
                    break
                nx += dx
                ny += dy
            if found:
                count += 1
        return count

    total_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]: 
                total_count += searchWord(i, j, word)
    
    return total_count

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

word = "XMAS"
count = countXmas(grid, word)
print(f"'{word}' found {count} time(s) in the grid.")
