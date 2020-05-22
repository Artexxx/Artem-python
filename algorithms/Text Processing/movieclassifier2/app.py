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


data = dict()


@app.route('/')
def main():
    data['reviewresponse'] = 'None'
    return render_template('index.html', data=data)


@app.route('/results', methods=['POST'])
def resolve():
    review = request.form.get('review')
    data['reviewresponse'], proba = classify(preprocessor(review))

    return render_template('index.html', data=data, probability=round(proba * 100, 2))


if __name__ == '__main__':
    app.run(debug=True)
