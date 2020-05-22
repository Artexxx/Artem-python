from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np
import pickle
import sqlite3
import os


def tokenizer(text):
    return text.split()

vect = HashingVectorizer(decode_error='ignore', n_features=2 ** 21,  # n- кол-во признаков
                         preprocessor=None, tokenizer=tokenizer)


def update_model(db_path, model, batch_size=10000):
    """
    Преобучает модель на данных из базы.
    - желательно проверить достоверность данных перед переобучением
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * from review_db')

    results = c.fetchmany(batch_size)
    while results:
        data = np.array(results)
        X = data[:, 0]
        y = data[:, 1].astype(int)

        classes = np.array([0, 1])
        X_train = vect.transform(X)
        model.partial_fit(X_train, y, classes=classes)
        results = c.fetchmany(batch_size)

    conn.close()
    return model


clf = pickle.load(open(os.path.join('pkl_objects', 'classifier.pkl'), 'rb'))
clf = update_model(db_path='reviews.sqlite', model=clf, batch_size=10000)

# pickle.dump(clf, open(os.path.join(cur_dir,
#             'pkl_objects', 'classifier.pkl'), 'wb')
#             , protocol=4)
