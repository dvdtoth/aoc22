#!/opt/homebrew/bin/python3
cycle = 0
x = 1
text = str('')

def check_signal():
    global text
    pos = cycle % 40
    print(pos)
    if pos == x or pos == x-1 or pos == x+1:
        text += '#'
    else:
        text += ' '
    if pos == 0:
        text += "\n"

with open("./input") as input:
    for line in input:
        if line[:4] == "noop":
            cycle += 1
            check_signal()
        else:
            op, val = str.split(line, ' ')
            val = int(val)
            if op == "addx":
                cycle += 1
                check_signal()
                x += val
                cycle += 1
                check_signal()

print(text)   