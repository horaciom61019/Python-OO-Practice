"""Word Finder: finds random words from a dictionary."""

import random
from tokenize import Ignore

class WordFinder:
    ''' Finds random words from file

        >>> wf = WordFinder("/Users/horacio/Documents/Springboard/Software Engineering Career Track 2/Python Fundamentals/python-oo-practice/words.txt");
        235886 words read

        >>> wf.random() in "/Users/horacio/Documents/Springboard/Software Engineering Career Track 2/Python Fundamentals/python-oo-practice/words.txt"
        True
    '''

    def __init__(self, path):
        ''' Open file and print total words in file '''
        file = open(path)

        self.words = self.wordGrabber(file)

        print(f"{len(self.words)} words read")

    def wordGrabber(self, file):
        ''' Add words in file to a list'''
        # return [w.strip() for w in file]
        list = []

        for w in file:
            list.append(w.strip())
        return list

    def random(self):
        ''' Select random word from words list '''
        print(self.words)
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """ Excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("/Users/horacio/Documents/Springboard/Software Engineering Career Track 2/Python Fundamentals/python-oo-practice/special-words.txt")
    3 words read

    >>> swf.random() in "/Users/horacio/Documents/Springboard/Software Engineering Career Track 2/Python Fundamentals/python-oo-practice/special-words.txt"
    True
    """

    def parse(self, file):
        """Parse file -> list of words, skipping blanks/comments."""
        
        list = []

        for w in file:
            if w.strip() and not w.startswith("#"):
                list.append(w)

        return list



wf = WordFinder("/Users/horacio/Documents/Springboard/Software Engineering Career Track 2/Python Fundamentals/python-oo-practice/words.txt")
sf = SpecialWordFinder("/Users/horacio/Documents/Springboard/Software Engineering Career Track 2/Python Fundamentals/python-oo-practice/special-words.txt")
