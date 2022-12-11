#!/opt/homebrew/bin/python3

# position x row, y col
positions = set()
hx, hy, tx, ty = 0, 0, 0, 0

sign = lambda x : 1 if x > 0 else ( -1 if x < 0 else 0)

def move_head(dir, hx, hy):
    if dir == 'U':
        hy = hy + 1
    if dir == 'D':
        hy = hy - 1
    if dir == 'R':
        hx = hx + 1
    if dir == 'L':
        hx = hx - 1
    return hx, hy

def move_tail(tx, ty, hx, hy):
    # Distance
    dx = tx-hx
    dy = ty-hy
    if dx == 0 or dy == 0:
        if abs(dx) >= 2:
            tx -= sign(dx)
        if abs(dy) >= 2:
            ty -= sign(dy)
    elif abs(dx) != 1 or abs(dy) != 1:
        tx -= sign(dx)
        ty -= sign(dy)

    positions.add((tx,ty))

    return tx, ty


with open("./input") as input:
    for line in input:
        dir, dist = str.split(line, ' ')
        dist = int(dist)
        # move head
        for _ in range(dist):
            hx, hy = move_head(dir, hx, hy)
            tx, ty = move_tail(tx, ty, hx, hy)

print(len(positions))

