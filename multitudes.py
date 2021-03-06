"""
Даны два списка чисел.
Выведите все числа, которые входят как в первый,
так и во второй список в порядке возрастания.
"""
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a.intersection(b)
c = list(c)
c = sorted(c)
print(*c)

"""
Даны два списка чисел. Выведите все числа в порядке возрастания, 
которые входят в первый список, но при этом отсутствуют во втором. 
"""
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a.difference(b)
c = list(c)
c = sorted(c)
print(*c)

"""
Напишите программу, которая выводит все цифры, встречающиеся в символьной 
строке больше одного раза.
Входные данные
Входная строка может содержать содержит цифры, пробелы и латинские буквы.
Выходные данные
Программа должна вывести в одну строчку в порядке возрастания все цифры, 
встречающиеся во входной строке больше одного раза. 
Если таких цифр нет, нужно вывести слово 'NO'.
"""
a = input()
b = set()
for i in a:
    if i.isdigit():
        if a.count(i) > 1:
            b.add(i)
b = sorted(b)
if len(b) != 0:
    for i in b:
        print(i, end=' ')
else:
    print('NO')

"""
Напишите программу, которая удаляет из строки все повторяющиеся символы, 
при этом регистр букв необходимо учитывать.
Входные данные
Программа получает на вход строку, состоящую из заглавных и строчных символов, 
цифр и знаков препинания.
Выходные данные
Программа должна вывести исходную строку, из которой удалены все повторяющиеся символы.
"""
n = input()
a = []
for i in n:
    if i not in a:
        a.append(i)
print(''.join(a))

"""
Конь Валера собрался с друзьями на вечеринку. 
Он давно следит за тенденциями моды и поэтому знает, 
что сейчас очень популярно носить все подковы разного цвета. 
С прошлого года у Валеры остались четыре подковы, но, возможно, 
некоторые из них имеют одинаковый цвет. В этом случае, чтобы не ударить в грязь 
лицом перед своими стильными товарищами, ему нужно сходить в магазин и 
купить дополнительно несколько каких-нибудь подков.
К счастью в магазине продаются подковы всех возможных цветов, 
и у Валеры имеется достаточно денег, чтобы купить любые четыре. 
Однако в целях экономии он хотел бы потратить как можно меньше денег, 
поэтому вам нужно помочь Валере и определить, какое минимальное количество подков 
нужно купить, чтобы он смог надеть на вечеринку четыре подковы различного цвета.
Входные данные
В первой строке через пробел записаны четыре целых 
числа s1,s2,s3,s4 (1≤s1,s2,s3,s4≤109) — цвета подков, имеющихся у Валеры.
Считайте, что все возможные цвета пронумерованы целыми числами.
Выходные данные
Выведите единственное целое число — минимальное количество подков, которое нужно купить.
"""
n = list(map(int, input().split()))
a = set(n)
count = 4 - len(a)
print(count)

"""
Кажется, еще совсем недавно наступил новый 2013 год. 
А знали ли Вы забавный факт о том, что 2013 год является первым годом 
после далекого 1987 года, в котором все цифры различны?
Теперь же Вам предлагается решить следующую задачу: задан номер года, 
найдите наименьший номер года, который строго больше заданного и в 
котором все цифры различны.
Входные данные
В единственной строке задано целое число y 
(1000≤y≤9000) — номер года.
Выходные данные
Выведите единственное целое число — минимальный номер года, 
который строго больше y, в котором все цифры различны.
"""
n = int(input())
n += 1
while n > 0:
    d = dict.fromkeys(str(n))
    if len(d) == 4:
        print(''.join(d))
        break
    n += 1

"""
Входные данные
В первой и единственной строке задано описание множества букв. 
Длина строки не превышает 1000. Гарантируется, что строка начинается с 
открывающейся фигурной скобки, а заканчивается закрывающейся. 
Между ними через запятую перечислены маленькие латинские буквы. 
После каждой запятой следует пробел.
Выходные данные
Выведите единственное число — количество различных букв в множестве.
"""
n = input()[1:-1]
if len(n) == 0:
    print('0')
else:
    print(len(set(n.split(', '))))

"""
Слово или предложение на некотором языке называется панграммой, 
если в нем встречаются все символы алфавита этого языка хотя бы один раз. 
Панграммы часто используют в типографии для демонстрации шрифтов или 
тестирования средств вывода различных устройств.
Вам дана строка, состоящая из маленьких и больших латинских букв. 
Проверьте, является ли эта строка панграммой. Считается, 
что строка содержит букву латинского алфавита, если эта буква встречается 
в верхнем или нижнем регистре.
Входные данные
В первой строке записано одно целое 
число n (1≤n≤100) — количество символов в строке.
Во второй строке записана сама строка. Строка содержит исключительно 
строчные и заглавные латинские буквы.
Выходные данные
Выведите «YES», если строка является панграммой, и «NO» в противном случае.
"""
n = int(input())
a = input().lower()
stroka = set(a)
if len(stroka) == 26:
    print('YES')
else:
    print('NO')