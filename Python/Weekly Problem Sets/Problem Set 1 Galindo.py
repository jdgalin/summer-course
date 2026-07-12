### Problem 1
print("Problem 1\n")
name     = input("Enter your name: ")
number   = input("Enter your most favorite number: ")
nametext = f'* Hello {name}!'
numtext  = f'* your favorite number is {number}.'
border_length = len(max(nametext, numtext, key=len))+2
print('*'*border_length)
print(nametext.ljust(border_length-2)+' *')
print(numtext.ljust(border_length-2)+' *')
print('*'* border_length)
print(f'\n\n\nRaw input type: {type(number)}\nAs int: {int(float(number)//1)} --> {type(int(float(number)//1))}\nAs float: {float(number)} --> {type(float(number))}')

### Problem 2
print("\n\nProblem 2\n")
print(*list(range(1,15+1)))
for index in range(2,31,2): print(index, end=' ')
print()
for index in range(30,-1,-2): print(index, end=' ')
print('\n\n')

while True:
    try: start=int(input("enter a start value: "))
    except ValueError: print("please enter an integer value for start")
    else: break
while True: 
    try: stop=int(input("please enter stop value: "))
    except ValueError: print("please enter an integer value for stop")
    else: break
while True:
    try: 
        step=int(input("enter a step value: "))
        if step==0: 
            print("step value cannot be zero")
            continue
        elif step<0 and start<stop: 
            print("step value cannot be negative if start is less than stop") 
            continue
        elif step>0 and start>stop: 
            print("step value cannot be positive if start is greater than stop")
            continue
    except ValueError: print("please enter an integer value for step")
    else: break
print(*list(range(start, stop+step, step)))

### Problem 3
print("\n\nProblem 3\n")
name = input("ENTER SOLDIER NAME: ")
rank = input("ENTER SOLDIER RANK: ")
while True:
    try: push_ups   = int(input("ENTER PUSH UPS COMPLETED: "))
    except ValueError: print("please enter an integer value for push ups completed")
    else: break
while True:
    try: 
        run_time = input("ENTER RUN TIME (MM:SS): ").split(':')
        if len(run_time) == 2: run_time = int(run_time[0])*60 + int(run_time[1])
        else: raise ValueError
    except ValueError: print("please enter a valid time in the format MM:SS")
    else: break

print(f'''\n
=== AFTER-ACTION REPORT ===
Soldier: {rank} {name}
Push-ups: {push_ups}
2-mile run: {run_time//60:02d}:{run_time%60:02d}
Average pace: {int((run_time/2)//60):02d}:{int((run_time/2)%60):02d} per mile
DISMISSED.''')

### Problem 4
print("\n\nProblem 4\n")
while True:
    try:
        distance = float(input("Enter the distance in miles: "))
        break
    except ValueError:
        print("Please enter a valid number for the distance.")
while True:
    try:
        mpg = float(input("Enter the vehicle's fuel efficiency (miles per gallon): "))
        break
    except ValueError:
        print("Please enter a valid number for the fuel efficiency.")
while True:
    try:
        price_per_gallon = float(input("Enter the price of fuel per gallon: "))
        break
    except ValueError:
        print("Please enter a valid number for the price of fuel.")

gallons_needed = distance / mpg
total_cost = gallons_needed * price_per_gallon
print(f"\nFuel needed: {gallons_needed:.2f} gallons")
print(f"Total cost: ${total_cost:.2f}") 

print("\n--- Price Scenarios ---")
for price in range(int(price_per_gallon*100), int(price_per_gallon*100+101),50):
    print(f'Gas @ ${price/100:.2f}/gal: Total = ${gallons_needed*price/100:.2f}')