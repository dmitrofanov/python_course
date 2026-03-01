class TicketChecker:
    def is_lucky(self, ticket_number):
        """
        Проверяет, является ли билет счастливым
        ticket_number - строка из 6 цифр
        """
        # Проверяем, что длина строки равна 6
        if len(ticket_number) != 6:
            return False
        
        # Сумма первых трех цифр
        first_sum = 0
        for i in range(3):
            first_sum += int(ticket_number[i])
        
        # Сумма последних трех цифр
        second_sum = 0
        for i in range(3, 6):
            second_sum += int(ticket_number[i])
        
        # Сравниваем суммы
        return first_sum == second_sum
    
    def find_lucky_in_range(self, start, end):
        """Находит все счастливые билеты в диапазоне чисел"""
        lucky_tickets = []
        
        # Перебираем все числа в диапазоне
        for num in range(start, end + 1):
            # Превращаем число в строку из 6 цифр (добавляем нули слева)
            ticket_str = str(num).zfill(6)
            
            # Проверяем, счастливый ли билет
            if self.is_lucky(ticket_str):
                lucky_tickets.append(ticket_str)
        
        return lucky_tickets


# Пример использования
checker = TicketChecker()
print(checker.is_lucky("123420"))  # True
print(checker.is_lucky("111111"))  # True
print(checker.is_lucky("123456"))  # False

# Найдем счастливые билеты от 000000 до 000050
print(checker.find_lucky_in_range(0, 50))
# Например: ['000000', '001001', '001010', ...]