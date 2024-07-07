first = int(input('Введите 1-ое число: '))
second = int(input('Введите 2-е число: '))
third = int(input('Введите 3-е число: '))
if first != second != third != first:
    print(0)
elif first == second != third or first != second == third or first == third != second:
    print(2)
else:
    print(3)
