"""
ЗАДАЧА 2: Найди самое частое слово в тексте

Напиши 4 маленькие функции:
1. split_text(text) - разбивает текст на слова (return text.split())
2. clean_words(words) - убирает знаки препинания и приводит к нижнему регистру. Почитай про метод strip на строках.
3. count_words(words) - считает частоту слов, возвращает словарь {слово: количество}
4. find_most_common(word_counts) - находит слово с максимальной частотой

Обработай текст цепочкой:
find_most_common(count_words(clean_words(split_text(текст))))
"""

def split_text(text):
    return text.split()

def clean_words(words):
    cleaned = []
    for word in words:
        clean_word = word.strip(".,!?;:\"\'()").lower()
        if clean_word:
            cleaned.append(clean_word)
    return cleaned

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def find_most_common(word_counts):
    max_value = 0
    max_word = None
    for word, value in word_counts.items():
        if value > max_value:
            max_value = value
            max_word = word
    return max_word, max_value


print(find_most_common(count_words(clean_words(split_text("я играю     по вечерам в игры,после того как я позанимаюсь, я опять играю в игры")))))

