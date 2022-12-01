#!/usr/bin/python3

input = open('input', 'r')
Lines = input.readlines()
tops = [0,0,0]
total = 0

for line in Lines:
    if line == '\n':
        for key, top in enumerate(tops):
            if tops[key] < total:
                print(tops[key], 'is smaller than', total)
                tops.append(total)
                tops.sort(reverse=True)
                print("sorted: ", tops)
                tops = tops[ : -1]
                break
        total = 0
    else:
      total = total + int(line)

print(sum(tops))
input.close()