#!/usr/bin/python3
# import readline
# input = open('input', 'r')

input = open('input', 'r')
Lines = input.readlines()
top = 0
sum = 0

for line in Lines:
    if line == '\n':
        if top < sum:
            top = sum
        sum = 0
    else:
      sum = sum + int(line)

print(top)
input.close()