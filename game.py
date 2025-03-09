import random
from pyscript import Element
c1, c2, c3, c4 = 1, 1, 1, 1

def game_lvl_1(n):
    global c1 
    random_num = random.randint(0, 3)
    if n == random_num:
        print(f'Yes, you guessed the correct number... it’s {random_num}')
        print(f'You guessed it in {c1} attempts')
    else:
        print(f'You guessed incorrectly... it was {random_num}')
        c1 += 1
        new = int(input('Guess again... Enter the Number: '))
        game_lvl_1(new)

def game_lvl_2(n1):
    global c2
    random_num1 = random.randint(0, 5)
    if n1 == random_num1:
        print(f'Yes, you guessed the correct number... it’s {random_num1}')
        print(f'You guessed it in {c2} attempts')
    else:
        print(f'You guessed incorrectly... it was {random_num1}')
        c2 += 1
        new1 = int(input('Guess again... Enter the Number: '))
        game_lvl_2(new1)

def game_lvl_3(n2):
    global c3
    random_num2 = random.randint(0, 10)
    if n2 == random_num2:
        print(f'Yes, you guessed the correct number... it’s {random_num2}')
        print(f'You guessed it in {c3} attempts')
    else:
        print(f'You guessed incorrectly... it was {random_num2}')
        c3 += 1
        new2 = int(input('Guess again... Enter the Number: '))
        game_lvl_3(new2)

def game_lvl_4(n3):
    global c4
    random_num3 = random.randint(0, 100)
    if n3 == random_num3:
        print(f'Yes, you guessed the correct number... it’s {random_num3}')
        print(f'You guessed it in {c4} attempts')
    else:
        print(f'You guessed incorrectly... it was {random_num3}')
        c4 += 1
        new3 = int(input('Guess again... Enter the Number: '))
        game_lvl_4(new3)
