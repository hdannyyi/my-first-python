#Print a Square

"""stars = "*****"
star_rows = 1

while star_rows < 6:
    star_rows = star_rows + 1
    print(stars)
"""

#Print a Square 2


stars = "*"
user_input = int(input('How big is the square?'))
count = 0

while count < user_input:
    print(stars * user_input)
    count += 1