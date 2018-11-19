import random

number = random.randint(1000, 9999)
m_number = [number//1000, number%1000 - number%100, number%100 - number%10, number%10]

def level():
    print("Выберите уровень сложности:")
    print("1. Лёгкий")
    print("2. Средний")
    print("3. Сложный")
    try:
        level = int(input())
    except ValueError:
        print("БУДЕШЬ ИГРАТЬ НА СЛОЖНОМ!")
        return 2
    if 1 <= level <= 3:
        return 11 - level**2
    else:
        print("БУДЕШЬ ИГРАТЬ НА СЛОЖНОМ!")
        return 2
def search(limit):
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
            print("Молодчина! Загаданное мной число действительно:", player)
        else:
            print(true)
            if limit != 0:
                limit -= 1
                search(limit)
            else:
                print("Ай да молодец! Снова не угадал!")
    else:
        print("Введите четырёхзначное число >.<")
        search(limit)

limit = level()
print("Введите четырёхзначное число:")
search(limit)
