import random

#used what i know
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
num = random.randint(0, len(friends))
print(friends[num])

#or from doc
print(random.choice(friends))