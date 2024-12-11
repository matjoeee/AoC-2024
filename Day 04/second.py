""" 
Second part of the Advent of Code exercise

Day 4 --> https://adventofcode.com/2024/day/4#part2

Made by Matjoeee
"""

import numpy as np

def mas(sequence):
    return sequence == "MAS" or sequence == "SAM"

def countMas(grid):
    count = 0
    rows, cols = grid.shape
    
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if (
                mas(grid[r - 1, c - 1] + grid[r, c] + grid[r + 1, c + 1]) and mas(grid[r + 1, c - 1] + grid[r, c] + grid[r - 1, c + 1])
            ):
                count += 1
    return count

# Main script
if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    gridArr = np.array([list(row) for row in grid])
    
    masCount = countMas(gridArr)
    
    print(masCount)
