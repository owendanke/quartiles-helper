# helper functions

def is_vowel(letter: chr):
    """ Returns True if a given letter is a vowel """
    vowels = set(['a','e','i','o','u','y'])
    if vowels.intersection(letter):
        return True
    else:
        return False
    
def is_word(word: str, eng_dict: dict):
    """ Returns a tuple of the word's validity and definition
    True if the word is real and False if it isn't 
    definition if the word is real 
    """

    if word in eng_dict:
        return (True, eng_dict[word])
    else:
        return (False, "")
    
class solvers():
    
    def __init__(self, game: iter, eng_dict: dict):
        self.game = game
        self.active_dictionary = eng_dict
        self.max_depth = 4      # trivial depth limit from game rule
        self.solution_list = list()
    
    def bfs(self):
        pass

    def dfs(self):
        #for tile in self.game:
        pass            

    def iddfs(self):
        pass

    def bruce(self):
        """ Brute force all possible sollutions to a game. """
        
        for length in range(1, 5):
            print("Finding words of length ", length)
            # assemble all combinations of the current length
            combinations = [_ for _ in self.game]
            # check if combination is a word
            for possible_word in combinations:
                print(possible_word, is_word(possible_word, self.active_dictionary)[0])

            break
