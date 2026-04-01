text = "кот собака кот рыба кот птица собака рыба рыба рыба кот"
words = text.split()

# Подсчёт частоты слов
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Частота слов:")
for word, count in word_count.items():
    print(f"  {word}: {count}")

# Топ-3 самых частых
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(f"\nТоп-3 самых частых слова:")
for i, (word, count) in enumerate(sorted_words[:3], 1):
    print(f"  {i}. {word} ({count} раз)")

# Самое длинное слово
longest = max(words, key=len)
print(f"\nСамое длинное слово: '{longest}' ({len(longest)} букв)")

# Общая статистика
print(f"\nВсего слов: {len(words)}")
print(f"Уникальных слов: {len(word_count)}")