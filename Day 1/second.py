"""
First part of the Advent of Code exercise

Day 1 --> https://adventofcode.com/2024/day/1#part2

Made by Matjoeee
"""
from collections import Counter

f = open("input.txt", "r")

f_loc = []          # First location
s_loc = []          # Second location

for x in f:
    list = (x.strip()).split()
    f_loc.append(list[0])
    s_loc.append(list[1])
        
f_loc.sort()
s_loc.sort()

f_loc = [int(num) for num in f_loc]
s_loc = [int(num) for num in s_loc]

count_loc = Counter(s_loc)
sim_loc = sum(num * count_loc[num] for num in f_loc)

print(sim_loc)

f.close()