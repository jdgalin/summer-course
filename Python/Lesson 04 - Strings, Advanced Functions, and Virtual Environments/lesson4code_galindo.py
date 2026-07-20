def validate_username(username):
    valid=True

    if len(username)>15: valid= False
    elif len(username)<5: valid= False
    print(len(username), valid)
    if username[0].isalpha()==False: valid = False
    print('first letter: ', valid)
    if username[-1].endswith('_'): valid =False
    print('ending', valid)
    number=0

    for char in username:
        if char.isdigit()==True: number+=1
        if not(char.isalnum() or char=='_'): valid=False
        print(char, valid)
    print(number)
    if not number>=1: valid=False
    print(valid)
    print('alphanumeric: ', valid)
    return valid

while True:
    username=input('provide a username: ')
    if validate_username(username)==True: break