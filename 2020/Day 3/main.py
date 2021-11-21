
def main():
    # get the input and make it wider 32 times
    inp = extend_input(get_input())
    answer = 1
    answer *= get_number_of_trees(inp, 1, 1)
    answer *= get_number_of_trees(inp, 3, 1)
    answer *= get_number_of_trees(inp, 5, 1)
    answer *= get_number_of_trees(inp, 7, 1)
    answer *= get_number_of_trees(inp, 1, 2)
    print(answer)


def get_input():
    f = open("input.txt", "r")
    inp = f.read()
    inp = inp.split("\n")
    return inp


def extend_input(inp):
    for x in range(len(inp)):
        inp[x] = inp[x] * 200
    return inp


def get_number_of_trees(inp, right, down):
    num_of_trees = 0
    for x in range(len(inp)):
        if 0 <= x < len(inp)/down:
            if inp[x*down][x*right] == '#':
                num_of_trees += 1

    return num_of_trees


main()
