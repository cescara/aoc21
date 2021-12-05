from util import get_filename


def play(number, boards):
    winners = []
    for board in boards:
        for line in board:
            for i, entry in enumerate(line):
                if number == entry[0]:
                    entry[1] = True
                    if all(e[1] for e in line) or all(l[i][1] for l in board):
                        winners.append(board)
    return winners


def final_score(number, winner):
    return sum([sum([e[0] for e in line if not e[1]]) for line in winner]) * number


def part1(numbers, boards):
    for number in numbers:
        winners = play(number, boards)
        if winners:
            break
    else:
        raise ValueError("No winner, that can't be right :O")

    return final_score(number, winners[0])


def part2(numbers, boards):
    for number in numbers:
        winners = play(number, boards)

        if winners:
            for winner in winners:
                boards.remove(winner)
            if not boards:
                break
    else:
        raise ValueError("No winner, that can't be right :O")

    return final_score(number, winners[-1])


def main():
    with open(get_filename()) as file:
        numbers = [int(num) for num in file.readline().strip().split(",")]
        raw_boards = file.read().split("\n\n")

    boards = []
    for raw_board in raw_boards:
        board = []
        for line in [l for l in raw_board.split("\n") if l]:
            board.append([[int(num), False] for num in line.split()])
        boards.append(board)

    print(part1(numbers, boards))

    for board in boards:
        for line in board:
            for entry in line:
                entry[1] = False

    print(part2(numbers, boards))


if __name__ == '__main__':
    main()
