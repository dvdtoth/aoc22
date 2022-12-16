#!/opt/homebrew/bin/python3
cycle = 0
x = 1
signal = 0

def check_signal():
    global signal
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal += x * cycle

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
                cycle += 1
                check_signal()
                x += val
print(signal)