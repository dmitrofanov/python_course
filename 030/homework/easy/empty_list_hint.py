def is_empty(lst):
    return not lst

tests = [[], [1, 2, 3], [], ["a"]]

for test in tests:
    print(f"{test}: {'пустой' if is_empty(test) else 'не пустой'}")