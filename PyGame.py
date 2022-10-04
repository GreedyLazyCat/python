import os
import random

n = random.randint(4, 30)

print('Игра в камни')

while True:
    print('Текущее кол-во камней:', n)
    print('Ход компьютера:', end=' ')
    move = random.randint(1, 2)
    if n == 3:
        move = random.randint(1, 2)
    elif n == 2:
        move = 1
    n -= move
    print('Компьютер взял', move, 'камней')
    if n <= 1:
        print ('Вы проиграли')
        break

    print('Текущее кол-во камней:', n)
    print('Ваш ход')
    move = int(input())
    while not (1 <= move <= 3):
        print("Введите кол-во камней от 1 до 3")
        move = int(input())
    n -= move
    if n <= 1:
        print('Вы победили')
        break