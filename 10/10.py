path = 'input.txt'

g = []

with open(path, 'r') as file:
    for row in file:
        r = []
        for c in row.strip():
            if c.isdigit():
                r.append(int(c))
            else:
                r.append(c)
        g.append(r)


def part1(grid):
    """ part 1 """
    m = len(grid)
    n = len(grid[0])

    def getScore(r, c, finishes, prevH = -1):
        if not (0 <= r < m and 0 <= c < n):
            return len(finishes)
        if prevH + 1 != grid[r][c]:
            return len(finishes)
        if grid[r][c] == 9:
            finishes.add((r, c))
            return len(finishes)

        score = 0
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            score = getScore(r + dr, c + dc, finishes, grid[r][c])

        return score

    result = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] != 0:
                continue

            result += getScore(r, c, set())

    return result


def part2(grid):
    """ part 2 """
    m = len(grid)
    n = len(grid[0])

    def getScore(r, c, score = 0, prevH = -1):
        if not (0 <= r < m and 0 <= c < n):
            return score
        if prevH + 1 != grid[r][c]:
            return score
        if grid[r][c] == 9:
            score += 1

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            score = getScore(r + dr, c + dc, score, grid[r][c])

        return score

    result = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] != 0:
                continue
            result += getScore(r, c)

    return result


print(part1(g))
print(part2(g))
