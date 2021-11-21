
def main():
    inp = get_input()
    print(check_for_valid_passports(inp))


def get_input():
    f = open("input.txt", "r")
    inp = f.read()
    inp = inp.split("\n\n")
    return inp


def check_for_valid_passports(inp):
    num_of_valid_passports = 0
    inp_dict = {}
    for x in inp:
        if "byr" in x and "iyr" in x and "eyr" in x and "hgt" in x and "hcl" in x and "ecl" in x and "pid" in x:  # this is pretty much the first part
            inp_dict = create_dictionary_for_input(x)
            if 1920 <= int(inp_dict["byr"]) <= 2002 and 2010 <= int(inp_dict["iyr"]) <= 2020 and 2020 <= int(inp_dict["eyr"]) <= 2030:
                if "cm" in inp_dict["hgt"] or "in" in inp_dict["hgt"]:
                    if is_hgt_valid(inp_dict["hgt"]):
                        if is_hcl_valid(inp_dict["hcl"]):
                            if is_ecl_valid(inp_dict["ecl"]):
                                if len(inp_dict["pid"]) == 9 and inp_dict["pid"].isdecimal():
                                    num_of_valid_passports += 1

    return num_of_valid_passports


def create_dictionary_for_input(x):
    inp_dict = {
        "byr": x[x.index("byr") + 4:x.index("byr") + 8],
        "iyr": x[x.index("iyr") + 4:x.index("iyr") + 8],
        "eyr": x[x.index("eyr") + 4:x.index("eyr") + 8],
        "ecl": x[x.index("ecl") + 4:x.index("ecl") + 7],
        # "pid": x[x.index("pid") + 4:x.index("pid") + 13]
    }
    inp_dict.update(get_hgt_and_hcl(x, "hgt", 10))
    inp_dict.update(get_hgt_and_hcl(x, "hcl", 14))
    inp_dict.update(get_hgt_and_hcl(x, "pid", 17))

    return inp_dict


def get_hgt_and_hcl(x, prop, index):
    inp_dict = {}
    try:
        inp_dict.update({prop: x[x.index(prop) + 4:x.index(" ", x.index(prop) + 4, x.index(prop) + index)]})
    except ValueError:
        try:
            inp_dict.update({prop: x[x.index(prop) + 4:x.index("\n", x.index(prop) + 4, x.index(prop) + index)]})
        except ValueError:
            inp_dict.update({prop: x[x.index(prop) + 4:]})

    return inp_dict


def is_hgt_valid(hgt):
    if "cm" in hgt:
        if 150 <= int(hgt[:hgt.index("cm")]) <= 193:
            return True
    elif "in" in hgt:
        if 59 <= int(hgt[:hgt.index("in")]) <= 76:
            return True
    else:
        return False


def is_hcl_valid(hcl):
    ok = "0123456789abcdef"
    if len(hcl) == 7:
        if hcl[0] == "#":
            if all(c in ok for c in hcl[1:]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def is_ecl_valid(ecl):
    if ecl == "amb":
        return True
    elif ecl == "blu":
        return True
    elif ecl == "brn":
        return True
    elif ecl == "gry":
        return True
    elif ecl == "grn":
        return True
    elif ecl == "hzl":
        return True
    elif ecl == "oth":
        return True
    else:
        return False


main()
