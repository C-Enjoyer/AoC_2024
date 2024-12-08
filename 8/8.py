import numpy as np

path = 'input.txt'

g = []

with open(path, 'r') as file:
    for row in file:
        g.append(list(row.strip()))


def isInGrid(coord, m, n):
    return 0 <= coord[0] < m and 0 <= coord[1] < n


def getAntiNodesForAntennas(a1, a2, m, n, recurring):
    x1, y1 = a1
    x2, y2 = a2

    k = (y2 - y1) / (x2 - x1)
    d = y1 - k * x1

    dx = abs(x1 - x2)
    minx = min(x1, x2)
    maxx = max(x1, x2)

    ans = []

    if recurring:
        ans = [a1, a2]

    while True:
        minx -= dx
        y = int(round(k * minx + d))

        if not isInGrid((minx, y), m, n):
            break

        ans.append((minx, y))

        if not recurring:
            break

    while True:
        maxx += dx
        y = int(round(k * maxx + d))

        if not isInGrid((maxx, y), m, n):
            break

        ans.append((maxx, y))

        if not recurring:
            break

    return ans


def getNumAntiNodes(grid, recurring = False):
    antennas = {}
    m = len(grid)
    n = len(grid[0])

    nodes = set()

    for r in range(m):
        for c in range(n):
            if grid[r][c] != '.':
                if grid[r][c] in antennas:
                    antennas[grid[r][c]].append((r, c))
                else:
                    antennas[grid[r][c]] = [(r, c)]

    for _, coords in antennas.items():
        nc = len(coords)
        for i in range(nc - 1):
            for j in range(i + 1, nc):
                for an in getAntiNodesForAntennas(coords[i], coords[j], m, n, recurring):
                    nodes.add(an)

    return len(nodes)


def part1(grid):
    """ part 1 """

    return getNumAntiNodes(grid)

    
def part2(grid):
    """ part 2 """

    return getNumAntiNodes(grid, True)


print(part1(g))
print(part2(g))