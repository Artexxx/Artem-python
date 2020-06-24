from pymorphy2 import MorphAnalyzer as MA
from pymorphy2.analyzer import Parse
#from pymystem3 import Mystem

from typing import Dict


class MorphologyAnalyzer:

    def __init__(self):
        self.__morph: MA = MA()
        self.__cache: Dict = {}

    def parse(self, word: str) -> Parse:
        if word in self.__cache:
            return self.__cache[word]
        else:
            analysis = self.__morph.parse(word)
            self.__cache[word] = analysis[0]
            return analysis[0]


morph = MorphologyAnalyzer()
