import re
from nltk import SyllableTokenizer

punktuation_mark_re = {'is_exclamative': re.compile(r'.+!$'),
                       'is_interrogative': re.compile(r'.+\?!?$')}

direct_speech_re = re.compile(r':?\s?[–«](\s?[А-Я].+?)[,.?!»]', re.DOTALL)

RUSSIAN_SONORITY_HIERARCHY = [
    "уеыаоэёюияь", # vowels
    "мн",          # nasals
    "фвсзшщхцчж",  # fricatives
    "лй",          # approximant
    "пбтдкгр",     # stops
]
SSP = SyllableTokenizer('ru', sonority_hierarchy=RUSSIAN_SONORITY_HIERARCHY)