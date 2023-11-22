# Перетин масивів
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

intersection = [x for x in array1 if x in array2]
print(f"Перетин масивів:{intersection}")




# чи є заданий рядок числом
string1 = "123"

is_number = lambda s: s.isdigit()

print(f'"{string1}" є числом: {is_number(string1)}')


# Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда.
new_list = [
    ["apple", "banana"],
    ["kiwi", "orange", "pear", "grape"],
    ["lemon", "tomato", "orange", "mayo", "kiwi", "melon", "watermelon"]]


max_list = max(new_list, key=lambda x: len(x))
min_list = min(new_list, key=lambda x: len(x))


print(f"Список з максимальною довжиною:{max_list}, з мінімальною довжиною:{min_list}")
