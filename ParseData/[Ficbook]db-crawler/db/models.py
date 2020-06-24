from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

Base = declarative_base()


class Novel(Base):
    """
    Выполняет следующий SQL запрос:
        CREATE TABLE `novel` (
            `id`	INTEGER NOT NULL,
            `url`	VARCHAR UNIQUE,
            `title`	VARCHAR,
            `author`	VARCHAR,
            `description`	VARCHAR,
            `pairing_and_characters`	VARCHAR,
            `rating`	VARCHAR,
            `size`	VARCHAR,
            `status`	VARCHAR,
            `tags`	VARCHAR,
            `author_notes`	VARCHAR,
            `like_count`	INTEGER,
            `text`	VARCHAR,
            `date_added`	DATE,
            `sentence_count`	INTEGER,
            `sent_word_count_average`	FLOAT,
            `word_count`	INTEGER,
            `verb_to_all_ratio`	FLOAT,
            `noun_to_all_ratio`	FLOAT,
            `ad_to_all_ratio`	FLOAT,
            `sent_syl_average`	FLOAT,
            `word_average_sym_count`	FLOAT,
            `word_average_syl_count`	FLOAT,
            `exclamative_sent_word_ratio`	FLOAT,
            `interrogative_sent_word_ratio`	FLOAT,
            `direct_speech_word_ratio`	FLOAT,
            PRIMARY KEY(`id`)
        );
    """
    __tablename__ = 'novel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    pairing_and_characters = Column(String)
    rating = Column(String)
    size = Column(String)
    status = Column(String)
    tags = Column(String)
    author_notes = Column(String)
    like_count = Column(Integer)
    text = Column(String)
    date_added = Column(Date)

    sentence_count = Column(Integer)
    sent_word_count_average = Column(Float)
    word_count = Column(Integer)
    verb_to_all_ratio = Column(Float)
    noun_to_all_ratio = Column(Float)
    ad_to_all_ratio = Column(Float)
    sent_syl_average = Column(Float)
    word_average_sym_count = Column(Float)
    word_average_syl_count = Column(Float)
    exclamative_sent_word_ratio = Column(Float)
    interrogative_sent_word_ratio = Column(Float)
    direct_speech_word_ratio = Column(Float)
