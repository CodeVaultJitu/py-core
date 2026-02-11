import random

#random integer
rand_int = random.randint(1, 2)
print(rand_int)

#random float
# random_float_0to1 = random.random()
# print(random_float_0to1)
#
# random_float = random.uniform(10, 12)
# print(random_float)

if rand_int == 1:
    print("You've got heads.")
else:
    print("You've got tails.")