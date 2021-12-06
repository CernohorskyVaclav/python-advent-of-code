import operator

def main():
    inp = get_input()
    print(part_one(inp))
    print(part_two(inp))


def part_one(inp):
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
    ogr = get_ogr_ang_csr(inp, operator.gt, "0")  # oxygen generator rating
    scr = get_ogr_ang_csr(inp, operator.lt, "1")  # CO2 scrubber rating

    return int(ogr, 2) * int(scr, 2)


def get_ogr_ang_csr(inp, operation, if_equal):
    one = 0
    zero = 0
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[y][x] == "1":
                one += 1
            elif inp[y][x] == "0":
                zero += 1
            else:
                print("error, wrong input (neither 0 or 1)")
        if operation(one, zero):                 # --v-- this is what you want to be removed
            inp = list(filter(lambda val: val[x] != "0", inp))
            one = 0
            zero = 0
        elif operation(zero, one):               # --v-- this is what you want to be removed
            inp = list(filter(lambda val: val[x] != "1", inp))
            one = 0
            zero = 0
        else:
            inp = list(filter(lambda val: val[x] != if_equal, inp))
            one = 0
            zero = 0

        if len(inp) == 1:
            return inp[0]


def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")

    return inp


main()
