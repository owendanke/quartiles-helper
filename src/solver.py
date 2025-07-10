def load_eng_dict():
    """ Loads all English words to a python set """

    with open("land_data/words") as words_file:
        words_list = set(words_file.read().split())
    
    return words_list

def load_bigrams():
    pass

def load_games():
    """ Load a list of quartiles games 
        There are five example games
    """
    games_list = list()
    with open('games') as games_file:
        for game in games_file:
            games_list.append([tile for tile in game.split()])

    return games_list


def find_solutions(game):
    """ Find all five solutions to a game """

    games = load_games()
    current_game = games[game]

    solutions = list()

    

    return solutions

if __name__ == "__main__":
    #print("Loading dictionary...")
    find_solutions(1)
    