"""
Проверь, пустой ли список, не используя len().
tests это список списков, где каждый внутренний список
нужно проверить на пустоту.
"""
def is_empty(test):
    return not test

tests = [[], [1, 2, 3], [], ["a"]]

for test in tests:
    print(f"{test}: {'пустой' if is_empty(test) else 'не пустой'}")
