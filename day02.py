from util import get_filename


def part1(commands):
    pos = depth = 0
    for command, value in commands:
        if command == "forward":
            pos += value
        elif command == "up":
            depth -= value
        elif command == "down":
            depth += value
        else:
            raise ValueError(f"{command} doesn't exist")

    return pos * depth


def part2(commands):
    pos = depth = aim = 0
    for command, value in commands:
        if command == "forward":
            pos += value
            depth += (aim * value)
        elif command == "up":
            aim -= value
        elif command == "down":
            aim += value
        else:
            raise ValueError(f"{command} doesn't exist")

    return pos * depth


def main():
    with open(get_filename()) as file:
        inp = [(line.split()[0], int(line.split()[1])) for line in file]
    print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    main()
