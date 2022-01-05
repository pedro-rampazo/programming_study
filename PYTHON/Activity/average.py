"""
Read grade_one(float) and grade_two(float) - the grades must be between 0 and 10
Read weights(list) with 3.5 and 7.5 values
Average equation = (grade1 * weight1) + (grade2 * weight2) / weight1 + weight2
Print Average
"""
grade_one = -1
grade_two = -1
weights = [3.5, 7.5]

while grade_one < 0 or grade_one > 10:
    grade_one = float(input("GRADE 1: "))

while grade_two < 0 or grade_two > 10:
    grade_two = float(input("GRADE 2: "))

average = ((grade_one * weights[0]) + (grade_two * weights[1])) / (weights[0] + weights[1])

print(f"GRADE 1 = {grade_one} \
        WEIGHT 1 = {weights[0]} | \
        GRADE 2 = {grade_two} \
        WEIGHT 2 = {weights[1]} | \
        AVERAGE = {average}")
