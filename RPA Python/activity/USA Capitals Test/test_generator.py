import os
import random
import usa_capitals

os.chdir('./activity/USA Capitals Test')

for test in range(35):
    states = list(usa_capitals.capitals.keys())
    random.shuffle(states)
    capitals = list(usa_capitals.capitals.values())
    random.shuffle(capitals)
    file = open(f"Test#{test+1}.txt", 'w')
    file.write(f"Name:\n\nDate:\n\nPeriod:\n\nUSA CAPITALS (Form {test+1})\n\n")
    
    for qst_num, chosen_state in enumerate(states, 1):
        right_answer = usa_capitals.capitals[chosen_state]
        
        alternatives = [right_answer]
        letter = ['A', 'B', 'C', 'D']

        for alt in range(3):
            cap_alt = random.choice(capitals)
            while cap_alt == right_answer:
                cap_alt = random.choice(capitals)
            alternatives.append(cap_alt)

        file.write(f"{qst_num}. What is capital of {chosen_state}?\n")

        random.shuffle(alternatives)

        for lt, opt in zip(letter, alternatives):
            file.write(f"   {lt}) {opt}\n")
             
    file.close()
