# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти :  '))
if num == 1:
    print('Возможные коориднаты: X (1, +бесконечность) Y (1, +бесконечность')
elif num == 2:
    print('Возможные коориднаты: X (-1, -бесконечность) Y (1, +бесконечность)')
elif num == 3:
    print('Возможные коориднаты: X (-1, -бесконечность) Y (-1, -бесконечность)')
elif num == 4:
    print('Возможные коориднаты: X (1, +бесконечность) Y (-1, -бесконечность)')
else:
    print('Это не номер четверти')
