from random import randint,choice
from decouple import config
my_money=config('MY_MONEY', cast=int)
def win(users_slot, bet_money):
    global my_money
    numbers=list(range(1,31))
    win_slot=randint(1, len(numbers)-1)
    print(f'Выиграшный слот под номером {win_slot}')
    if win_slot==users_slot:
        my_money=my_money+bet_money*2
        print(f"YOU WON!YOUR BALANCE IS {my_money}")
    else:
        my_money=my_money-bet_money
    print(f"YOU LOST. YOUR BALANCE IS {my_money}")