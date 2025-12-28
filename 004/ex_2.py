# Функция find_most_common_word(text)
#     Написать функцию, которая находит слово, встречающееся в тексте чаще всего (без учёта регистра).
#     Что тренируем: Словарь как счётчик, цикл по списку слов, обновление значений в словаре, поиск максимума по значению.

#     Алгоритм:
#         Привести текст к нижнему регистру и разбить на слова.
#         Создать пустой словарь word_count.
#         В цикле for word in words увеличивать счётчик.
#         Найти ключ с максимальным значением (можно через цикл).

def find_most_common_word(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word,0) +1
    max_key = ''
    max_count = 0
    for word,count in word_count.items():
        if count > max_count:
            max_key = word
            max_count = count
    return max_key
print(find_most_common_word('privet privet hi hi hi 8 8 8 8 8 9 9 0 0 0 00 0 0 0 0 '))