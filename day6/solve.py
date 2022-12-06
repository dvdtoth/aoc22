#!/usr/bin/python3

with open("./input") as input:
    line = input.readline()

buff = []
count = 0
last = 0

for k, c in enumerate(line):
    if c not in buff and len(buff) < 5 and (k == last + 1 or last == 0):
        buff.append(c)
        last = k
        count += 1
        if len(buff) == 4:
            print(count)
            break
    else:
        buff = [c]
        last = 0
        count +=1