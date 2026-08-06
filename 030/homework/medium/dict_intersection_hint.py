dict_a = {"a": 1, "b": 2, "c": 3, "d": 4}
dict_b = {"x": 2, "y": 4, "z": 6, "w": 1}

common = {}
for key_a, val_a in dict_a.items():
    if val_a in dict_b.values():
        common[key_a] = val_a

print(f"Общие по значениям: {common}")