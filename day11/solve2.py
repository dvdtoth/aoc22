#!/opt/homebrew/bin/python3
import numpy

monkey = []
op = []
test = []
true = []
false = []

ops = {'+' : numpy.add, '*': numpy.multiply}

file = open("./input").read().strip()

for mo in file.split('\n\n'):
    id, items, o, ts, t, f = mo.split('\n')
    monkey.append([int(i) for i in items.split(":")[1].split(",")])
    op.append(o.split()[-2:])
    test.append(int(ts.split()[-1]))
    true.append(int(t.split()[-1]))
    false.append(int(f.split()[-1]))

inspect = [0 for _ in range(len(monkey))]

modulo = 1
for t in test:
    modulo = modulo * t

for r in range(10000):
    for m in range(len(monkey)):
        for i in monkey[m].copy():
            worry = ops[op[m][0]](i, i if op[m][1] == "old" else int(op[m][1]))
            monkey[m].remove(i)
            inspect[m] += 1
            # This is the tricky math catch of part2: Divide by common modulo to keep the number "low".
            worry %= modulo
            monkey[true[m]].append(worry) if worry % test[m] == 0 else monkey[false[m]].append(worry)

# monkey business 
print(numpy.prod(sorted(inspect)[-2:]))