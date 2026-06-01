# We have written the solutions in multiple different ways
# as a demonstration of different techniques
# Use whichever one makes the most sense to you.
# It's also good to compare/contrast!

# Uncomment the problem you're working on and run the script
# using `python path/to/script.py`

# You can comment/uncomment blocks of code by highlighting
# the lines and using 'Ctrl + /'

########################
## Solution Problem 1a
########################

# user_name = input("What is your name? ")
# favorite_number = input("What is your favorite number? ")

# num_asterisks = 30
# print('*' * num_asterisks) # print the header line

# greeting = 'Hello, ' + user_name.strip().title() + '!' # clean up the user's name a little bit
# white_space_length = (30 - len(greeting) - 3) # how many spaces do we need?
# print('* ' + greeting + ' ' * white_space_length + '*')

# favorite_number = 'Your favorite number is ' + favorite_number
# print('* ' + favorite_number + '  *')

# print('*' * num_asterisks) # print the last header line

########################
## Solution Problem 1b
########################

# user_name = input("What is your name? ")
# favorite_number = input("What is your favorite number? ")

# num_asterisks = 30
# print('*' * num_asterisks) # print the header line

# greeting = 'Hello, ' + user_name.strip().title() + '!' # clean up the user's name a little bit
# print(f'* {greeting:<26} *') # use an f-string plus string formatters

# favorite_number = 'Your favorite number is ' + favorite_number
# print(f'* {favorite_number:<26} *')

# print('*' * num_asterisks) # print the last header line

########################
## Solution Problem 1c
########################

# user_name = input("What is your name? ")
# favorite_number = input("What is your favorite number? ")
# greeting = 'Hello, ' + user_name.strip().title() + '!' # clean up the user's name a little bit
# favorite_number = 'Your favorite number is ' + favorite_number

# necessary_length = max(len(greeting), len(favorite_number))

# num_asterisks = necessary_length + 4 # needs some extra for the '* ' and ' *'
# print('*' * num_asterisks) # print the header line
# print(f'* {greeting:<{necessary_length}} *') # Note the extra '{}' surrounding the 'necessary_length'
# print(f'* {favorite_number:<{necessary_length}} *')
# print('*' * num_asterisks) # print the last header line

########################
## Solution Problem 1c - Bonus
########################
# user_name = input("What is your name? ")
# favorite_number = input("What is your favorite number? ")
# greeting = 'Hello, ' + user_name.strip().title() + '!' # clean up the user's name a little bit
# favorite_number = 'Your favorite number is ' + favorite_number

# necessary_length = max(len(greeting), len(favorite_number))

# num_asterisks = necessary_length + 4 # needs some extra for the '* ' and ' *'
# print('*' * num_asterisks) # print the header line
# print(f'* {greeting:<{necessary_length}} *') # Note the extra '{}' surrounding the 'necessary_length'
# print(f'* {favorite_number:<{necessary_length}} *')
# print('*' * num_asterisks) # print the last header line

# print(f'Raw input type: {type(favorite_number)}')
# print(f'  As int: {int(favorite_number)}')
# print(f'  As float: {float(favorite_number)}')

########################
## Solution Problem 2a
########################
# print(list(range(1, 16)))
# print(list(range(2, 31, 2)))
# print(list(range(20, -1, -1)))

########################
## Solution Problem 2b
########################
# for num in range(1, 16):
#     print(num, end=' ')
# print()

# for num in range(2, 31, 2):
#     print(num, end=' ') 
# print()

# for num in range(20, -1, -1):
#     print(num, end=' ')
# print()

########################
## Solution Problem 2c - bonus
########################
# user_start = int(input('Enter the start value (inclusive): '))
# user_end = int(input('Enter the end value (exclusive): '))
# user_step = int(input('Enter the number of values you want to skip (0 for none): '))
# user_step = user_step + 1 # skipping one number means a step of two

# for num in range(user_start, user_end, user_step):
#     print(num, end=' ')
# print()

########################
## Solution Problem 3
########################
# user_name = input("ENTER SOLDIER NAME: ")
# user_rank = input("ENTER RANK: ")
# user_pushups = int(input("PUSH-UPS COMPLETED: "))
# user_2mr = float(input("2-MILE RUN TIME (minutes): "))

# print()
# print('=== AFTER-ACTION REPORT ===')
# print(f'Soldier: {user_rank} {user_name}')
# print(f'Push-ups: {user_pushups}')
# print(f'2-mile run: {user_2mr:.1f} minutes') # limit to one decimal place
# print(f'Average pace: {user_2mr / 2:.1f} per mile')
# print('DISMISSED.')

########################
## Solution Problem 4a
########################
# print('--- Road Trip Fuel Estimate ---')
# user_distance =     int(input('Distance (miles)       : '))
# user_efficiency = float(input('Fuel efficiency (MPG)  : '))
# user_price =      float(input('Gas price ($/gal)      : '))

# gals_needed = user_distance / user_efficiency
# total_cost = gals_needed * user_price

# print() # a little white space is nice
# print(f'Gallons needed       : {gals_needed:>7.1f}')
# print(f'Total fuel cost      : ${total_cost:>7.2f}')

########################
## Solution Problem 4a
########################
# print('--- Road Trip Fuel Estimate ---')
# user_distance =     int(input('Distance (miles)       : '))
# user_efficiency = float(input('Fuel efficiency (MPG)  : '))
# user_price =      float(input('Gas price ($/gal)      : '))

# gals_needed = user_distance / user_efficiency
# print()
# print(f'Gallons needed       : {gals_needed:>7.1f}')

# for offset in range(0, 3):
#     offset = offset * 0.5
#     total_cost = gals_needed * (user_price + offset)

#     print(f'Gas at (${user_price + offset:.2f})       : ${total_cost:>7.2f}')