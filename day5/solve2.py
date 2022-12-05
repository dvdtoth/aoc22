#!/usr/bin/python3
import string

with open("./input") as input:
    Lines = input.read().splitlines()

# Map stack
stack = {1:[],5:[],9:[],13:[],17:[],21:[],25:[],29:[],33:[]}
key_index_list = dict(enumerate(stack.keys()))
for num, line in enumerate(Lines):
    # Map initial layout
    if num < 8:
        for k, c in enumerate(line):
            if k in [1,5,9,13,17,21,25,29,33] and c in string.ascii_uppercase:
                stack[k].append(c)
    # Solve
    if num > 9:
        subs = line.split()
        iter, a, b = int(subs[1]), key_index_list[int(subs[3])-1], key_index_list[int(subs[5])-1]
        for i in range(iter):
            if len(stack[a]) > 0:
                stack[b].insert(0, stack[a][iter-1-i])
                stack[a].pop(iter-1-i)
# Print result
for k,v in enumerate(stack):
    print(stack[v][0],end='')
print("")