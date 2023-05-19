
#ДЗ на понедельник (Ivanov_Lesson_16.py) - скидывает на гитхаб
# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать,
# требуется только изменение переданного списка, например:
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]


def modify_list(lst):
    return [i // 2 for i in lst if not i % 2]

print(modify_list([1, 2, 3, 4, 5, 6]))
print(modify_list([10, 5, 8, 3]))



