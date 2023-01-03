#!/usr/bin/env python3

import numpy as np

with open("./input") as input:
    Lines = input.read().splitlines()

matrix = np.array([[int(s) for s in line.strip()] for line in Lines])

def look_all_sides(matrix, coords = set()):
    for kl,l in enumerate(matrix):
        # Left
        tallest = -1
        for k, c in enumerate(l):
            if c > tallest:
                coords.add(str([kl,k]))
                tallest = c
        # Right
        tallest = -1
        for k, c in enumerate(reversed(l)):
            if c > tallest:
                coords.add(str([kl,len(l)-1-k]))
                tallest = c

    matrix2 = np.rot90(matrix) # rotate left by 90
    for kl, l in enumerate(matrix2):
        # Top
        tallest = -1
        for k, c in enumerate(l):
            if c > tallest:
                coords.add(str([k,len(l)-1-kl]))
                tallest = c
        # Bottom
        tallest = -1
        for k, c in enumerate(reversed(l)):
            if c > tallest:
                coords.add(str([len(l)-1-k,len(l)-1-kl]))
                tallest = c
    return coords

print(len(look_all_sides(matrix)))