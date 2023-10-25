import datetime as dt
import random


"""
task 1
 Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів. 
 Приймає на вхід будь-яку дату та час (datetime), а також значення днів(int), 
 і знак(True або False, які репрезентують + і -). 
 Повертає datetime. В цій задачі скористайтесь datetime.timedelta
 """


def add_days(date: dt.datetime, day_values: int, add=True) -> dt.datetime:
    if add:
        result = date + dt.timedelta(day_values)
    else:
        result = date - dt.timedelta(day_values)

    return result


date = dt.datetime(2023, 10, 21, 15, 25, 25)
day_values = 3
add = True

new_value = add_days(date, day_values, add)
print(new_value)

"""
Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні), 
вираховуючі різницю між наданим значеням і значенням datetime.now().
Приймає дату та час(datetime), повертає два значення: datetime і datetime.timestamp. 
В цій задачі скористайтесь для конвертації datetime.timestamp. Виведіть результат в консоль
"""


def age_in_seconds(date_of_birth: dt.datetime):
    value = dt.datetime.now() - date_of_birth
    seconds = value.total_seconds()
    return value, seconds


date_of_birth = dt.datetime(1990, 10, 15)
value, age_seconds = age_in_seconds(date_of_birth)

print("Вік:", value)
print("Вік в секундах:", age_seconds)


"""
Створіть за допомогою list comprehension список, в якому буде 100 елементів, 
і кожен із яких буде в границях від 1 до 10(для цього можна скористатись функцією randint із модуля random). 
Порахуйте кількість кожного елемента і виведіть в консоль
"""

list_of_value = [random.randint(1, 10) for _ in range(100)]
result = {}
for num in list_of_value:
    result[num] = result.get(num, 0) + 1
print(result)


