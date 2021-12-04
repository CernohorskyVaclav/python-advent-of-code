
def main():
    print("part one: ", part_one(get_input()))
    print("part two: ", part_two(get_input()))


def part_one(inp):
    num = 0
    for x in range(len(inp)):
        if x == 0:
            continue
        else:
            if inp[x - 1] < inp[x]:
                num += 1

    return num


def part_two(inp):
    inp = list(map(int, inp))
    num = 0
    iterator = 0
    first = int()
    second = int()
    for x in range(len(inp) - 3):
        first = inp[x] + inp[x + 1] + inp[x + 2]
        second = inp[x + 1] + inp[x + 2] + inp[x + 3]
        if first < second:
            num += 1

    return num


def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    return inp


main()
