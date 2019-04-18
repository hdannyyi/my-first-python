#Print a triangle
stars = 0
user_input = int(input('How tall is your pyramid? '))

while stars <= user_input:
    print(((' ') * (user_input - stars)) + ('*' + ('*' * (stars * 2))))
    stars += 1