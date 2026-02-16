import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

pass_letter = ""
pass_num = ""
pass_symbol = ""
password = ""

print("Welcome to the PyPassword Generator!")

letter_num = int(input("How many letters would you like in your password? (Enter a number): "))
if letter_num == 0:
    print("Please enter a number")
else:
    number_num = int(input("How many numbers would you like? (Enter a number): "))
    if number_num == 0:
        print("Please enter a number")
    else:
        symbol_num = int(input("How many symbols would you like? (Enter a number): "))
        if symbol_num == 0:
            print("Please enter a number")
        else:
            for i in range(letter_num):
                random_letter = random.choice(letters)
                pass_letter += random_letter
                # pass_letter += random.choice(letters)
                # print(pass_letter)

            for j in range(number_num):
                random_number = random.choice(numbers)
                pass_num += random_number

            for k in range(symbol_num):
                random_symbol = random.choice(symbols)
                pass_symbol += random_symbol

pass_word = list(pass_letter + pass_num + pass_symbol)
print(pass_word)
random.shuffle(pass_word)
# print(i)

for i in pass_word:
    password += i
# print(i)

print(f"Your password is: {password}")
