
def main():
    print(get_number_of_bags(get_input()))


def get_number_of_bags(inp):
    inp = inp
    bag_list = list()
    x = 0
    while x < len(inp):
        if "shiny gold bag" in inp[x][inp[x].index("contain"):]:
            bag_list.append(inp[x][:inp[x].index("s contain")])
            inp.pop(x)
            x -= 1
        x += 1

    return get_list_of_required_bags(inp, bag_list)


def get_list_of_required_bags(inp, bag_list):
    for y in bag_list:
        x = 0
        while x < len(inp):
            if y in inp[x][inp[x].index("contain"):]:
                bag_list.append(inp[x][:inp[x].index("s contain")])
                inp.pop(x)
                x -= 1
            x += 1
    return len(bag_list)


def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    return inp


main()
