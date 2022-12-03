#!/usr/bin/python3
import string

with open("./input") as input:
    Lines = input.read().splitlines()

#1-26
string.ascii_lowercase
#27-52
string.ascii_uppercase

total, member = 0, {}

for key, line in enumerate(Lines):
    member[key % 3] = set(sorted(line))
    if key % 3 == 2:
        badge = "".join(member[0].intersection(member[1], member[2]))
        if badge in string.ascii_lowercase:
             total += string.ascii_lowercase.find(badge) + 1
        if badge in string.ascii_uppercase:
             total += string.ascii_uppercase.find(badge) + 27
print(total)