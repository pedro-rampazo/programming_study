import random

class GameRules:

    def shuffle(self, *cards_list):
        cards_list = list(cards_list)
        player_one = []
        player_two = []
        new_game = []

        while len(cards_list) != 0:
            get_card = random.choice(cards_list)
            player_one.append(get_card)
            cards_list.remove(get_card)
            get_card = random.choice(cards_list)
            player_two.append(get_card)
            cards_list.remove(get_card)
        
        new_game.append(player_one)
        new_game.append(player_two)

        return new_game


    def TopTrumps(self):
        pass