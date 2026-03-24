import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#option 1
print(random.choice(friends))

choice = random.choice(friends)
print(choice)

#option 2
print(friends[random.randint(0, 4)])