import requests
from page_parsing import get_readlinks, fetch_catalogue_page, parse_fic
from db.session_manager import session_scope
from db.models import Novel
from data_utils.metrics import Text
from sqlalchemy import and_
import time


def main(page_range=(0, 30_000)):
    for i in range(*page_range):
        print(f"Page {i}/{page_range[1]}")
        fanfic_addresses = get_readlinks(fetch_catalogue_page(i))
        with session_scope() as sess:
            already_exist_obj = sess.query(Novel.url).filter(Novel.url.in_([a['url'] for a in fanfic_addresses])).all()
            already_exist_lst = [o.url for o in already_exist_obj]
        for idx, fic_address in enumerate([fa for fa in fanfic_addresses if fa['url'] not in already_exist_lst]):
            fic_page = requests.get(fic_address['url'])
            result = parse_fic(fic_page.content.decode())
            result.update(fic_address)
            with session_scope() as sess:
                sess.add(Novel(**result))
                print(f"Text {idx}")
            time.sleep(.5)


def get_text(idx: int):
    with session_scope() as session:
        print(session.query(Novel.id).first())


def calculate_metrics():
    with session_scope() as query_session:
        novels = query_session.query(Novel).filter(and_(Novel.text.isnot(None),
                                                        Novel.rating.isnot(None),
                                                        Novel.word_count.is_(None))).all()
        for novel in novels:
            with session_scope() as session:
                text = Text(novel.text)
                metrics = {
                    Novel.word_count: text.word_count,
                    Novel.ad_to_all_ratio: text.ad_to_all_ratio,
                    Novel.direct_speech_word_ratio: text.direct_speech_word_ratio,
                    Novel.exclamative_sent_word_ratio: text.exclamative_sent_word_ratio,
                    Novel.interrogative_sent_word_ratio: text.interrogative_sent_word_ratio,
                    Novel.word_average_sym_count: text.word_average_sym_count,
                    Novel.word_average_syl_count: text.word_average_syl_count,
                    Novel.noun_to_all_ratio: text.noun_to_all_ratio,
                    Novel.verb_to_all_ratio: text.verb_to_all_ratio,
                    Novel.sent_syl_average: text.sent_syl_average,
                    Novel.sentence_count: text.sentence_count,
                    Novel.sent_word_count_average: text.sent_word_count_average
                }
                session.query(Novel).filter(Novel.id == novel.id).update(metrics)
                print(novel.title)


if __name__ == '__main__':
    calculate_metrics()
    #main((6, 30_000))
