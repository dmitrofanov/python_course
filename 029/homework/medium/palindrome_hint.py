def is_palindrome(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[-(i + 1)]:
            return False
    return True

tests = [
    [1, 2, 3, 2, 1],
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c', 'b', 'a'],
    ['a', 'b', 'c', 'd', 'e']
]

for test in tests:
    print(f"{test}: {'палиндром' if is_palindrome(test) else 'не палиндром'}")