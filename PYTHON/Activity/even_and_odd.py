time = int(input("Number of times: "))
number_list = [[], []]


for value in range(0, time):
    number = int(input(f"Insert number {value+1}: "))
    if number % 2 == 0:
        number_list[0].append(number)
    else:
        number_list[1].append(number)

number_list[0].sort()
number_list[1].sort(reverse = True)

for element in number_list:
    for n in element:
        print(n)
