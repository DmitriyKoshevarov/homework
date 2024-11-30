stone_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
index = 0

while index < len(stone_1):
    stone_1_value = stone_1[index]
    print('Значение в первом поле:',stone_1_value)
    result = []

    for i in range(1,21):
        for j in range(i+1,21):
            stones_2_summ = i + j
            if stone_1_value % stones_2_summ == 0:
                result.append(f'{i}{j}')
    index += 1
    password = ''.join(result)
    print('Пароль:', password)