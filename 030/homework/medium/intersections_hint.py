list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [3, 5, 7]
list_c = [3, 5, 8]

def contains_all(main_list, sub_list):
    return set(sub_list) <= set(main_list)

print(f"А: {list_a}")
print(f"Б: {list_b} -> {contains_all(list_a, list_b)}")
print(f"В: {list_c} -> {contains_all(list_a, list_c)}")