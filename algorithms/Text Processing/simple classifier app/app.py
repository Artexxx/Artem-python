from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np
import sqlite3
import pickle
import re
import os

app = Flask(__name__)

# Подготовка классификатора
clf = pickle.load(open(os.path.join('pkl_objects', 'classifier.pkl'), 'rb'))


def tokenizer(text):
    return text.split()


vect = HashingVectorizer(decode_error='ignore', n_features=2 ** 21,  # n- кол-во признаков
                         preprocessor=None, tokenizer=tokenizer)


def preprocessor(raw_text):
    """
    Очищает текст перед записью в базу и обучением.
    1. поиск эмоций
    2. удаление посторонних знаков и приведение к нижнему регистру + эмоции
    """
    # cleantext = BeautifulSoup(raw_text, "lxml").text
    # cleantext = re.sub('<[^>]*>', '', raw_text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', raw_text)
    text = (re.sub('[\W]+', ' ', raw_text.lower()) +
            ' '.join(emoticons).replace('-', ''))
    return text


def classify(document):
    """
    Делает предсказание по содержимому документа.
    :returns  {'negative'/'positive'}, proba (float)
    """
    label = {0: 'negative', 1: 'positive'}
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba


def train(document, y):
    X = vect.transform([document])
    clf.partial_fit(X, [y])


def sqlite_entry(path, document, y):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("INSERT INTO review_db (review, sentiment, date)" \
              " VALUES (?, ?, DATETIME('now'))", (document, y))
    conn.commit()
    conn.close()
# Конец подготовки классификатора

class ReviewForm(Form):  #
    moviereview = TextAreaField('', [validators.DataRequired(), validators.length(min=20)])


@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('review_form.html', form=form)


@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = preprocessor(request.form['moviereview'])
        y, proba = classify(review)
        return render_template('results.html',
                               content=review,
                               prediction=y,
                               probability=round(proba * 100, 2))
    return render_template('review_form.html', form=form)


@app.route('/thanks', methods=['POST'])
def feedback():
    feedback = request.form['feedback_button']
    review = request.form['review']
    prediction = request.form['prediction']

    inv_label = {'negative': 0, 'positive': 1}
    y = inv_label[prediction]
    if feedback == 'Incorrect':
        y = int(not (y))
    train(review, y)
    sqlite_entry('reviews.sqlite', review, y)
    return render_template('thanks.html')


if __name__ == '__main__':
    app.run(debug=True)
