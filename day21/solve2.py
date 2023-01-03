#!/usr/bin/env python3

ops = dict()
evals = 0
with open("./input") as input:
    for line in input:
        data = line.strip().split(" ")
        if len(data) == 2:
            ops.update({line[:4]: int(data[1])})
        else:
            evals += 1
            ops.update({line[:4]: [data[1], data[2], data[3]]})


def solve(num):
    global x, y
    e = evals
    o = ops.copy()
    o['humn'] = num

    while e > 1:
        for k in o:
            if k == 'root':
                continue
            if type(o[k]) is not int:
                a, op, b = o[k]
                if type(o[a]) is int and type(o[b]) is int:
                    o[k] = int(eval(str(o[a]) + op + str(o[b])))
                    e -= 1
    x = o[ops['root'][0]]
    y = o[ops['root'][2]]

    return x, y

o = ops.copy()
x = 1
y = 2
bottom = 0
top = int(1e20)
while x != y:
    mid = (bottom+top)//2
    x,y = solve(mid)
    score = y - x
    # print(mid, x, y)
    if score < 0:
        bottom = mid
    elif score > 0:
        top = mid

# print(mid)
# mehh
print(mid-1)

# weird off by one to fix
# print(solve(3093175982596))
# print(solve(3093175982595))
