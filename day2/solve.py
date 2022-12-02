#!/usr/bin/python3

file = open("./input", "r")
Lines = file.readlines()

# Rock A X
# Paper B Y
# Scissors C Z

total = 0
draw = ["A X\n", "B Y\n", "C Z\n"]
win = ["A Y\n", "B Z\n", "C X\n"]

for line in Lines:
    if line[2] == 'X':
        total += 1
    if line[2] == 'Y':
        total += 2
    if line[2] == 'Z':
        total += 3
    if line in win:
        total += 6
    if line in draw:
        total += 3
print(total)