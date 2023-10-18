# Создаем переменные с числовыми списками от 0 до 9
list1 = list(range(10))
list2 = list(range(0, 10, 2))
res = []  # Создаем начальную переменную res с пустым списком

# Определяем функцию intersection(arg1, arg2)
def intersection(arg1, arg2):
    res = []  # Локальная пустая переменная res
    for item in arg1:
        if item in arg2:
            res.append(item)
    return res

# Вызываем функцию и выводим начальное значение res
result = intersection(list1, list2)
print("Результат вызова функции:", result)
