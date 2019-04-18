#Multiplication table

a = 1
while a < 11:
    b = 1
    while b < 11:
        print('%d X %d = %d' % (a, b, (a * b)))
        b += 1
    a += 1