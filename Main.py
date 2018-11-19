# Project-2

import random
number = random.randint(1000, 9999)
m_number = [number//1000, number%1000 - number%100, number%100 - number%10, number%10]
def search():
    true = "-"
    try:
        player = int(input())
    except ValueError:
        player = 0
    if 1 <= (player//1000) <= 9:
        m_player = [player//1000, player%1000 - player%100, player%100 - player%10, player%10]
        for step in range(4):
            if m_player[step] == m_number[step]:
                true = true + str(step+1)
        if player == number:
            print("Браво! Загаданное число:", player)
        else:
            print(true)
            search()
    else:
        print("Введите четырёхзначное число!")
        search()
print("Введите четырёхзначное число:")
search()
