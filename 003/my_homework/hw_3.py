#Создать функцию, которая принимает строку и печатает каждое слово с новой строки. Использовать функции, созданные в заданиях 1 и 2.
def list_of_str(text):
    return text.split()
def list_of_words(words):
    for word in words:
        print(word)
def list_of_strings(text):
    words = list_of_str(text)
    list_of_words(words)
list_of_strings('h fd gf 333')
