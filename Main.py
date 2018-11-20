import Local
import random

number = random.randint(1000, 9999)
m_number = [number//1000, number%1000 - number%100, number%100 - number%10, number%10]

def level():
    print(Local.RU_CHOOSE_A_DIFFICULTY_LEVEL)
    print(Local.RU_EASY)
    print(Local.RU_MEDIUM)
    print(Local.RU_HARD)
    try:
        level = int(input())
    except ValueError:
        print(Local.RU_ANGRY_ANSWER)
        return 2
    if 1 <= level <= 3:
        return 11 - level**2
    else:
        print(Local.RU_ANGRY_ANSWER)
        return 2
def search(limit):
    true = Local.RU_DASH
    try:
        player = int(input())
    except ValueError:
        player = 0
    if 1 <= (player//1000) <= 9:
        m_player = [player//1000, player%1000 - player%100, player%100 - player%10, player%10]
        for step in range(4):
            if m_player[step] == m_number[step]:
                true = true[:-1] + str(step+1) + "."
        if player == number:
            print(Local.RU_CONGRATULATIONS, player)
        else:
            print(true)
            if limit != 0:
                limit -= 1
                search(limit)
            else:
                print(Local.RU_MOCKERY)
    else:
        print(Local.RU_ANGRY_INPUT_A_FOUR_DIGIT_NUMBER)
        search(limit)

limit = level()
print(Local.RU_INPUT_A_FOUR_DIGIT_NUMBER)
search(limit)
