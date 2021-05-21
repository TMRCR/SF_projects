import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v3(number):
    count = 0 #счетчик попыток
    a = 1 #минимальное возможное число
    b = 100 #максимальное возможное число
    while True: #запускаем цикл
        count += 1 #плюсуем попытку
        predict = (a + b) // 2 #предполагаем число, находящееся в середине списка возможных
        if number == predict:
            return count #мы угадали!!! завершаем цикл, возвращаем попытки
        elif number > predict:
            a = predict + 1 #отсеиваем все, что меньше загаданного числа
        else:
            b = predict - 1 #отсеиваем все, что больше загаданного числа


# запускаем
score_game(game_core_v3)
#Данная программа отгадывает число в среднем, с пятой попытки
