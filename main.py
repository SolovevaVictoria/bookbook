'''Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе
стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение
Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
**Вывод:** Парам пам-пам

Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция,
у которой ровно два аргумента, как, например, у операции умножения.
'''
def rithm(st):
    res = []
    for i in st.split():
        res.append(sum(list(map(lambda x: 1 if x in 'уеаоэяию' else 0, i))))
    return len(set(res)) == 1

def print_operation_table(operation, num_rows=6, num_columns=6):
    res = []
    for i in range(1, num_rows + 1):
        print(*list(operation(i, j) for j in range(1, num_columns + 1)))



print('ЗАДАЧА 34:')
test = 'пара-ра-рам рам-пам-папам па-ра-па-да'
#test1 = 'парарам ра-пам'
#test2 = 'па-па-ра-па-па'
#test3 = ''
print('Парам пам-пам' if rithm(test) else 'Пам парам')

print('\nЗАДАЧА 36:')
print_operation_table(lambda x, y: x * y)





