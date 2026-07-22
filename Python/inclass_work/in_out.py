import random
import os

current_directory=os.path.dirname(__file__)
file_path= os.path.join(current_directory, 'integers.txt')

with open(file_path, 'w') as file:
    for number in range(0,5):
        file.write(f'{str(random.randint(50,100))} \n')

total=0
max=0
min=100
num_lines=0
with open(file_path, 'r', 'w') as file:
    for number in file.readlines():
        number=int(number)
        total+=number
        num_lines+=1
        if number>max: max=number
        if number<min: min=number

average=total/num_lines
print(f'max: {max}\nmin: {min}\n average: {average}')