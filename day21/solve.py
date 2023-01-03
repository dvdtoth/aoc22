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

while evals > 0:
    for k in ops:
        if type(ops[k]) is not int:
            a, op, b = ops[k]
            if type(ops[a]) is int and type(ops[b]) is int:
                ops[k] = int(eval(str(ops[a]) + op + str(ops[b])))
                evals -= 1

print(ops["root"])




