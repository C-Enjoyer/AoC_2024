import heapq

path = 'input.txt'

g = []

with open(path, 'r') as file:
    for row in file:
        g.append(list(row.strip()))


def getStart(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return (r, c)
    return None


def getDistances(grid, start):
    q = []
    visited = { (start): 0 }

    heapq.heappush(q, (0, start))

    while q:
        score, (r, c) = heapq.heappop(q)

        if (r, c) in visited and visited[(r, c)] < score:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] != '#':
                np = (r+dr, c+dc)
                if np not in visited or visited[np] > score + 1:
                    visited[np] = score + 1
                    heapq.heappush(q, (score+1, np))

    return visited


def part1(distances):
    """ part 1 """

    result = 0
    cut = 2

    for p in distances:
        for dr in range(-cut, cut + 1):
            for dc in range(-cut, cut + 1):
                if dr == dc == 0 or abs(dr) + abs(dc) > cut:
                    continue
                np = (p[0] + dr, p[1] + dc)
                if np in distances:
                    cost = distances[p] - distances[np]
                    cheatedCost = abs(p[0] - np[0]) + abs(p[1] - np[1])
                    if (cost - cheatedCost) >= 100:
                        result += 1

    return result

    
def part2(distances):
    """ part 2 """

    result = 0
    cut = 20

    for (p1r, p1c), d1 in distances.items():
        for (p2r, p2c), d2 in distances.items():
            if (p1r, p1c) == (p2r, p2c):
                continue
            cost = d2 - d1
            cheatedCost = abs(p1r - p2r) + abs(p1c - p2c)
            if cheatedCost <= cut and (cost - cheatedCost) >= 100:
                result += 1

    return result


s = getStart(g)
d = getDistances(g, s)

print(part1(d))
print(part2(d))
