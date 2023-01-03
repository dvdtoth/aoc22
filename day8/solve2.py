#!/usr/bin/env python3

import numpy as np

with open("./input") as input:
    Lines = input.read().splitlines()

matrix = np.array([[int(s) for s in line.strip()] for line in Lines])

def line_of_sight(line, tree, loc):
    if loc == 0:
        return 0
    visible = 0
    for t in reversed(line[:loc]):
        visible += 1
        if t >= tree:
            break
    return visible


def look_all_sides(matrix, coords = dict()):
    for kl,l in enumerate(matrix):
        # Left
        score, prev = 0, 0
        for k, c in enumerate(l):
            score = line_of_sight(l, c, k)
            coords[str([kl,k])] = [score]
        # Right
        score, prev = 0, 0
        for k, c in enumerate(l[::-1]):
            score = line_of_sight(l[::-1], c, k)
            coords[str([kl,len(l)-1-k])].append(score)


    matrix2 = np.rot90(matrix) # rotate left by 90
    for kl, l in enumerate(matrix2):
        # Top
        score, prev = 0, 0
        for k, c in enumerate(l):
            score = line_of_sight(l, c, k)
            coords[str([k,len(l)-1-kl])].append(score)

        # Bottom
        score, prev = 0, 0
        for k, c in enumerate(l[::-1]):
            score = line_of_sight(l[::-1], c, k)
            coords[str([len(l)-1-k,len(l)-1-kl])].append(score)

    return coords

def best_spot(coords):
    best = 0

    for v in coords.values():
        if np.prod(v) > best:
            best = np.prod(v)
    return best

print(best_spot(look_all_sides(matrix)))