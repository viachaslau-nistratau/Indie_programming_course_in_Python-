"""
На вход программе поступает целое число n. Вам необходимо создать словарь,
который будет включать в себя ключи от 1 до n,
а значениями соответствующего ключа будет значение ключа в квадрате.
В качестве ответа выведите полученный словарь
"""
n = int(input())
a = {a: a**2 for a in range(1, n+1)}
print(a)

"""
Напишите программу, которая печатает словарь alphabet, 
где ключи  - строчные английские символы, 
а значения - порядковые номера букв в алфавите.
Начало вашего словаря должны быть таким {"a": 1, "b": 2 }
В качестве ответа распечатайте ключи и значения данного словаря по алфавиту, 
каждую пару на новой строчке.
Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:
"""
from string import ascii_lowercase
a = str(ascii_lowercase)
alphabet = {}
count = 0
for i in a[::1]:
    count += 1
    alphabet.setdefault(i,count)
    alphabet.items()
for i in alphabet.items():
    print(*i)

"""
Есть два словаря, нужно их объединить в новый словарь rez и вывести его на экран
"""
rez = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
rez.update(d2)
print(rez)

"""
Представьте, у нас есть список товаров и их стоимость, 
но мы хотим взглянуть на него в отсортированном виде. 
Вверху хотим видеть самые дорогие товары, внизу самые дешевые
Программа будет принимать строки, в которых сперва указывается название товара, 
а затем через двоеточие с пробелом его цена - целое положительное число.
Строка "конец" означает списка товаров и соответственно окончание ввода
Все товары имеют уникальные названия, цены не дублируются.
Ваша задача вывести список товаров по уменьшению цены
Sample Input:
Sony PlayStation 5: 46000
Телевизор QLED Samsung QE65Q60TAU: 87090
Смартфон Samsung Galaxy A11: 10000
Планшет Samsung Galaxy Tab S6: 26600
конец
"""
spis = {}
while True:
    x = list(input().split(':'))
    if x[0] == 'конец':
        break
    else:
        k, v = x[0], int(x[1])
    spis[k] = v
for i in sorted(spis.items(), key=lambda para: para[1], reverse=True):
        print(i[0])

"""
Рейтинг таксистов
Руководитель таксопарка хочет увидеть отчет по всем таксистам, 
где нужно указать имя таксиста и его среднюю оценку. 
Информацию в отчете нужно расположить по убыванию средней оценки таксиста.
После каждого успешно выполненного заказа, клиент выставляет таксисту 
оценку - целое число от 1 до 5.
Входные данные
Программа будет принимать строки, в которых сперва указывается имя таксиста, 
а затем через запятую с пробелом его оценка за заказ.
Строка "конец" является последней строкой и означает окончание ввода
Выходные данные
Нужно расположить таксистов в порядке убывания их средней оценке и 
вывести имя каждого таксиста и его среднюю оценку в отдельной строке. 
В случае совпадения средних оценок расположить таксистов нужно 
отсортировать имена таксистов по алфавиту 
"""
dict = {}
dict_2 = {}
while True:
    a = list(input().split(', '))
    if a[0] == 'конец':
        break
    if a[0] in dict:
        dict[a[0]] += [int(a[1])]
    else:
        dict[a[0]] = [int(a[1])]
for items in dict:
    result = sum(dict[items]) / len(dict[items])
    dict_2[items] = result
for i in sorted(dict_2.items(), key=lambda para: (-para[1], para[0])):
    print(*i)

"""
Премия Оскар
Представьте, что мы с вами сами можем решать кому и сколько 
статуэток Оскара уйдет (Лео бы тогда давно купался в этих статуэтках)
Ваша задача написать программу, которая находит информацию, 
кто из актеров получил наибольшее и наименьшее количество статуэток
Входные данные
Программа принимать на вход в первой строке натуральное 
число n - количество вручаемых сегодня наград. И затем в n следующих 
троках вводятся имена актеров - победителей.
Выходные данные
Нужно вывести в  отдельных строках имена актеров набравших наибольшее 
и наименьшее количество статуэток и через запятую их количество. 
Гарантируется, что всегда будет только один человек, 
набравших наибольшее и наименьшее количество статуэток.
"""
n = int(input())
d = {}
for i in range(n):
    m = input()
    kk = m.split(", ")
    if kk[0] in d:
        d[kk[0]]+=1
    else:
        d[kk[0]] = 1
z = sorted((d.items()), key=lambda para: para[1], reverse=True )
print(z[0][0], z[0][1], sep=", ")
print(z[-1][0], z[-1][1], sep=", ")

"""
Телефонная книга
Петя очень популярный парень, у него много друзей и он хочет сохранить 
их контакты в телефонной книге. Известно, что у каждого друга 
может быть один или больше номеров телефонов. Напишите программу, 
которая поможет Пете находить все номера определённого друга.
Формат ввода
В первой строке задано одно целое число N (1 ≤ N ≤ 1000) — количество 
номеров телефонов, информацию о которых Петя  решил сохранить в 
телефонной книге. В следующих N строках заданы телефоны и имена их 
владельцев через пробел. Телефон — это несколько цифр, записанных подряд, 
имя же состоит только из русских букв. Записи не повторяются.
В следующей строке записано целое число M (1 ≤ M ≤ 100) — количество 
запросов от Пети. В следующих M строках записаны сами запросы, 
по одному на строке. Каждый запрос — это имя какого-то друга, 
чьи телефоны Петя хочет сейчас найти, записанное в точности так, как в телефонной книге.
Формат вывода
Для каждого запроса от Пети выведите в отдельной строке все телефоны, 
принадлежащие человеку с этим именем. Телефоны одного человека выводите 
в одну строку через пробел в том порядке, в котором они были заданы во входных данных.
Если в телефонной книге нет телефонов человека с таким именем, 
выведите в соответствующей строке «Неизвестный номер» (без кавычек).
"""
n = int(input())
dict = {}
for i in range(n):
    m = input().split()
    m[0], m[1] = m[1], m[0]
    if m[0] not in dict:
        dict[m[0]] = str(m[1])
    else:
        dict[m[0]] += ' ' + str(m[1])
k = int(input())
spis = []
for j in range(k):
    nm = str(input())
    spis.append(nm)
for x in spis:
    if x not in dict:
        print('Неизвестный номер')
    else:
        print(dict[x])

"""
задача научиться использовать словарь для подсчета количества. 
Вашей программе поступает на вход строка, вам необходимо подсчитать 
сколько раз встретилась каждая буква в этой строке без учета регистра, 
при этом цифры и символы пунктуации нужно пропустить. 
Ответ нужно сохранить в словаре, в котором ключ - буква, 
а значение - количество раз, сколько эта буква встретилась в строке. 
В качестве ответа нужно вывести словарь
"""
a = input().lower()
b = {}
for item in a:
    if item.isalpha():
        if item in b:
            b[item[0]] += 1
        else:
            b[item[0]] = 1
print(b)

