import sys

path = 'input.txt'

g = []

with open(path, 'r') as file:
    for row in file:
        g.append(list(row.strip()))


def findStartEnd(grid):
    start, end = None, None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = (r, c)
                if end:
                    return start, end
            elif grid[r][c] == 'E':
                end = (r, c)
                if start:
                    return start, end

    return None, None


def findRoutes(grid, start, end):

    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    routes = []
    visited = {}

    queue = [(start, [start], 0, 0)]
    while queue:
        (r, c), history, score, dir = queue.pop(0)

        if (r, c) == end:
            routes.append((history, score))
            continue

        if ((r, c), dir) in visited and visited[((r, c), dir)] < score:
            continue

        visited[((r, c), dir)] = score

        for _dir, (dr, dc) in enumerate(dirs):
            if (dir + 2) % 4 == _dir:
                continue

            nr, nc = r + dr, c + dc
            if grid[nr][nc] != "#" and (nr, nc) not in history:
                if _dir == dir:
                    queue.append(((nr, nc), history + [(nr, nc)], score + 1, _dir))
                else:
                    queue.append(((r, c), history, score + 1000, _dir))

    return routes


def part1(routes):
    """ part 1 """

    best = sys.maxsize
    for route in routes:
        best = min(best, route[1])

    return best

    
def part2(routes):
    """ part 2 """

    best = sys.maxsize
    tiles = set()

    for route in routes:
        if route[1] < best:
            best = route[1]
            tiles = set(route[0])
        elif route[1] == best:
            tiles |= set(route[0])

    return len(tiles)


s, e = findStartEnd(g)
r = findRoutes(g, s, e)
print(part1(r))
print(part2(r))
