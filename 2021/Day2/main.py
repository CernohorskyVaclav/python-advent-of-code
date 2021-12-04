
def main():
    inp = get_input()
    print(part_one(inp))
    print(part_two(inp))


# part one
def part_one(inp):
    hor = 0  # horizontal position
    depth = 0
    for x in inp:
        if x[0] == "forward":
            hor += int(x[1])
        elif x[0] == "down":
            depth += int(x[1])
        elif x[0] == "up":
            depth -= int(x[1])
        else:
            print("error in get_hor_pos_and_depth(inp), didn't get the correct command input")

    return hor * depth


# part two
def part_two(inp):
    hor = 0  # horizontal position
    depth = 0
    aim = 0
    for x in inp:
        if x[0] == "forward":
            hor += int(x[1])
            depth += aim * int(x[1])
        elif x[0] == "down":
            aim += int(x[1])
        elif x[0] == "up":
            aim -= int(x[1])
        else:
            print("error in get_hor_pos_and_depth(inp), didn't get the correct command input")

    return hor * depth


def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    for x in range(len(inp)):
        inp[x] = inp[x].split(" ")

    return inp


main()
