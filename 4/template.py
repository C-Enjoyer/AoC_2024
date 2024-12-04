path = 'input.txt'

g = []

with open(path, 'r') as file:
    for row in file:
        g.append(list(row.strip()))


def getSafe(grid, m, n, r, c):
    if not (0 <= r < m):
        return ''
    if not (0 <= c < n):
        return ''
    return grid[r][c]


def part1(grid):
    """ part 1 """
    result = 0

    word = "XMAS"
    m = len(grid)
    n = len(grid[0])

    for r in range(m):
        for c in range(n):
            if grid[r][c] == word[0]:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        found = True
                        curr = r
                        curc = c
                        for letter in word[1:]:
                            curr += dr
                            curc += dc
                            if getSafe(grid, m, n, curr, curc) != letter:
                                found = False
                                break

                        if found:
                            result += 1

    return result

    
def part2(grid):
    """ part 2 """
    result = 0

    m = len(grid)
    n = len(grid[0])

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 'A':
                ms = 0
                ss = 0
                for dr, dc in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    letter = getSafe(grid, m, n, r + dr, c + dc)
                    if letter == 'M':
                        ms += 1
                    elif letter == 'S':
                        ss += 1

                if ms == ss == 2 and grid[r - 1][c - 1] != grid[r + 1][c + 1]:
                    result += 1

    return result


print(part1(g))
print(part2(g))