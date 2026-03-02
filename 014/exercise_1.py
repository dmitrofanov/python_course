'''
Задание: Счастливый билет (Поиск закономерностей)

Цель: Развить навык сравнения частей данных и обработки строк.

Задание:
В некоторых культурах есть поверье: билет счастливый, если сумма первых трех цифр его номера равна сумме последних трех цифр.

    Напиши класс TicketChecker.

    Метод is_lucky(ticket_number), который принимает строку из 6 цифр (например, "123420") и возвращает True, если билет счастливый, и False, если нет.

    Усложнение: Метод find_lucky_in_range(start, end) принимает два целых шестизначных числа и возвращает список всех счастливых билетов в этом диапазоне.
'''

'Пример работы:'



class TicketChecker:
    def is_lucky(self,ticket_number):
        # print(int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]))
        # sum1 = 0
        # for i in 0,1,2:
        #     sum1 += int(ticket_number[i])
        
        # sum2 = 0
        # for i in 3,4,5:
        #     sum2 += int(ticket_number[i])
        
        # return sum1 == sum2
        # или
        return int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]) == int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

    def find_lucky_in_range(self, start, end):
        # tickets = []
        # for ticket_number in range(start,end):
        #     if self.is_lucky(str(ticket_number)):
        #         tickets.append(ticket_number)
        # return tickets
        return [ticket_number for ticket_number in range(start , end +1) if self.is_lucky(str(ticket_number))]

checker = TicketChecker()
print(checker.is_lucky("123420"))  # 1+2+3 = 6, 4+2+0 = 6 -> True
print(checker.is_lucky("111111"))  # 3 == 3 -> True
print(checker.is_lucky("123456"))  # 6 vs 15 -> False

print(checker.find_lucky_in_range(0,100000))