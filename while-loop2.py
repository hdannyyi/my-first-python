#Prompt user over and over and over again until they say "bye"
#but if they say "bye" three times just exit the program

#set our bye_count to 0, no one has said anything yet

"""bye_count = 0

while bye_count < 3:
    should_run = True

    while should_run:
        user_input = input("What?")
        print("%s" % (user_input))
        if user_input == "bye":
            should_run = False

            bye_count = bye_count + 1
        print(bye_count)"""


#How many coins?

coin_count = 0
should_run = True

while should_run:
    print('You have %d coins.' % (coin_count))
    user_input = input('Do you want another?')
    if user_input == "yes":
        coin_count = coin_count + 1
    elif user_input == "no":
        should_run = False
        print("bye")

    
        
        
