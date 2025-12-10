## Вычислить сколько секунд прошло с момента вашего рождения
from datetime import datetime
birthday = datetime(1991, 10, 5)
now = datetime.now()
# вычесть birthday из now и вывести результат вызова функции total_seconds из разницы
print((now - birthday).total_seconds())