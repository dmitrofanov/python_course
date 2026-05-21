list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

set_a = set(list_a)
set_b = set(list_b)

both = set_a & set_b
only_a = set_a - set_b
only_b = set_b - set_a

print(f"Общие: {both}")
print(f"Только в первом: {only_a}")
print(f"Только во втором: {only_b}")