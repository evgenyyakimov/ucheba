import random

number = random.randint(1, 100)
#print(number)
print(
    '''
    Игра Угадай Число
    ------------------
    Неограниченное кол-во пользователей для игры.
    Число в диапозоне от 1 до 100
    Три уровня сложности: 1 уровень - 10 попыток,
    2 уровень - 5 попыток, 3 уровень - 3 попытки
    '''
)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности: '))
max_count = levels[level]

user_count = int(input('Введите кол-во пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}: ')
    users.append(user_name)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('')
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {users}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'Победитель {winner_name}')
print('')
print('')
print('')
input('Нажмите ENTER для закрытия')