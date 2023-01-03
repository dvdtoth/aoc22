#!/usr/bin/env python3

from collections import deque

with open("./input") as input:
    q = deque(enumerate((int(line) for line in input)))

# mix
for i in range(len(q)):
    while q[0][0] != i:
        q.rotate(-1)

    item_pos, item_val = q.popleft()

    q.rotate(-1 * item_val)
    q.appendleft((item_pos, item_val))

# count from 0
while q[0][1] != 0:
    q.rotate(-1)

total = 0
for i in range(3001):
    q.rotate(-1)
    if (i+1) % 1000 == 0:
        total += q[0][1]

print(total)


