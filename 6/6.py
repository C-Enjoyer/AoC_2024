import bisect
import copy

path = 'input.txt'

g = []

with open(path, 'r') as file:
    for row in file:
        g.append(list(row.strip()))


def analizeGrid(grid):
    m = len(grid)
    n = len(grid[0])
    dir = ''
    pos = (0, 0)
    rowObs = [[] for _ in range(m)]
    colObs = [[] for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '#':
                rowObs[r].append(c)
                colObs[c].append(r)
            if grid[r][c] in ['^', '>', 'v', '<']:
                dir = grid[r][c]
                pos = (r, c)

    return m, n, rowObs, colObs, dir, pos


def getLines(gridInfo):
    m, n, rowObs, colObs, dir, pos = gridInfo

    turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    curr = pos[0]
    curc = pos[1]
    lines = set()

    while 1:
        if dir == 'v':
            nextObs = m
            for obs in colObs[curc]:
                if obs > curr:
                    nextObs = obs
                    break

            newLine = (dir, curc, curr, nextObs - 1)
            if newLine in lines:
                return []
            lines.add(newLine)

            if nextObs == m:
                break

            curr = nextObs - 1

        elif dir == '^':
            nextObs = -1
            for obs in colObs[curc][::-1]:
                if obs < curr:
                    nextObs = obs
                    break

            newLine = (dir, curc, curr, nextObs + 1)
            if newLine in lines:
                return []
            lines.add(newLine)

            if nextObs == -1:
                break

            curr = nextObs + 1

        elif dir == '>':
            nextObs = n
            for obs in rowObs[curr]:
                if obs > curc:
                    nextObs = obs
                    break

            newLine = (dir, curr, curc, nextObs - 1)
            if newLine in lines:
                return []
            lines.add(newLine)

            if nextObs == n:
                break

            curc = nextObs - 1

        elif dir == '<':
            nextObs = -1
            for obs in rowObs[curr][::-1]:
                if obs < curc:
                    nextObs = obs
                    break

            newLine = (dir, curr, curc, nextObs + 1)
            if newLine in lines:
                return []
            lines.add(newLine)

            if nextObs == -1:
                break

            curc = nextObs + 1

        dir = turn[dir]

    return lines


def getPath(lines):
    visited = set()

    for dir, fixed, start, end in lines:
        if dir == '^':
            for r in range(start, end - 1, -1):
                visited.add((r, fixed))
        elif dir == 'v':
            for r in range(start, end + 1):
                visited.add((r, fixed))
        elif dir == '<':
            for c in range(start, end - 1, -1):
                visited.add((fixed, c))
        elif dir == '>':
            for c in range(start, end + 1):
                visited.add((fixed, c))

    return visited


def part1(path):
    """ part 1 """
    return len(path)


def part2(path, gridInfo):
    """ part 2 """

    m, n, rowObs, colObs, dir, pos = gridInfo
    result = 0

    path.remove(pos)
    path = list(path)

    for i in range(len(path)):
        newRowObs = copy.deepcopy(rowObs)
        newColObs = copy.deepcopy(colObs)

        bisect.insort(newRowObs[path[i][0]], path[i][1])
        bisect.insort(newColObs[path[i][1]], path[i][0])

        if len(getLines((m, n, newRowObs, newColObs, dir, pos))) == 0:
            result += 1

    return result


gi = analizeGrid(g)
p = getPath(getLines(gi))
print(part1(p))
print(part2(p, gi))
