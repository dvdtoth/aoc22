#!/usr/bin/python3

file = open("./input", "r")
Lines = file.readlines()

# Rock A 1
# Paper B 2
# Scissors C 3
# Lose X
# Draw Y
# Win Z

total = 0
one = ["A Y\n", "B X\n", "C Z\n"]
two = ["A Z\n", "B Y\n", "C X\n"]
three = ["A X\n", "B Z\n", "C Y\n"]

for line in Lines:
    if line[2] == 'Y':
        total += 3
    if line[2] == 'Z':
        total += 6
    if line in one:
        total += 1
    if line in two:
        total += 2
    if line in three:
        total += 3
print(total)