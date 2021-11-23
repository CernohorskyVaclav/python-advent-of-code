
def main():
    print(get_number_of_bags(get_input()))
    print(get_all_bags(get_input()))


# ------------------------------
# part 1
# ------------------------------


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
    return bag_list


# ------------------------------
# part 2
# ------------------------------


def get_all_bags(inp):
    for x in range(len(inp)):
        inp[x] = inp[x].replace(".", "")
        inp[x] = inp[x].replace(" bags", "")
        inp[x] = inp[x].replace(" bag", "")
        inp[x] = inp[x].split(" contain ")
        inp[x][1] = inp[x][1].split(", ")

    bag_dict = dict()
    for x in inp:
        if "no" in x[1][0]:
            bag_dict.update({x[0]: ""})
        else:
            bag_dict.update({x[0]: []})
            for y in range(len(x[1])):
                bag_dict[x[0]].append({"count": int(x[1][y][:x[1][y].index(" ")]), "type": x[1][y][x[1][y].index(" ") + 1:]})

    return bag_count(bag_dict, "shiny gold")


# got the bag_count() method from https://auth0.com/blog/advent-of-code-tips-tricks/. feel pretty ashamed.
# but to be honest, I don't think I understood the problem really well.
# I am however proud of my conversion of the list to the dictionary. I never really used a dictionary before.
def bag_count(bag_collection, bag_name):
    count = 0
    top_level_bag = bag_collection[bag_name]
    print(f"Currently counting bags inside {bag_name}.")

    if len(top_level_bag) == 0:
        # Base case: There are no bags inside the current bag.
        # Stop counting.
        return 0
    else:
        # Recursive case: There are bags inside the current bag.
        # Count them, and their contents.
        for current_bag in top_level_bag:
            print(f"There are {current_bag['count']} of {current_bag['type']} inside {bag_name}.")
            # Add the number of bags of the current type
            # to the count.
            current_bag_type_count = current_bag['count']
            count += current_bag_type_count
            # Count the bags inside each bag of the current type,
            # multiply it by the number of the current type,
            # then add it to the count.
            bags_inside_current_bag_type_count = bag_count(bag_collection, current_bag["type"])
            count += bags_inside_current_bag_type_count * current_bag_type_count

    return count


def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    return inp


main()
