#!/usr/bin/python3
import re

with open("./input") as input:
    Lines = input.read().splitlines()

count = 0

for line in Lines:
    ranges = re.split(r'[,-]', line)
    a = set(range(int(ranges[0]), int(ranges[1])+1))
    b = set(range(int(ranges[2]), int(ranges[3])+1))
    if a.intersection(b) or b.intersection(a):
        count += 1
print(count)