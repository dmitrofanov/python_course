# 1) Создай словарь c оценками для двух учеников (Анна, Игорь) с помощью функции dict и с помощью литерала. Ключом должно являться Имя ученика (строка), а значением оценка (число).

students_grades_l = {"Anna": 5, "Igor": 4}
students_grades_d = dict(Anna = 5, Igor = 4)
print(students_grades_l)
print(students_grades_d)

# 2) Возьми словарь из задания 1 и выведи оценку для Анны.

students_grades_l = {"Anna": 5, "Igor": 4}
students_grades_d = dict(Anna = 5, Igor = 4)
print(f"Оценка Анны:{students_grades_l["Anna"]}")
print(students_grades_d["Anna"])

# 3) Возьми словарь из задания 1 и добавь туда запись для Петра.

students_grades_l = {"Anna": 5, "Igor": 4}
students_grades_l["Petr"] = 3
print(students_grades_l)

# 4) Возьми словарь из задания 1 и удали оттуда запись для Игоря.

students_grades_l = {"Anna": 5, "Igor": 4}
del students_grades_l["Igor"]
print(students_grades_l)

# 5) Даны следующие переменные
ip_addr = '192.168.20.43'
hostname = 'application-server-001'
# создай словарь с помощью функции dict и с помощью синтаксиса литерала, в котором значения будут взяты из этих переменных. Имена для ключей выбери сам (можно взять такие же как имена переменных).

server_l = {"ip_addr": ip_addr,"hostname": hostname}
server_d = dict(ip_addr = ip_addr,hostname = hostname)
print(server_l)
print(server_d)