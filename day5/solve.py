#!/usr/bin/python3
import string

with open("./input") as input:
    Lines = input.read().splitlines()

#[V] [B] [M] [M] [C] [Q] [C] [G] [H]
    # first 8 is the map
    # 9, 10 not needed
    # instructions start at 11

# move 5 from 4 to 7
# move [repetitions] from [A] to [B]

# Print the list
stack = {1:[],5:[],9:[],13:[],17:[],21:[],25:[],29:[],33:[]}
for num, line in enumerate(Lines):
    # Map initial layout
    if num < 8:
        for k, c in enumerate(line):
            if k in [1,5,9,13,17,21,25,29,33] and c in string.ascii_uppercase:
                stack[k].append(c)
    # Solve
    key_index_list = dict(enumerate(stack.keys()))

    if num > 9:
        subs = line.split()
        iter, a, b = int(subs[1]), key_index_list[int(subs[3])-1], key_index_list[int(subs[5])-1]
        for i in range(iter):
            if len(stack[a]) > 0:
                stack[b].insert(0, stack[a][0])
                stack[a].pop(0)
for k,v in enumerate(stack):
    print(stack[v][0],end='')
print("")