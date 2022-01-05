"""
Game Of The Greatest:
- Read rounds number of the game
- Create loop according with rounds number to read Og's choice and Child's choice
- Create a function() to check if (1 <= N <= 10)
- Create verification to know what number is the greatest
- Count score for the player who won the round
- In the end of the game, show the scoreboard and indicate who won
"""
def check_choice(intern_number):
    if intern_number < 1 or intern_number > 10:
        return False
    else:
        return True


round_number = int(input("Enter the number of rounds: "))
ogs_score = 0
child_score = 0
    
for round in range(1, round_number + 1):
    ogs_choice = 0
    child_choice = 0
    
    while check_choice(ogs_choice) is False or check_choice(child_choice) is False:
        print(f"Round {round}")
        ogs_choice = int(input("Og's Choice: "))
        child_choice = int(input("Child's Choice: "))
        
        if ogs_choice > child_choice:
            print("Round Winner: Og!!!")
            ogs_score += 1
        elif child_choice > ogs_choice:
            print("Round Winner: Child!!!")
            child_score += 1
        else:
            print("A tie!!")

if ogs_score > child_score:
    print(f"Og's Score {ogs_score} X {child_score} Child's Score → WINNER: OG!!!")
elif child_score > ogs_score:
    print(f"Og's Score {ogs_score} X {child_score} Child's Score → WINNER: CHILD!!!")
else:
    print("WINNER: A tie!!")

