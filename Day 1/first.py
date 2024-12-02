""" 
First part of the Advent of Code exercise

Day 1 --> https://adventofcode.com/2024/day/1

Made by Matjoeee
"""

f = open("input.txt", "r")

f_loc = []          # First location
s_loc = []          # Second location

for x in f:
    list = (x.strip()).split()
    f_loc.append(list[0])
    s_loc.append(list[1])
        
f_loc.sort()
s_loc.sort()
diff_loc = [abs(int(a) - int(b)) for a, b in zip(f_loc, s_loc)]

print(sum(diff_loc))

f.close()