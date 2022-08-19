from audioop import reverse
from operator import itemgetter

number_tshirt = int(input("Number of t-shirts: "))
tshirt_list = []

for count in range(number_tshirt, 0, -1):
    student_name = input("Student: ")
    color_size_tshirt = input("Color and size of t-shirt: ")
    color_size_tshirt = color_size_tshirt.split(color_size_tshirt[-2])
    tshirt_feature = (color_size_tshirt[0], color_size_tshirt[1], student_name)
    tshirt_list.append(tshirt_feature)


tshirt_list = sorted(tshirt_list, key = lambda x: (x[0], x[1], x[2]))

for lst in tshirt_list:
    print(f"{lst[0]} {lst[1]} {lst[2]}")

