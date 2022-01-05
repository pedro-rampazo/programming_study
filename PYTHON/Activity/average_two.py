"""
Average Two
- Read four scores: N1(float), N2(float), N3(float), N4(float)
- Create list of weights → 2(int), 3(int), 4(int), 1(int)
- First average(float) = ((N1 . W1) + (N2 . W2) + (N3 . W3) + (N4 . W4)) / (W1 + W2 + W3 + W4)
- Conditional:
    → First average(float) >= 7 → Approved Student
    → 5 <= First average(float) <= 6.9 → In exam student
    → First average(float) < 5 → Reproved Student
- "In exam student" situation:
    → Read Exam Score(float)
    → Second average(float) = (Exam score(float) + First average(float)) / 2
    → Conditional:
        → Second average(float) >= 5 → Approved student
        → Second average(float) <= 4.9 → Reproved student
    → Print final average
"""
scores = []
weights = [2, 3, 4, 1]

for position in range(1, 5):
    position = float(input(f"Insert your {position} score: "))
    scores.append(position)

main_average = float(( \
    (scores[0] * weights[0]) + \
    (scores[1] * weights[1]) + \
    (scores[2] * weights[2]) + \
    (scores[3] * weights[3]) \
    )) \
    / \
    (sum(weights))

print(f"MAIN AVERAGE: {main_average}")

if main_average >= 7:
    print("Approved Student!!")
elif main_average < 5:
    print("Reproved Student!!")
else:
    exam_score = float(input("Insert exam score: "))
    second_average = float((exam_score + main_average) / 2)
    print(f"NEW AVERAGE: {second_average}")
    if second_average >= 5:
        print("Approved Student!!")
    else:
        print("Reproved Student!!")
