from util import get_filename

ZERO = "0"
ONE = "1"


def part1(report):
    gamma = epsilon = ""

    for i in range(len(report[0])):
        switch = 0
        for line in report:
            if line[i] == ZERO:
                switch -= 1
            elif line[i] == ONE:
                switch += 1
            else:
                raise ValueError("Wrong input!")

        if switch > 0:
            gamma += ONE
            epsilon += ZERO
        elif switch < 0:
            gamma += ZERO
            epsilon += ONE
        else:
            raise ValueError("No most/least common bit D:")

    return int(gamma, 2) * int(epsilon, 2)


def reduce(lines, pos, param):
    balance = 0
    for line in lines:
        if line[pos] == ZERO:
            balance -= 1
        elif line[pos] == ONE:
            balance += 1
        else:
            raise ValueError("Wrong input!")

    if balance >= 0:
        switch = ONE if param == 1 else ZERO
    else:
        switch = ZERO if param == 1 else ONE

    reduced = [line for line in lines if line[pos] == switch]

    if len(reduced) > 1:
        return reduce(reduced, pos + 1, param)

    return reduced[0]


def part2(report):
    oxygen = reduce(report, 0, 1)
    co2 = reduce(report, 0, 0)

    return int(oxygen, 2) * int(co2, 2)


def main():
    with open(get_filename()) as file:
        inp = [line.strip() for line in file]

    print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    main()
