from random import choice
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
    Initialize the file path and create the list
    >>> word_finder = WordFinder("test.txt")
    4 words read
"
    >>> word_finder.random() in ["Aaronite", "aba", "abac", "abaca"]
    True

    >>> word_finder.random() not in ["Aaronite", "aba", "abac", "abaca"]
    False
    """
    def __init__(self, file):
        self.file = file
        self.list = []
        self.make_list()
        print(f"{len(self.list)} words read")

    def make_list(self):
        """
        Open file and append each line to self.list
        
    """
        with open(self.file) as file:
            for line in file:
                line = line.strip()
                self.list.append(line)
        file.close()

    def random(self):
        """
        Return a random item from word list
        """
        return choice(self.list)
    

class SpecialWordFinder(WordFinder):
    """
    Skip lines that start with #"""
    def make_list(self):
        """
        Parse the line and skip ones that start with #
        """
        with open(self.file) as file:
            for line in file:
                if not line.startswith('#'):
                    line = line.strip()
                    self.list.append(line)
        file.close()
        
