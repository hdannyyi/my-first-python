#Print a box

width = int(input("What is the width?"))
height = int(input("What is the height?"))

y = 0
while y < height:
    x = 0
    while x < width: 
        top = (y == 0)
        bottom = (y == (height - 1))
        left = (x == 0)
        right = (x == (width - 1))
        if top or bottom or left or right:
            print('*', end='')
        else:
            print(' ', end='')
        x = x + 1
    print()
    y = y + 1