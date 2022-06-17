"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine to find random words from a dictionary.
    >>> wf = WordFinder("dictionary.txt")
    3 words read

    >>> wf.random() in ["pepperoni", "pineapple", "onion"]
    "pineapple"
    """
    
    def __init__(self, path):
        """Read dictionary and print number of items."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dictionary into a list of words"""

        return [val.strip() for val in dict_file]


    def random(self):
        """Return random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Modified Wordfinder to find random words in a subcategory, given a file of words
    >>> swf = SpecialWordFinder("specialDictionary.txt")
    3 words read

    >>> swf.random() in ["purple", "green", "blue"]
    "purple"
    """
    
    def parse(self, dict_file):
        """Parse dictionary to list of words, skipping blanks and comments"""
        
        return [val.strip() for val in dict_file if val.strip() and not val.startswith("#")]

