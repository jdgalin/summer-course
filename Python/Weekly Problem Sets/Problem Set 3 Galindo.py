import random
import numpy as np
import math
###PROBLEM 1
print('Problem 1\n\n')

def roll(sides):
    return random.randint(1,sides)
def roll_many(num_dice,sides):
    result = []
    for die in range(num_dice):
        result.append(random.randint(1,sides))
    return result
def display_check(check):
    print('rolls: ', end='')
    total= sum(check)
    for roll in check:
        print(roll, end=' ')
    print(f'\ntotal roll: {total}')
    return 0
move_check=roll_many(2,6)
print('movement check: ')
display_check(move_check)
print()

attack_check=roll(20)
match attack_check:
    case 1:  print("1-CRITICAL MISS!")
    case 20: print("20-CRITICAL HIT!")
    case _:print(f'attack: {attack_check}')

print('\ndamage check: ')
damage=roll_many(3,8)
display_check(damage)
print()

total=[]
for iteration in range(1000):
    total.append(sum(roll_many(3,8)))
print(f'average of 1000 damage rolls: {sum(total)/len(total)}')

final_message=random.choice(['hell yeah', 'get some', 'fight fight fight', 'mucho bueno', 'option 5'])
print(f'\n{final_message}')

### PROBLEM 2
print('\nProblem 2\n\n')

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def orbit_circumference(radius):
    return radius*2*math.pi

def fuel_needed(mass, velocity):
    return math.floor((0.5 * mass * (velocity ** 2))*100)/100

def navigation_report(ship_pos, station_pos, orbit_radius,ship_mass,ship_velocity):
    print(f'''NAVIGATION REPORT:
          
ship position:          {ship_pos}
station position:       {station_pos}
distance to station:    {distance(ship_pos[0],station_pos[0],ship_pos[1],station_pos[1]):.0f}
orbit radius:           {orbit_radius}
orbit circumference:    {orbit_circumference(orbit_radius):.02f}
ship mass:              {ship_mass}
ship velocity:          {ship_velocity}
fuel required:          {fuel_needed(ship_mass, ship_velocity):.02f}

ship velocity(log10):{math.log(ship_velocity, 10)}
''')
    
navigation_report([0,0],[143,892],6371,5,78)
# ## Problem 2 — Space Mission Calculator 🚀

# *Your spacecraft navigation system needs precise calculations. Import the `math` module to power the nav computer.*

# **Your task:**

# - Import the `math` module.
# - Write a function `distance(x1, y1, x2, y2)` that calculates the straight-line distance between two points in space using the distance formula. Use `math.sqrt()`.
# - Write a function `orbit_circumference(radius)` that calculates the circumference of a circular orbit. Use `math.pi`.
# - Write a function `fuel_needed(mass, velocity)` that calculates kinetic energy as `0.5 * mass * velocity ** 2`, then returns the result rounded to 2 decimal places using `math.floor()`.
# - Use the functions to print a navigation report for the following mission data:

# ```python
# ship_pos    = (0, 0)
# station_pos = (143, 892)
# orbit_radius = 6371        # km (Earth's radius)
# ship_mass    = 50000       # kg
# ship_velocity = 7800       # m/s
# ```

# - Also print `math.log(ship_velocity, 10)` and explain in a comment what this value represents.