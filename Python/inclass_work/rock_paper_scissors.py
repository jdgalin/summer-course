import random

choices=['rock', 'paper', 'scissors', 'gun']

def get_choice():
    while True:
        try: user_choice=input('enter rock, paper, or scissors? ')
        except ValueError: print('how did you manage to screw this up?')
        if user_choice in choices: break
        else: print('follow directions next time.')
    return choices.index(user_choice)


def play_round(user, computer, score):
    print(f'user choose {choices[user]}. \ncomputer choose {choices[computer]}.')
    match user:
        case user if user > computer and user !=2: 
            score[0]+=1
            print('player wins this round\n')
        case user if user == computer: 
            print('tie, go again\n')
        case _: 
            score[1]+=1
            print('computer wins this round\n')
    return score 


def play_set():
    score=[0,0] #[player,computer]
    while True:
        try: num_games=int(input('how many games would you like to play(1,3,5,7, or 9)?'))
        except ValueError: 
            print("what's wrong with you?")
            continue
        if num_games in [1,3,5,7,9]: break
        else: print('that was not an option')

    while score[0]<(num_games//2)+1 and score[1]<(num_games//2)+1:
        user_choice=get_choice()
        computer_choice=random.randint(0,2)
        score=play_round(user_choice,computer_choice,score)
        print(f'rounds won: \nplayer: {score[0]}   computer: {score[1]} ')
    

    if score[0]>score[1]: winner='player' 
    else: winner='computer' 
    print(f'\nThe winner is {winner}!\n\n')

    play_again=input('would you like to play again? (y/n)')
    return play_again

while True:
    play_again=play_set()
    if play_again!=('y'): break