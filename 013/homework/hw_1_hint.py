class NumberMaster:
    def sum_digits(self, n):
        """Возвращает сумму цифр числа"""
        total = 0
        # Превращаем число в строку, чтобы перебирать цифры
        for digit_char in str(n):
            # Превращаем символ обратно в число и добавляем к сумме
            total += int(digit_char)
        return total
    
    def reduce_to_single(self, n):
        """Повторяет суммирование цифр, пока не получится однозначное число"""
        current = n
        # Пока число не станет однозначным (меньше 10)
        while current >= 10:
            current = self.sum_digits(current)
        return current


# Пример использования
nm = NumberMaster()
print(nm.sum_digits(123))  # 6
print(nm.reduce_to_single(999))  # 9
print(nm.reduce_to_single(185))  # 5
