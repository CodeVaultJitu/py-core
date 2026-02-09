print("Welcome to the roller costers!")
height =  int(input("How tall are you in cm? "))
age = int(input("How old are you? "))
bill = 0
wants_photo = input("Would you like to have a photo taken of you? (y/n) ")

if height >= 120:
    print("You can ride")
    if age <= 12:
        print("your ticket price is $5")
        bill = 5
    elif age <= 18:
        print("your ticket price is $7")
        bill = 7
    else:
        print("your ticket price is $12")
        bill = 12
    #this if should be inside the previous if loop
    if wants_photo == "y":
        bill += 3
    #loop ends
    print(f"and your bill is: ${bill}")
else:
    print("You can't ride.")
