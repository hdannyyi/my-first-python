#Print a banner
banner = 0
stars = '*'
user_input = input('Text? ')

while banner < 3:
    print('**' + (stars * len(user_input) + '**'))
    print(('* ' + user_input + ' *'))
    print('**' + (stars * len(user_input) + '**'))
    banner += 1 