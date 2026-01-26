# 5) Напиши функцию words, которая принимает предложение (строку) и возвращает список слов в этом предложении.

def words(text):
    return text.split()
print(words('slovo1 slovo2 slovo3'))