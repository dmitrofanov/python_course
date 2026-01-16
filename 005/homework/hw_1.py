"""
Напиши функцию divide_safe(), которая делит два числа.
1. Сделай параметры a и b ИМЕНОВАННЫМИ (чтобы было понятно, что на что делим)
2. Добавь необязательный параметр default (по умолчанию None)
3. Функция должна ВОЗВРАЩАТЬ результат, а не печатать его
4. Используй try-except, чтобы обработать:
   - Деление на ноль (ZeroDivisionError) → вернуть default
   - Если a или b не числа (TypeError) → вернуть default
   - Любые другие ошибки → тоже вернуть default

Примеры работы:
print(divide_safe(a=10, b=2))     # Должно вернуть 5.0
print(divide_safe(b=2, a=10))     # Должно вернуть 5.0 (порядок не важен!)
print(divide_safe(a=10, b=0))     # Должно вернуть None
print(divide_safe(a=10, b=0, default=0))  # Должно вернуть 0
print(divide_safe(a="десять", b=2))  # Должно вернуть None
"""

# Подсказка: структура функции
def divide_safe(a, b, default=None):
    try:
        # попытаться вернуть a / b
    except ZeroDivisionError:
        # вернуть default
    except TypeError:
        # вернуть default
    except Exception:
        # вернуть default (на всякий случай)