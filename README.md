# python-courses-25
Homeworks for the course "Python".


**HW 3. Functions**

Темы: функции, декораторы, работа с файлами.

Задача 1.
Напишите функцию, которая принимает список и делает его “плоским”.
Используйте рекурсию. Функция должна модифицировать переданный список,
а не создавать новый.
Пример:
-- list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
-- flatten_list(list_a)
-- print(list_a)
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Задача 2.
Напишите функцию, которая производит слияние двух словарей. Используйте
рекурсию. В обоих словарях может быть любой уровень вложенности. Вложены
могут быть другие коллекции: словари, списки, множества, кортежи.
Пример:
-- dict_a = {“a”: 1, “b”: {“c”: 1, “f”: 4}}
-- dict_b = {“d”: 1, “b”: {“c”: 2, “e”: 3}}
-- merge_dicts(dict_a, dict_b)
-- print(dict_a)
{“a”: 1, “b”: {“c”: 2, “e”: 3, “f”: 4}, “d”: 1}

Задача 3.
Напишите декоратор log_calls, который записывает в файл время вызова, имя и
аргументы вызванной функции. Один вызов функции - одна строка в файле.
Декоратор должен принимать имя файла для записи в качестве параметра.

Задача 4.
Пользователь вводит матрицу (список списков). Напишите функцию, которая
транспонирует матрицу, не изменяя входную матрицу. Транспонирование
матрицы - операция над матрицей, когда ее строки становятся столбцами с
теми же номерами.

Задача 5.
Напишите декоратор cache, который кэширует результат вызова функции
(сохраняет в словаре). Когда функция вызывается снова с теми же
аргументами, декоратор должен возвращать результат из кэша, вместо того,
чтобы вызывать декорированную функцию.

Задача 6.
Напишите функцию unique_elements, которая принимает вложенный список и
возвращает уникальные элементы.
Пример:
-- list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
-- unique_elements(list_a)
[1, 2, 3, 4, 5, 6, 7, 10, 8, 9]

Задача 7.
Реализуйте функцию merge_sorted_list, которая принимает два
отсортированных списка, и возвращает новый отсортированный список,
содержащий элементы из обоих списков.

Задача 8*.
Реализуйте функцию merge_sort, которая получает несортированный список, и
сортирует его с помощью алгоритма “сортировка слиянием”.

Дополнительные условия и требования к решениям:
1. Запрещается использовать встроенные функции, которые решают
задачу. Например, если задача “отсортировать список”, то запрещается
использовать функции sort или sorted.
2. Везде, где есть ввод пользователя, предполагаем, что будут вводится
корректные данные.
3. Форматирование строк приветствуется.
4. Вывод результатов и промежуточной информации на экран должен
содержать пояснения, что именно выведено (если необходимо).
5. Каждая задача должна быть помещена в отдельный файл с названием
task_1.py, task_2.py в директории hw3 и т.д.



**HOMEWORK 2. Built-in Types**

Темы: базовые типы (tuple, list, set, dict), циклы (for, while).

Задача 1. Посчитать слова
Во входной строке записан текст (вводится пользователем). Словом считается
последовательность символов (кроме пробела), идущих подряд. Слова
разделены одним или большим числом пробелов или символами конца строки.
Посчитайте:
1. Сколько раз каждое слово встречается в тексте и стройте словарь
{слово: количество}.
2. Количество уникальных слов.
Слова Apple и apple считаются одинаковыми.


Задача 2. Анализ списка чисел
Пользователь вводит список чисел. Числа вводятся через пробел, могут быть
как целые, так и с плавающей точкой. Выведите на экран:
1. Уникальные числа.
2. Повторяющиеся числа.
3. Четные и нечетные чисел.
4. Отрицательные чисел.
5. Числа с плавающей точкой.
6. Сумму всех чисел, кратных 5.
7. Самое большое число.
8. Самое маленькое число.

Задача 3. Второе по величине число
Пользователь вводит список чисел. Найдите второе по величине число.

Задача 4. Сравнение списков чисел
Пользователь вводит 2 набора чисел. Выведите на экран:
1. Числа, которые присутствуют в обоих наборах одновременно.
2. Числа из первого набора, которые отсутствуют во втором, и наоборот.
3. Числа из обоих наборов, за исключением чисел, найденных в пункте 1.

Задача 5. Анаграммы
Пользователь вводит 2 слова. Напишите программу, которая проверяет,
являются ли они анаграммами (первое слово может быть сформировано путем
перестановки букв во втором слове).
Пример:
- “listen”
- “silent”
True

