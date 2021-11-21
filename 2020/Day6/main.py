
def main():
    print(get_sum_of_counts(get_input()))


def get_sum_of_counts(inp):
    all_counts = []
    for x in inp:
        all_counts.append(get_count(x))
    return sum(all_counts)


def get_count(group):
    group_yes = str()
    count_of_yeses = int()
    for x in group[0]:
        for y in range(len(group)):
            if y > 0:
                if x in group[y]:
                    count_of_yeses += 1

        if count_of_yeses == len(group) - 1:
            group_yes += x

        count_of_yeses = 0

    return len(group_yes)


def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n\n")
    for x in range(len(inp)):
        inp[x] = inp[x].split("\n")
    return inp


main()
