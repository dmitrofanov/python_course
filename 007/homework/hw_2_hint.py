def split_text(text):
    return text.split()

def clean_words(words):
    cleaned = []
    for word in words:
        # Убираем знаки препинания вокруг слова
        clean_word = word.strip(".,!?;:\"\'()").lower()
        if clean_word:  # Не добавляем пустые строки
            cleaned.append(clean_word)
    return cleaned

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        ### альтернативно можно было записать предыдущие 4 строчки в одну строку так:
        ### counts[word] = counts.get(word, 0) + 1
    return counts

def find_most_common(word_counts):
    if not word_counts:
        return None
    # Находим ключ с максимальным значением
    max_word = ''
    max_count = 0
    for word, count in word_counts.items():
        if count > max_count:
            max_word = word
            max_count = count
    return max_word
    ### альтернативно можно было найти максимум в одну строчку вот так:
    ### return max(word_counts.items(), key=lambda x: x[1])[0]

# Текст для анализа
text = "Быстрый рыжий лис прыгает через ленивую собаку. Лис очень быстрый!"

# Обработка цепочкой
most_common = find_most_common(count_words(clean_words(split_text(text))))
print(f"Самое частое слово: '{most_common}'")

# Посмотрим промежуточные результаты
words = split_text(text)
print(f"Слова: {words}")
clean = clean_words(words)
print(f"Очищенные: {clean}")
counts = count_words(clean)
print(f"Частоты: {counts}")