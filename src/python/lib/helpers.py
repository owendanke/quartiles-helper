"""
helper functions
"""

def is_vowel(letter: chr):
    """ Returns True if a given letter is a vowel """
    vowels = set(['a','e','i','o','u','y'])
    if vowels.intersection(letter):
        return True
    else:
        return False
    
def is_word(word: str, eng_dict: dict):
    """ True if the word is real and False if it isn't  """

    if word in eng_dict:
        return True
    else:
        return False
    
def get_definition(word: str, eng_dict: dict):
    """ Returns the definition of a real word, None otherwise """
    if word in eng_dict:
        return eng_dict[word]
    else:
        return None