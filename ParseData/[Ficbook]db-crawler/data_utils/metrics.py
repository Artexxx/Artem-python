from .constants import punktuation_mark_re, direct_speech_re, SSP
from .utils import Parse, morph
from typing import List
from nltk import sent_tokenize, word_tokenize
from lazy_property import LazyProperty


class Word:
    syllables: List[str]
    symbols: str
    POS: str
    normal_form: str

    def __init__(self, word: str):
        self.symbols = word
        self.syllables = SSP.tokenize(word)
        analysis: Parse = morph.parse(word)
        self.normal_form = analysis.normal_form
        self.POS = str(analysis.tag.POS)

    def length(self, kind="sym"):
        if kind == 'sym':
            return len(self.symbols)
        elif kind == 'syl':
            return len(self.syllables)


DICT = {}


class Sentence:
    text: str
    is_exclamative: bool
    is_interrogative: bool
    words: List[Word]

    def __init__(self, text: str):
        self.text = text
        self.words = []
        self.__guess_punctuation()
        self.__parse_words()

    def __guess_punctuation(self):
        for name, expression in punktuation_mark_re.items():
            setattr(self, name, bool(expression.match(self.text)))

    def __parse_words(self):
        for word_str in word_tokenize(self.text, 'russian'):
            if word_str not in DICT:
                word = Word(word_str)
                DICT[word_str] = word
            else:
                word = DICT[word_str]
            if word.POS != 'None':
                self.words.append(word)

    def __len__(self):
        return len(self.words)

    def __iter__(self) -> Word:
        for word in self.words:
            yield word

    def __str__(self):
        return self.text

    @LazyProperty
    def syllable_count(self):
        return sum(word.length('syl') for word in self.words)

    @LazyProperty
    def average_symbol_count(self):
        return sum(word.length('sym') for word in self.words) / len(self)

    @LazyProperty
    def average_syllable_count(self):
        return sum(word.length('syl') for word in self.words) / len(self)

    def part_of_speech_count(self, pos_id: List[str]):
        return sum(1 for word in self if word.POS in pos_id)


class Text:
    sentences: List[Sentence]
    text: str

    def __init__(self, text_string: str):
        self.text = text_string
        self.sentences = []
        self.__parse()

    def __parse(self):
        for sent in sent_tokenize(self.text, 'russian'):
            self.sentences.append(Sentence(sent))

    def __len__(self):
        return len(self.sentences)

    def __iter__(self) -> Sentence:
        for sent in self.sentences:
            yield sent

    @LazyProperty
    def sentence_count(self):
        return len(self)

    @property
    def sent_word_count_average(self):
        return sum(len(sent) for sent in self) / len(self)

    @LazyProperty
    def word_count(self):
        return sum(len(sent) for sent in self)

    @property
    def verb_to_all_ratio(self):
        return sum(
            sent.part_of_speech_count(["VERB", "INFN", "PRTF", "PRTS", "GRND"]) / len(sent) for sent in self if
            len(sent)) / self.sentence_count

    @property
    def noun_to_all_ratio(self):
        return sum(sent.part_of_speech_count(["NOUN"]) / len(sent) for sent in self if len(sent)) / self.sentence_count

    @property
    def ad_to_all_ratio(self):
        return sum(sent.part_of_speech_count(["ADVB", "ADJF", "ADJS"]) / len(sent) for sent in self if
                   len(sent)) / self.sentence_count

    @property
    def sent_syl_average(self):
        return sum(sent.syllable_count / len(sent) for sent in self if len(sent)) / self.sentence_count

    @property
    def word_average_sym_count(self):
        return sum(word.length('sym') / len(sent) for sent in self for word in sent if len(sent)) / self.word_count

    @property
    def word_average_syl_count(self):
        return sum(word.length('syl') / len(sent) for sent in self for word in sent if len(sent)) / self.word_count

    @property
    def exclamative_sent_word_ratio(self):
        return sum(len(sent) for sent in self if sent.is_exclamative) / self.word_count

    @property
    def interrogative_sent_word_ratio(self):
        return sum(len(sent) for sent in self if sent.is_interrogative) / self.word_count

    @property
    def direct_speech_word_ratio(self):
        direct_speech_occurences = []
        for sent in self:
            direct_speech_occurences.extend([Sentence(speech) for speech in direct_speech_re.findall(str(sent))])
        return sum(len(sent) for sent in direct_speech_occurences if len(sent)) / self.word_count
