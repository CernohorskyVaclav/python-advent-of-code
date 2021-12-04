
def main():
    inp = get_input()
    print(part_one(inp))
    print(part_two(inp))


def part_one(inp):
    inp = inp.split("\n")
    one = 0
    zero = 0
    gamma = str()  # most common
    epsilon = str()  # least common
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[y][x] == "1":
                one += 1
            elif inp[y][x] == "0":
                zero += 1
            else:
                print("error, wrong input (neither 0 or 1)")
        if one < zero:
            gamma += "0"
            epsilon += "1"
        elif zero < one:
            gamma += "1"
            epsilon += "0"
        else:
            print("error, gamma and epsilon are equal")
        one = 0
        zero = 0

    return int(gamma, 2) * int(epsilon, 2)


def part_two(inp):
    listo = [len(inp[0])]
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            listo[x].append(inp[y][x])
    return listo


def get_input():
    f = open("input.txt", "r")
    inp = f.read()

    return inp


main()
