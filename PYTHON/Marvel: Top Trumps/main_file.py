from hero_card_class import HeroCard
from game_rules_class import GameRules


spiderman = HeroCard("Spiderman", "1B", 175, 7, 36, 11, 66)
daredevil = HeroCard("Daredevil", "1D", 180, 5, 23, 3, 88)
wolverine = HeroCard("Wolverine", "1C", 158, 5, 35, 6, 95)
hulk = HeroCard("Hulk", "1A", 210, 2, 50, 6, 73)

cards = (spiderman, daredevil, wolverine, hulk)

print(GameRules.shuffle(cards))