Задача 6. Удаление дубликатов без set()
Пользователь вводит список (любой). Удалите все дубликаты без использования set().

Задача 7. Сжатие строки
Пользователь вводит строку. Напишите программу, которая сжимает строку
следующим образом: если символ X повторяется N раз, то итоговая строка
должна содержать XN.
Пример:
- “aaaabbbccaff”
a4b3c2a1f2

Задача 8. Угадай число
Программа случайно загадывает число от 1 до 100.
- Пользователь вводит догадки.
- Программа подсказывает "Больше" или "Меньше".
- Игра продолжается, пока пользователь не угадает.

*Задача 9. Шифр Цезаря
Пользователь вводит строку и число N (может быть как положительным, так и
отрицательным). Напишите программу, которая шифрует строку с помощью
шифра Цезаря.
Шифр Цезаря - это подстановочный шифр, где каждая буква в исходном тексте
сдвигается вверх или вниз по алфавиту на N позиций.
Пример:
Enter N:
- 3
Enter text:
- hello
Result: khoor
Пояснение:
В слове hello каждая буква сдвигается по алфавиту на 3 позиции. Таким
образом h становится k (алфавит a b c d e f g h i j k l m n o p q r s t u v w x y z), e
становится h, l становится o, o становится r.

*Задача 10. Самая длинная подстрока
Найдите самую длинную подстроку без дубликатов ("abcabcbb" → "abc").


Пояснения
1. Каждая задача должна быть помещена в отдельный файл с названием
task_1.py, task_2.py, и т.д.
2. Для ввода используйте input(), для вывода - print().
3. Вывод результатов и промежуточной информации на экран должен
содержать пояснения, чтобы было понятно, что именно выводится на
экран.



**HOMEWORK 1**

Задача 1. Форматирование ФИО
Введите фамилию, имя и отчество. Приведите их к формату Фамилия И.О.
(первая буква имени и отчества с точкой).

Задача 2. Удаление гласных
Введите строку и удалите из нее все гласные (a, e, i, o, u), затем выведите
результат.

Задача 3. Упрощенный шифр Цезаря
Введите маленькую латинскую букву (a–z) и число n. Выведите букву,
сдвинутую в алфавите на n позиций (с учетом зацикливания, т.е. буква z при
n=1 становится a, при n=2 - b, и т.д.)

Задача 4. Проверка пароля
Введите пароль, проверьте, и выведите на экран:
- Если меньше 16 символов → "Слишком короткий"
- Если содержит только буквы или только цифры → "Слабый пароль"
- Иначе → "Надёжный пароль".

Задача 5. Размен денег
Введите сумму в рублях (целое число). Определите, сколько купюр по 100, 50,
10, 5 и 1 рублю потребуется для ее размена.

Задача 6. Магическое число
Введите число и вычислите сумму его цифр. Если число делится на 7 без
остатка, выведите "Магическое число!", иначе просто сумму цифр.

Задача 7. Формат времени
Введите количество секунд и переведите их в минуты и секунды, например, 75
→ 1 минута 15 секунд.

Задача 8. Палиндром
Введите строку и определите, является ли она палиндромом (читается
одинаково слева направо и справа налево).

Задача 9. Сравнение дробных чисел
Введите два числа с плавающей точкой. Выведите True, если их разница по
модулю меньше 0.001, иначе False.

Задача 10. Определение времени по углу
Введите угол (0–360), на который повернута минутная стрелка часов.
Определите, сколько сейчас минут.

Задача 11. Проверка IP адреса
Введите строку. Проверьте, является ли она корректным IP-адресом (формат
должен быть XXX.XXX.XXX.XXX, где XXX - число от 0 до 255).

*Задача 12. Система счисления
Введите число в десятичной системе. Преобразуйте его в двоичную, а затем
снова в десятичную, без использования встроенных функций bin() и int().

*Задача 13. Римские числа
Введите число (1-100). Преобразуйте его в римскую систему (58 → LVIII).

*Задача 14. Римская арифметика
Введите два числа в римской системе (XIV, XXVIII). Вычислите их сумму и
разность, вернув римский результат.

Пояснения
1. Каждая задача должна быть помещена в отдельный файл с названием
task_1.py, task_2.py, и т.д.
2. Для ввода используйте input(), для вывода - print().
3. Вывод результатов и промежуточной информации на экран должен
содержать пояснения, чтобы было понятно, что именно выводится на
экран.