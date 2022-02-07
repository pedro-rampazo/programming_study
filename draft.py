import random

fruit = ["Banana", "Lemon", "Pineapple", "Watermelon"]
list_one = []
list_two = []

while len(fruit) != 0:
    get_fruit_one = random.choice(fruit)
    list_one.append(get_fruit_one)
    fruit.remove(get_fruit_one)
    get_fruit_two = random.choice(fruit)
    list_two.append(get_fruit_two)
    fruit.remove(get_fruit_two)

print(fruit)
print(list_one)
print(list_two)
