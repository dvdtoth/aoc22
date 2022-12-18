#!/opt/homebrew/bin/python3

from collections import deque

grid = []
with open("./input") as input:
    for line in input:
        grid.append(line.strip())
elevation = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
hor = len(grid[0])
ver = len(grid)

for x in range(ver):
    for y in range(hor):
        if grid[x][y] == 'S':
            elevation[x][y] = 1
        elif grid[x][y] == 'E':
            elevation[x][y] = 26
        else:
            elevation[x][y] = ord(grid[x][y]) - ord('a')+1

def bfs():
    q = deque()
    for x in range(ver):
        for y in range(hor):
            if elevation[x][y] == 1:
                q.append(((x,y), 0))
    been = set()
    while q:
        (x,y), dist = q.popleft()
        if (x,y) in been:
            continue
        been.add((x,y))
        if grid[x][y] == 'E':
            return dist
        for dx, dy in [(-1,0), (0,1), (1,0), (0, -1)]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < ver and 0 <= ny < hor and elevation[nx][ny] <= 1+ elevation[x][y]:
                q.append(((nx,ny), dist + 1))

print(bfs())