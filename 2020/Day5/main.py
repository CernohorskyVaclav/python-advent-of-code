
def main():
    inp = get_input()
    pass_ids = get_the_ids(inp)
    pass_ids.sort()
    print(get_your_id(pass_ids))


def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    return inp


def get_the_ids(inp):
    id_num = []
    for x in inp:
        row = get_row(x[:7])
        column = get_column(x[-3:])
        pass_id = row * 8 + column
        id_num.append(pass_id)

    return id_num


def get_row(y):
    num = list(range(0, 128))
    for x in y:
        if x == "F":
            del num[int((len(num)/2)):]
        elif x == "B":
            del num[:int((len(num)/2))]

    return num[0]


def get_column(y):
    num = list(range(0, 8))
    for x in y:
        if x == "L":
            del num[int((len(num) / 2)):]
        elif x == "R":
            del num[:int((len(num) / 2))]

    return num[0]


def get_your_id(pass_ids):
    return [x for x in range(pass_ids[0], pass_ids[-1] + 1)
            if x not in pass_ids]


main()
