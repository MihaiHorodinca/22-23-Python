# Ex 1
# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)

def f1(a, b):
    set_a = set()
    set_b = set()

    for el in a:
        set_a.add(el)

    for el in b:
        set_b.add(el)

    return [set_a.intersection(set_b), set_a.union(set_b), set_a.difference(set_b), set_b.difference(set_a)]


# print(f1([1, 2, 3], [3, 4, 5]))


# Ex 2
# 2. Write a function that receives a string as a parameter and returns a dictionary in which
# the keys are the characters in the character string and
# the values are the number of occurrences of that character in the given text.

def f2(string):
    result = dict()

    for char in string:
        if char in result.keys():
            result[char] = result[char] + 1
        else:
            result[char] = 1

    return result


# print(f2("mamabcam"))


# Ex 3
# 3. Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other containers,
# such as dictionaries, lists, sets, etc.)

def f3(dict_a, dict_b):
    return not (dict_a != dict_b)


print(f3({1, 2}, {1, 2}))


# Ex 5
# 5. The validate_dict function that receives as a parameter a set of tuples
# (that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if
# it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules, False otherwise.

def f5(rules, to_check):
    dict_rules = dict()

    for rule in rules:
        k, r1, r2, r3 = rule
        dict_rules[k] = (r1, r2, r3)

    for (key, string) in list(to_check.items()):
        if key in dict_rules.keys():
            r1, r2, r3 = dict_rules[key]

            if not string.startswith(r1):
                return False
            if not string.startswith(r2, 1, len(string) - 1):
                return False
            if not string.endswith(r3):
                return False

    return True


# print(f5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
#          {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))


# Ex 6
# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing the number of duplicate elements in the list
# (use sets to achieve this objective).


def f6(my_list):
    unique = set()
    multiple = set()

    for el in my_list:
        if el in unique:
            unique.remove(el)
            multiple.add(el)
        else:
            if not el in multiple:
                unique.add(el)

    return len(unique), len(multiple)


# print(f6([1, 2, 3, 1, 5, 21]))


# Ex 7
# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -.

def f7(*sets):
    sets = list(sets)
    print(sets)
    result = dict()

    for i in range(0, len(sets)):
        for j in range(i + 1, len(sets)):
            set_a = sets[i]
            set_b = sets[j]

            intersection_str = str(set_a) + " & " + str(set_b)
            intersection_set = set_a.intersection(set_b)
            result[intersection_str] = intersection_set

            union_str = str(set_a) + " | " + str(set_b)
            union_set = set_a.union(set_b)
            result[union_str] = union_set

            diff_str_a = str(set_a) + " - " + str(set_b)
            diff_set_a = set_a.difference(set_b)
            result[diff_str_a] = diff_set_a

            diff_str_b = str(set_b) + " - " + str(set_a)
            diff_set_b = set_b.difference(set_a)
            result[diff_str_b] = diff_set_b

    return result


# print(f7({1, 2}, {2, 3}))


# Ex 8
# 8. Write a function that receives a single dict parameter named mapping. This dictionary always contains
# a string key "start". Starting with the value of this key you must obtain a list of objects by iterating
# over mapping in the following way: the value of the current key is the key for the next value, until you find a loop
# (a key that was visited before). The function must return the list of objects obtained as previously described.


def f8(mapping):
    value = "start"
    visited = list()
    visited.append("start")

    while not mapping[value] in visited:
        value = mapping[value]
        visited.append(value)

    visited.remove("start")
    return visited

# print(f8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# Ex 9
# 9. Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
# and will return the number of positional arguments whose values can be found among keyword arguments values.

def f9(*args, **kwargs):
    result = 0

    for el in args:
        if el in kwargs.values():
            result += 1

    return result


# print(f9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
