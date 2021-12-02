from util import get_filename


def part1(data):
    result = 0
    prev = float("inf")

    for num in data:
        if num > prev:
            result += 1
        prev = num

    return result


def part2(data):
    windows = []
    for i in range(0, len(data) - 2):
        windows.append(data[i] + data[i + 1] + data[i + 2])

    return part1(windows)


def main():
    with open(get_filename()) as file:
        inp = [int(line) for line in file]
    print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    main()
