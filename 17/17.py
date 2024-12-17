path = 'input.txt'

ra, rb, rc = 0, 0, 0
p = []

with open(path, 'r') as file:
    for row in file:
        if row.startswith("Register A: "):
            ra = int(row.strip().split(": ")[1])
        elif row.startswith("Register B: "):
            rb = int(row.strip().split(": ")[1])
        elif row.startswith("Register C: "):
            rc = int(row.strip().split(": ")[1])
        elif row.startswith("Program: "):
            p = [int(x) for x in row.strip().split(": ")[1].split(",")]


def runProgram(rega, regb, regc, program):
    def getCombo(oper):
        if 0 <= oper <= 3:
            return oper
        elif oper == 4:
            return rega
        elif oper == 5:
            return regb
        elif oper == 6:
            return regc
        else:
            return -1

    pt = 0
    n = len(program)
    output = []

    while pt < n:
        ins = program[pt]
        oper = program[pt + 1]

        if ins == 0:
            rega = rega // (2 ** getCombo(oper))
        elif ins == 1:
            regb ^= oper
        elif ins == 2:
            regb = getCombo(oper) % 8
        elif ins == 3:
            if rega != 0:
                pt = oper - 2
        elif ins == 4:
            regb ^= regc
        elif ins == 5:
            output.append(getCombo(oper) % 8)
        elif ins == 6:
            regb = rega // (2 ** getCombo(oper))
        elif ins == 7:
            regc = rega // (2 ** getCombo(oper))

        pt += 2

    return output


def part1(rega, regb, regc, program):
    """ part 1 """

    return ",".join(str(x) for x in runProgram(rega, regb, regc, program))


def part2(program):
    """ part 2 """

    possible = [0]
    n = len(program)

    for i in range(n):
        nextPossible = []

        for a in possible:
            for posa in range(a * 8, a * 8 + 8):
                if runProgram(posa, 0, 0, program) == program[n - 1 - i:]:
                    nextPossible.append(posa)

        possible = nextPossible

    return min(possible)


print(part1(ra, rb, rc, p))
print(part2(p))
