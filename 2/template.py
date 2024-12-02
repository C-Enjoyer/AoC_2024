path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        nums = [int(x) for x in row.strip().split(' ')]
        l.append(nums)


def isSafe(nums, notSafe):
    n = len(nums)

    if n <= 1:
        return True

    isAsc = nums[1] > nums[0]

    for i in range(1, n):
        dif = nums[i] - nums[i-1]

        if dif == 0:
            notSafe.append(i)
            notSafe.append(i-1)
            return False

        if isAsc and dif < 0:
            notSafe.append(i)
            notSafe.append(i-1)
            return False

        if not isAsc and dif > 0:
            notSafe.append(i)
            notSafe.append(i-1)
            return False

        dif = abs(dif)

        if dif > 3 or dif < 1:
            notSafe.append(i)
            notSafe.append(i-1)
            return False

    return True


def part1(list):
    """ part 1 """

    result = 0

    for nums in list:
        if isSafe(nums, []):
            result += 1

    return result

    
def part2(list):
    """ part 2 """

    result = 0

    for nums in list:
        notSafe = [0]
        if isSafe(nums, notSafe):
            result += 1
        else:
            for ns in notSafe:
                if isSafe(nums[:ns] + nums[ns+1:], []):
                    result += 1
                    break

    return result


print(part1(l))
print(part2(l))
