from random import randint,choice
from decouple import config
my_money=config('MY_MONEY', cast=int)
def win(users_slot, bet_money):
    global my_money
    try:
        if users_slot > 31 or users_slot <= 0:
            raise ValueError
    except ValueError:
        print("Введите число от 1 до 30")
    try:
        if bet_money > my_money:
            raise ValueError
    except ValueError:
        print(f"Введите сумму не больше {my_money}")
    numbers=list(range(1,31))
    win_slot=randint(1, len(numbers)-1)
    print(f'Выиграшный слот под номером {win_slot}')
    if win_slot==users_slot:
        my_money=my_money+bet_money*2
        print(f"YOU WON!YOUR BALANCE IS {my_money}")
    else:
        my_money=my_money-bet_money
    print(f"YOU LOST. YOUR BALANCE IS {my_money}")
