#Prompt user over and over and over again


should_run = True

while should_run:
    user_input = input("What? ")
    print("%s" % user_input)
    if user_input == "bye":
        should_run = False
