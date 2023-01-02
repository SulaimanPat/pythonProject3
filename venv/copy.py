from random import randint
from decouple import config
import win
my_money=config('MY_MONEY', cast=int)
print("Добро пожаловать в наше казино.\nВ нашей игре нужно угадать выигравший слот от 1 до 30")
print(f"Ваш баланс: {my_money}")
while my_money!=0:
    try:
        users_slot=int(input("Введите выиграшный слот: "))
        if users_slot>31 or users_slot<=0:
            raise ValueError
    except ValueError:
        print("Введите число от 1 до 30")
        continue
    try:
        bet_money=int(input("Введите сумму вашей ставки: "))
        if bet_money>my_money:
            raise ValueError
    except ValueError:
        print(f"Введите сумму не больше {my_money}")
        continue
    win.win(users_slot, bet_money)
    stop=input("Вы хотите продолжить игру? Да/Нет: ").capitalize()
    if stop == "Да":
        continue
    elif stop==" Нет":
        print('Игра завершена')
        break
    else:
        print("Введите Да или Нет")
        continue


