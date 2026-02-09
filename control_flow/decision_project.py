print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    print("the price is $15")
    bill += 15
    if pepperoni == "Y":
        bill += 2

elif size == "M":
    print("the price is $20")
    bill = 20
    if pepperoni == "Y":
        bill += 3

elif size == "L":
    print("the price is $25")
    bill = 25
    if pepperoni == "Y":
        bill += 3

else:
    print("you typed the wrong inputs")


if extra_cheese == "Y":
    bill += 1

print(f"your bill is: ${bill}")
