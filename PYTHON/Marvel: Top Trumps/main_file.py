from hero_card_class import HeroCard
from game_rules_class import GameRules

spiderman = HeroCard("Spiderman", "1B", 175, 7, 36, 11, 66)
daredevil = HeroCard("Daredevil", "1D", 180, 5, 23, 3, 88)
wolverine = HeroCard("Wolverine", "1C", 158, 5, 35, 6, 95)
hulk = HeroCard("Hulk", "1A", 210, 2, 50, 6, 73)

cards = [spiderman, daredevil, wolverine, hulk]
attribute_options = ["height", "intelligence", "force", "speed", "ability"]

players_cards = GameRules.shuffle(cards)

while len(players_cards[0]) != 0 and len(players_cards[1]) != 0:
    while card_attribute not in attribute_options:
        card_attribute = input(f"""
    HERO/VILLAIN:   {players_cards[0][0].name}
    CARD:           {players_cards[0][0].card}
    --------------------------------------------------
    HEIGHT:         {players_cards[0][0].height}
    INTELLIGENCE:   {players_cards[0][0].intelligence}
    FORCE:          {players_cards[0][0].force}
    SPEED:          {players_cards[0][0].speed}
    ABILITY:        {players_cards[0][0].ability}
    Insert a attribute for the battle:
    """)
    card_attribute = card_attribute.lower()

    if card_attribute == attribute_options[0]:
        if players_cards[0][0].height > players_cards[1][0].height: