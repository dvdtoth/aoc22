#!/usr/bin/python3
import string

with open("./input") as input:
    Lines = input.read().splitlines()

#1-26
string.ascii_lowercase
#27-52
string.ascii_uppercase

total = 0

for line in Lines:
    first, second = set(sorted(line[:len(line)//2])), set(sorted(line[len(line)//2:]))
    for letter in first:
        if letter in second:
            print(letter, type(letter))
            if letter in string.ascii_lowercase:
                total += string.ascii_lowercase.find(letter) + 1
            if letter in string.ascii_uppercase:
                total += string.ascii_uppercase.find(letter) + 27
print(total)