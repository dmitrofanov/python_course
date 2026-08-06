text = "Анна и Иван гуляли в парке. Они увидели Ольгу и Артура."

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

words = text.split()
vowel_words = []

for word in words:
    # Убираем знаки препинания для проверки
    clean_word = word.strip(".,!?;:()\"'")
    if clean_word and clean_word[0] in vowels:
        vowel_words.append(clean_word)

print(f"Слова на гласную: {vowel_words}")