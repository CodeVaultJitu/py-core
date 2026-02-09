print("Welcome to the roller costers!")
height =  int(input("How tall are you in cm? "))
age = int(input("How old are you? "))

if height >= 120:
    print("You can ride")
    if age <= 12:
        print("and your ticket price is $5")
    elif age <= 18:
        print("and your ticket price is $7")
    else:
        print("and your ticket price is $12")
else:
    print("You can't ride.")
