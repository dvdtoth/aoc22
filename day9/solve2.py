#!/opt/homebrew/bin/python3

# position x row, y col
positions = set()
hx, hy, tx, ty = 0, 0, 0, 0

global rope
rope = [[0,0] for _ in range(10)]

sign = lambda x : 1 if x > 0 else ( -1 if x < 0 else 0)

moves = {
    'U': (0,1),
    'D': (0,-1),
    'R': (1,0),
    'L': (-1,0)
}

def move_knot(i):
    global rope
    hx, hy = rope[i-1]
    tx, ty = rope[i]
    dx = tx-hx
    dy = ty-hy
    if dx == 0 or dy == 0:
        if abs(dx) >= 2:
            rope[i][0] -= sign(dx)
        if abs(dy) >= 2:
            rope[i][1] -= sign(dy)
    elif abs(dx) != 1 or abs(dy) != 1:
        rope[i][0] -= sign(dx)
        rope[i][1] -= sign(dy)

    return tx, ty


with open("./input") as input:
    for line in input:
        dir, dist = str.split(line, ' ')
        dist = int(dist)
        positions.add(tuple(rope[-1]))

        for _ in range(dist):
            dx, dy = moves[dir]
            rope[0][0] += dx
            rope[0][1] += dy
            for i in range(1,10):
                move_knot(i)
            positions.add(tuple(rope[-1]))

print(len(positions))

