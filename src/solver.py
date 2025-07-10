import csv
import algorithms as alg

def load_word_set():
    """ Loads all English words to a python set """

    with open("lang_data/words") as words_file:
        words_list = set(words_file.read().split())
    
    return words_list

def load_eng_dict():
    """ Reads an English dictionary from a file 
    with words as keys and values as definitions
    """
    eng_dict = dict()
    entry = list()
    word = ""
    definition_list = list()
    definition = ""
    word_index = 0
    def_index = 3

    with open('src/lang_data/OPTED-Dictionary.csv') as dict_file:
        # drop first line of file
        header = dict_file.readline()
        reader = csv.reader(dict_file)
        
        # first word case
        row = next(reader)
        word = row[word_index].lower()
        #definition_list = row[2:]
        definition = row[def_index]

        for row in reader:
            if row[word_index] == word:
                # same word, different definition
                # definition_list.append(row[2:])
                pass #skip

            else:
                # different word
                # store word and definitions(s)
                eng_dict[word] = definition

                # reset word and definition(s)
                #print(row[0], len(row))
                word = row[word_index].lower()
                definition = row[def_index]
                #definition_list.clear()
                #definition_list.append(row[2:])

    return eng_dict


def load_bigrams():
    pass

def load_games():
    """ Load a list of quartiles games 
        There are five example games
    """
    games_list = list()
    with open('src/games') as games_file:
        for game in games_file:
            games_list.append([tile for tile in game.split()])

    return games_list


def find_solutions(game):
    """ Find all five solutions to a game """

    games = load_games()
    current_game = games[game]

    solutions = list()

    

    return solutions

def dict_lookup():
    print("Loading dictionary...")
    eng_dict = load_eng_dict()

    while(True):
        print('Type a word to search the dictionary or 99 to exit ')
        query = input()

        if query == '99':
            break

        else:
            print(alg.is_word(query.lower(), eng_dict))

if __name__ == "__main__":
    # dict_lookup()

    games = load_games()
    dictionary = load_eng_dict()

    Solver = alg.solvers(games[0], dictionary)
    Solver.bruce()

    print(Solver)