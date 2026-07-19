import random
import math
import turtle
import numpy as np


# ###PROBLEM 1
# print('Problem 1\n\n')

# def roll(sides):
#     return random.randint(1,sides)
# def roll_many(num_dice,sides):
#     result = []
#     for die in range(num_dice):
#         result.append(random.randint(1,sides))
#     return result
# def display_check(check):
#     print('rolls: ', end='')
#     total= sum(check)
#     for roll in check:
#         print(roll, end=' ')
#     print(f'\ntotal roll: {total}')
#     return 0
# move_check=roll_many(2,6)
# print('movement check: ')
# display_check(move_check)
# print()

# attack_check=roll(20)
# match attack_check:
#     case 1:  print("1-CRITICAL MISS!")
#     case 20: print("20-CRITICAL HIT!")
#     case _:print(f'attack: {attack_check}')

# print('\ndamage check: ')
# damage=roll_many(3,8)
# display_check(damage)
# print()

# total=[]
# for iteration in range(1000):
#     total.append(sum(roll_many(3,8)))
# print(f'average of 1000 damage rolls: {sum(total)/len(total)}')

# final_message=random.choice(['hell yeah', 'get some', 'fight fight fight', 'mucho bueno', 'option 5'])
# print(f'\n{final_message}')

# ### PROBLEM 2
# print('\nProblem 2\n\n')

# def distance(x1, y1, x2, y2):
#     return math.sqrt((x2-x1)**2+(y2-y1)**2)

# def orbit_circumference(radius):
#     return radius*2*math.pi

# def fuel_needed(mass, velocity):
#     return math.floor((0.5 * mass * (velocity ** 2))*100)/100

# def bearing(x1, y1, x2, y2):
#     return math.degrees(math.atan2(y2-y1,(x2-x1)))

# def navigation_report(ship_pos, station_pos, orbit_radius,ship_mass,ship_velocity):
#     print(f'''NAVIGATION REPORT:
          
# ship position:          {ship_pos}
# station position:       {station_pos}
# distance to station:    {distance(ship_pos[0],ship_pos[1],station_pos[0],station_pos[1]):.0f}
# bearing to station:     {bearing(ship_pos[0],ship_pos[1],station_pos[0],station_pos[1]):.0f}
# orbit radius:           {orbit_radius}
# orbit circumference:    {orbit_circumference(orbit_radius):.02f}
# ship mass:              {ship_mass}
# ship velocity:          {ship_velocity}
# fuel required:          {fuel_needed(ship_mass, ship_velocity):.02f}

# ship velocity(log10):{math.log(ship_velocity, 10)} 
# ''')
# navigation_report([0,0],[143,892],6371,5,78)



# ## Problem 3 — Animal Habitat Drawing 🐢
# print('\nProblem 3\n\n')

# def draw_rectangle(t:turtle,x:int,y:int,width:int,length:int)->0:
#     t.goto(x,y)
#     t.begin_fill()
#     t.setheading(90)
#     t.forward(width)
#     t.right(90)
#     t.forward(length)
#     t.right(90)
#     t.forward(width)
#     t.right(90)
#     t.forward(length)
#     t.end_fill()
#     return

# def draw_scene(t):
#     #create canvas
#     corner=200
#     t.penup()
#     #create ground
#     t.color("#34C445")
#     draw_rectangle(t, -corner, -corner, corner, 2*corner)
#     #create pond
#     t.goto(0,-(corner/4))
#     t.color('blue')
#     t.begin_fill()
#     t.circle(corner/4)
#     t.end_fill()
#     #draw sky
#     t.color("#90E1FC")
#     draw_rectangle(t,-corner,0,corner,2*corner)
#     #create sun

#     t.goto(corner, corner-40)
#     t.color('yellow')
#     t.begin_fill()
#     t.circle(-40, 90)
#     t.setheading(0)
#     t.forward(40)
#     t.right(90)
#     t.forward(40)
#     t.end_fill()
#     return


# def draw_tree(t, x, y):
#     t.color('brown')
#     draw_rectangle(t,x,y,20,10)
#     t.goto(x+5,y+50)
#     t.color('green')
#     t.begin_fill()
#     t.circle(15)
#     t.end_fill()
#     return



# t=turtle.Turtle()
# t.speed(0)
# draw_scene(t)
# more_trees=0
# num_trees=random.randint(3,25)
# while more_trees <= num_trees:
#     y=random.randint(-200,0)
#     x=random.randint(-200,190)
#     if (x)**2 + (y + 100)**2 <= 50**2: continue #if tree is in pond region, get new x,y values
#     else: 
#         draw_tree(t,x,y)
#         more_trees+=1
# t.goto(-250,-250)
# turtle.done()


# ## Problem 4 — Animal Guessing Game 🐾
# print('\nProblem 4\n\n')

# secret_number=random.randint(0,100)
# user_number= []

# while True:
#     try: user_number.append(int(input("enter an integer value between 1 and 100: ")))
#     except ValueError:
#         print('please follow directions')
#         continue
#     if user_number[-1]>100 or user_number[-1]<0:
#         print('please follow directions')
#         while True:
#             try: user_number[-1]=int(input("enter an integer value between 1 and 100: "))
#             except ValueError:
#                 print('please follow directions')
#                 continue
#     if user_number[-1]==secret_number:
#         print(f'congratulations, the number {secret_number} is correct.\nit took you {len(user_number)} tries.')
#         print(f'your average guess was {math.fsum(user_number)/len(user_number):.0f}.')
#         play_again=input('would you like to try again(y/n)?')
#         if play_again in ['y', 'Y', 'yes','yep','sure']:
#             user_number=[]
#             secret_number=secret_number=random.randint(0,100)
#             continue
#         break
#     if math.fabs(secret_number-user_number[-1])>40: print('Icy')
#     elif math.fabs(secret_number-user_number[-1])>20: print('Cold')
#     elif math.fabs(secret_number-user_number[-1])>10: print('Warm')
#     else: print('Hot')
#     if len(user_number)<2: print('keep guessing')
#     elif math.fabs(secret_number-user_number[-1])< math.fabs(secret_number-user_number[-2]): print('Getting Warmer')
#     elif math.fabs(secret_number-user_number[-1])> math.fabs(secret_number-user_number[-2]): print('Getting Colder')
#     else: print('same temperature')


## Problem 5 — Square Spiral 🌀
print('\nProblem 5\n\n')



num_spirals=int(input('how many spirals would you like? '))
spiral_color=input('enter a color: ')
length=10
added_length=5
colors= ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

s=turtle.Turtle()
s.speed(0)
s.color('black')
s.penup()
s.goto(0,0)
s.pendown()
for spiral in range(0,num_spirals):
    s.setheading(180)
    for lap in range(0,4):
        if spiral_color == 'rainbow': s.color(colors[(lap+spiral)%7])
        else: s.color(spiral_color)
        s.right(90)
        s.forward(length)
        length+=added_length


turtle.done()