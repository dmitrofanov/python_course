numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
target_diff = 2

pairs = []
used = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if abs(numbers[i] - numbers[j]) == target_diff:
            pair = tuple(sorted([numbers[i], numbers[j]]))
            if pair not in pairs:
                pairs.append(pair)

print(f"Пары с разностью {target_diff}: {pairs}")