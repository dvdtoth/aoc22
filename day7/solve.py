#!/usr/bin/python3

with open("./input") as input:
    Lines = input.read().splitlines()

root = {}
cwd = ["/"]
for key, line in enumerate(Lines):
    if line == "$ cd ..":
        cwd.pop()
    if line[:4] == "$ cd" and line != "$ cd .." and line != "$ cd /":
        cwd.append(line[5:])
    x = line.split()
    c = str(cwd)
    if x[0].isdigit() == True:
        meh = cwd.copy()
        for d in range(len(meh)):
            c = str(meh)
            if c not in root:
                root[c] = int(x[0])
            else:
                root[c] += int(x[0])
            meh.pop()


total = 0
for k,v in enumerate(root):
    if root[v] < 100000:
        total += root[v]
#    print(k, v, root[v])
print(total)
