import itertools
import lib.helpers
from random import Random

class solver():
    
    def __init__(self, game: iter, eng_dict: dict):
        self.game = game
        self.dictionary = eng_dict
        self.solution_list = list()

    def brute(self):
        """ Brute force all possible sollutions to a game. """
        
        solutions = list()
        permutations = list()
        
        permutations.append(list(itertools.permutations(self.game, 1)))
        permutations.append(list(itertools.permutations(self.game, 2)))
        permutations.append(list(itertools.permutations(self.game, 3)))
        permutations.append(list(itertools.permutations(self.game, 4)))

        for permutation_subset in permutations:
            solutions.append([''.join(possible_word) for possible_word in permutation_subset if lib.helpers.is_word(''.join(possible_word), self.dictionary)])

        self.solution_list = solutions

        return solutions
    
    def tile_hint(self, found_words: iter, tile: str):
        """ gives a hint based on a tile """
        results = [_ for _ in self.solution]
        pass

    def length_hint(self, found_words: iter, word_length: int):
        """ gives a hint based on the word length (number of tiles) """
        rand = Random()
        all_words = set(self.solution_list[word_length - 1])    # all possible words of given length
        results = list(all_words.difference(found_words))     # every word that hasn't been found

        hint = lib.helpers.get_definition(results[rand.randint(a=0, b=len(results) - 1)], self.dictionary)

        return hint

        