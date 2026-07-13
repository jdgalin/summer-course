import math
import random
import numpy as np

###Problem 1
print('\nProblem 1\n')
def pizzas_needed(people, slices_per_person, slices_per_pizza, extra_percent=0):
    return int(math.ceil(people *(1+extra_percent/100) * slices_per_person / slices_per_pizza))

def leftover_slices(people, slices_per_person, slices_per_pizza, extra_percent=0):
    return int(pizzas_needed(people, slices_per_person, slices_per_pizza, extra_percent) * slices_per_pizza - people * slices_per_person)
while True:
    try:
        people = int(input("How many guests? "))
        slices_per_person = int(input("Slices per person: "))
        slices_per_pizza = int(input("Slices per pizza: "))
        break
    except ValueError:
        print("Please enter valid integer values.")

print(f'''===PIZZA PARTY PLANNER===
Guests: {people}
Pizzas to order: {pizzas_needed(people, slices_per_person, slices_per_pizza, 15)}
Total slices: {people * slices_per_person}
Leftover slices: {leftover_slices(people, slices_per_person, slices_per_pizza, 15)}
      ''')



###Problem 2
print('\nProblem 2\n\n')

class hourly_o2_reading:
    def __init__(self):
        self.number  = 0
        self.reading = 0
        self.status  = ''
        self.trend   = 'N/A'

def o2_status(level):
    match level:
        case x if x <  15 and x >= 0: return 'CRITICAL'
        case X if x <= 18 and x >=15: return 'LOW'
        case x if x <= 23 and x > 18: return 'NORMAL'
        case x if x >  23 and x <100: return 'HIGH'
        case _: return 'INVALID READING'    

def trend(index):
        if  index == 0: return 'N/A'
        elif readings[index] >  readings[index-1]: return 'IMPROVING'
        elif readings[index] <  readings[index-1]: return 'DECLINING'  
        elif readings[index] == readings[index-1]: return 'STABLE'

def trend_end(readings):
    if readings[-1] > readings[-3]: return 'IMPROVING'
    elif readings[-1] < readings[-3]: return 'DECLINING'  
    elif readings[-1] == readings[-3]: return 'STABLE'  

readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]

status_counts = { 'CRITICAL': 0, 'LOW': 0, 'NORMAL': 0, 'HIGH': 0, 'INVALID READING': 0 }
reading = hourly_o2_reading()
for index in range(len(readings)):
    reading.number = index + 1
    reading.reading = readings[index]
    reading.status = o2_status(readings[index])
    reading.trend = trend(index)
    status_counts[reading.status] += 1
    print(f'''Hour {reading.number:02d}: {reading.reading:02d}% -- {reading.status} -- Trend: {reading.trend}''')
    if reading.status == 'CRITICAL': print("*** ALERT: TAKE ACTION IMMEDIATELY ***")
print(f'''
=== STATUS SUMMARY ===
CRITICAL: {status_counts['CRITICAL']} hours
LOW:      {status_counts['LOW']} hours
NORMAL:   {status_counts['NORMAL']} hours
HIGH:     {status_counts['HIGH']} hours
''')
print(f'Trend last 3 hours: {trend_end(readings)}\n')

### Problem 3
print('\nProblem 3\n\n')

def attack(defender_hp, damage):
    return max(0, defender_hp - damage)

def is_alive(defender_hp):
    return defender_hp > 0

def critical_hit(damage):
    roll = random.randint(1, 10)
    if roll < 3:
        print('*** CRITICAL HIT ***')
        return damage * 2
    else:
        return damage

hero_hp = 100
monster_hp = 90
round=1
print('=== BATTLE START ===')
while True:
    hero_hp=attack(hero_hp, 12)
    monster_hp=attack(monster_hp, critical_hit(18))
    print(f'Round {round}: Hero HP: {hero_hp} | Monster HP: {monster_hp}')
    if not is_alive(hero_hp): print('MONSTER WINS! The hero is defeated.'); break #Monster strikes first
    if not is_alive(monster_hp): print('HERO WINS! The monster is defeated.'); break
    round += 1


###Problem 4
print('\nProblem 4 \n\n')

def check_fitness(score):
    return score >= 70
 
def check_rank(rank):
    return rank in ['Corporal', 'Sergeant', 'Lieutenant']
 
def check_service_years(years):
    return years >= 2

name  = input('enter name: ')
rank  = input('enter rank: ')
score = input('enter fitness score: ')
years = input('enter years of service: ')


#check_fitness       = "PASS" if check_fitness(score)==True else "FAIL"
#check_rank          = "PASS" if check_rank(rank)==True else "FAIL"
#check_service_years = "PASS" if check_service_years(years)==True else "FAIL"

cleared=True
checks = [
    ("Fitness check", check_fitness(score), score),
    ("Rank check", check_rank(rank), rank),
    ("Service check", check_service_years(years), years),
]
print(f'''=== MISSION CLEARANCE REPORT ===
Soldier: {name}
''')
for check in checks:
    print(f'{check[0]}: ',"PASS" if check[1]==True else "FAIL")
    if check[1]==False: cleared=False

if cleared==False: print('\nFINAL STATUS: NOT CLEARED FOR MISSION.')
else: print('\nFINAL STATUS: CLEARED FOR MISSION.')


###Problem 5
print('\nProblem 5\n\n')

athletes = [
    ("Jordan",  82, 15),   # (name, games_played, goals_scored)
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
]

def goals_per_game(goals, games):
    gpg=goals/games
    gpg=round(gpg, 2)
    return gpg

def mvp_candidate(gpg):
    return True if gpg>= .25 else False

def grade(gpg):
    match gpg:
        case x if x<.10:            grade='F'
        case x if x>=.10 and x<.15: grade='D'
        case x if x>=.15 and x<.20: grade='C'
        case x if x>=.20 and x<.25: grade='B'
        case x if x>=.25:           grade='A'
    return grade


print('=== SEASON LEADERBOARD ===')
headings=['Athlete ', 'Games', 'Goals', 'GPG','Grade', 'MVP?']
for heading in headings:
    width=int(len(heading)+2)
    print(f'{heading}', end=('  '))
print()
print('-'*len(heading))
for athlete in athletes:
    goals = athlete[2] ; games = athlete[1]
    gpg=goals_per_game(goals, games)
    athlete_grade=grade(gpg)
    if mvp_candidate(gpg): mvp = "*" 
    else: mvp = " "
    print(f'{athlete[0]:<9}', f'{athlete[1]:<6}', f'{athlete[2]:<6}', f'{gpg:<5}', f'{athlete_grade:<6}', f'{mvp}')