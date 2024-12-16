path = 'input.txt'

g = []
mo = []

with open(path, 'r') as file:
    for row in file:
        if row[0] == '#':
            g.append(list(row.strip()))
        elif row[0] in '^>v<':
            for c in row.strip():
                mo.append(c)


def findRobot(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                return r, c

    return None

def expandGrid(grid):
    m = len(grid)
    n = len(grid[0])

    newGrid = [['.'] * 2 * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '#':
                newGrid[r][c * 2] = '#'
                newGrid[r][c * 2 + 1] = '#'
            elif grid[r][c] == 'O':
                newGrid[r][c * 2] = '['
                newGrid[r][c * 2 + 1] = ']'
            elif grid[r][c] == '@':
                newGrid[r][c * 2] = '@'

    return newGrid


def isValid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "#"


def isMoveable(grid, row, col, dr, dc, seen):
    if (row, col) in seen:
        return True
    seen.add((row, col))

    nr, nc = row + dr, col + dc
    match grid[nr][nc]:
        case "#":
            return False
        case "[":
            return isMoveable(grid, nr, nc, dr, dc, seen) and isMoveable(
                grid, nr, nc + 1, dr, dc, seen
            )
        case "]":
            return isMoveable(grid, nr, nc, dr, dc, seen) and isMoveable(
                grid, nr, nc - 1, dr, dc, seen
            )
        case "O":
            return isMoveable(grid, nr, nc, dr, dc, seen)
    return True


def doMove(grid, row, col, move):
    dr, dc = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[move]

    nr, nc = row + dr, col + dc

    if not isValid(grid, nr, nc):
        return row, col

    if grid[nr][nc] in ["[", "]", "O"]:
        seen = set()

        if not isMoveable(grid, row, col, dr, dc, seen):
            return row, col

        while len(seen) > 0:
            for r, c in seen.copy():
                nr2, nc2 = r + dr, c + dc
                if (nr2, nc2) not in seen:
                    if grid[nr2][nc2] != "@" and grid[r][c] != "@":
                        grid[nr2][nc2] = grid[r][c]
                        grid[r][c] = "."

                    seen.remove((r, c))

        grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
        return nr, nc

    grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
    return nr, nc


def part1(grid, moves, robot):
    """ part 1 """

    for move in moves:
        robot = doMove(grid, robot[0], robot[1], move)

    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                result += 100 * r + c

    return result

    
def part2(grid, moves, robot):
    """ part 2 """

    for move in moves:
        robot = doMove(grid, robot[0], robot[1], move)

    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '[':
                result += 100 * r + c

    return result


r1 = findRobot(g)
ng = expandGrid(g)
r2 = findRobot(ng)
print(part1(g, mo, r1))
print(part2(ng, mo, r2))
