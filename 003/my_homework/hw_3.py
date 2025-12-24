#Создать функцию, которая принимает строку и печатает каждое слово с новой строки. Использовать функции, созданные в заданиях 1 и 2.
def list_of_strings(text):
    words = text.split()
    for word in words:
        print(word)
list_of_strings('h fd gf 333')
