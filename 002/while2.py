invitation = 'Введите число чтобы добавить его в список или stop, чтобы выйти: '
answer = input(invitation)
numbers = []
while answer != 'stop':
    numbers.append(int(answer))
    answer = input(invitation)

# print(numbers)WWW
print('Сумма всех введённых чисел:', sum(numbers))