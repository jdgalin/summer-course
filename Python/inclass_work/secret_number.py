import random

secret_number=random.randint(1,100)
count=1
while True:
    try: player_number=int(input('enter a number between 1 and 100: '))
    except ValueError: print('entered number is not an integer')
    else: break
while player_number != secret_number:
    if player_number > secret_number: 
        while True:
            try: player_number=int(input('number is too high, try again: '))
            except ValueError: print('entered number is not an integer')
            else: break
    elif player_number < secret_number: 
        while True:
            try: player_number=int(input('number is too low, try again: '))
            except ValueError: print('entered number is not an integer')
            else: break
    count+=1
print(f'Congratulations! it took you {count} guesses')
