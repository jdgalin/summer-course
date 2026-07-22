def validate_username(username):
    valid=True

    if len(username)>15: valid= False
    elif len(username)<5: valid= False
    if username[0].isalpha()==False: valid = False
    if username[-1].endswith('_'): valid =False
    number=0

    for char in username:
        if char.isdigit()==True: number+=1
        if not(char.isalnum() or char=='_'): valid=False
    if not number>=1: valid=False
    return valid

while True:
    username=input('provide a username: ')
    if validate_username(username)==True: break