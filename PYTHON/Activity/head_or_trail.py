"""
Head or Trail:
- Read round_number
- Read winner of the round → only 0(head) or 1(trail) in input
- Save scoreboard between rounds
- Show Maria's victories or João's victories
"""
round_number = int(input("Number of rounds: "))
head_trail_options = [0, 1]
round_results = []

for round in range(1, round_number + 1):
    round_winner = -1
    while round_winner not in head_trail_options:
        round_winner = int(input(f"Round {round}! Head[0] or Trail[1]? "))
        round_results.append(round_winner)

print(f"GAME OVER! Maria's Victories: {round_results.count(0)} | João's Victories: {round_results.count(1)}")