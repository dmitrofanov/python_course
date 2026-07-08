text = "привет мир"

# Преобразуем в список символов
chars = list(text)
chars.reverse()
reverse_text = ''.join(chars)
reversed_text = ''.join(reversed(text))

print(f"Исходная: {text}")
print(f"Перевёрнутая reverse: {reverse_text}")
print(f"Перевёрнутая reversed: {reversed_text}")