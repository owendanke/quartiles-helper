import csv
from PIL import Image
import lib.helpers
import lib.solver as alg
import lib.game_ocr
from pathlib import Path

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


def load_games():
    """ Load a list of quartiles games 
        There are five example games
    """
    games_list = list()
    with open('src/games') as games_file:
        for game in games_file:
            games_list.append([tile for tile in game.split()])

    return games_list

if __name__ == "__main__":
    games = load_games()
    dictionary = load_eng_dict()

    Solver = alg.solver(games[3], dictionary)
    solutions = Solver.brute()
    print(solutions)

    print(Solver.length_hint([], 4))

    project_root = Path(__file__).parent
    test_image = 'IMG_4D2175EF60A8-1.jpeg'
    image_path = project_root.parent / test_image

    #lib.game_ocr.ocr_test(Image.open(test_image))
    #lib.game_ocr.find_grid(str(image_path))