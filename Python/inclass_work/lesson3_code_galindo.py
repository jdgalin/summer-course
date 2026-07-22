import random
# for number in range(1,101):
#     if number%3==0: 
#         print('Fizz', end='')
#         if number%5==0:print('Buzz',end='')
#     elif number%5==0: print('Buzz',end='')
#     else: print(number, end='')
#     print()

# while True:
#     print('\n\n\n')
#     choices=['rock', 'paper', 'scissors', 'gun']
#     while True:
#         try: user_choice=input('provide rock, paper, or scissors: ')
#         except: print('input not valid')
#         if user_choice in choices: break
#         else: print('please follow directions')

#     computer_choice = random.randint(0,2)
#     user_choice = choices.index(user_choice)
#     print(f'computer choose {choices[computer_choice]}')

#     user_victory='you win. good jorb'
#     if user_choice==computer_choice: print("it's a tie")
#     elif user_choice==3: print('you rotten cheater')
#     elif computer_choice==2 and user_choice==0: print(user_victory)
#     elif computer_choice>user_choice: print('computer wins! try again')
#     else: print(user_victory)


#     play_again= input('would you like to try again? (y/n)')
#     if play_again=='y': continue
#     else: break

def has_more_characters(str1: str, str2: str) -> str:
    if len(str1)>=len(str2): return str1
    else: return str2


str1='!'*random.randint(1,10)
str2='#'*random.randint(1,15)
print('string 1: ', str1)
print('string 2: ', str2)
print(f'{has_more_characters(str1,str2)}')



len()