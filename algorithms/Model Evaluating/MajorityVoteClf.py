import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.externals import six
from sklearn.pipeline import _name_estimators
from sklearn.base import clone


class MajorityVoteClf(BaseEstimator, ClassifierMixin):
    """
    classifiers (array)
        классификаторы для ансамбля
    vote (str) {classlabel, probability}
        classlabel - прогноз основывается на argmax классов
        probability - прогноз основывается на argmax суммы  вероятностей классов
            |> (для откалиброванных классификаторов)
    weights (nd-array), shape= [N-clf]
        назначают важность классификаторам, по умолчанию: равномерные веса
    """

    def __init__(self, classifiers, vote='classlabel', weights=None):
        self.classifiers = classifiers
        self.vote = vote
        self.weights = weights
        self.named_classifiers = {key: value for key, value in _name_estimators(classifiers)}

    def fit(self, X, y):
        """
        Подгоняет классификаторы.
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        y (vector)  целевые значения (0|1)
        :return self
        """
        self.classifiers_ = []
        for clf in self.classifiers:
            fitted_clf = clone(clf).fit(X, y)
            self.classifiers_.append(fitted_clf)
        return self

    def predict(self, X):
        """
        Делает прогноз для X
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        :return y_pred (vector) прогноз (0|1)
        """
        if self.vote == 'probability':
            y_pred = np.argmax(self.predict_proba(X), axis=1)
        else:  # vote - 'classlabel'
            predictions_clf = np.array([clf.predict(X) for clf in self.classifiers_]).T
            # мажоритарное голосование
            y_pred = np.apply_along_axis(lambda x: np.argmax(np.bincount(x, weights=self.weights)),
                                         axis=1, arr=predictions_clf)
        return y_pred

    def predict_proba(self, X):
        """
        Прогноз вероятностей для X
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        :return
            avg_proba (matrix), shape =  [примеры, колличество классификаторов]
                взвешанная усреднённая вероятность для каждого классификатора на образец
        """
        probas = [clf.predict_proba(X) for clf in self.classifiers_]
        avg_proba = np.average(probas, axis=0, weights=self.weights)
        return avg_proba

    def get_params(self, deep=True):
        """
        Возвращает имена параметров классификатора
        Решает ошибку:
            it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' methods."""
        if not deep:
            return super(MajorityVoteClf, self).get_params(deep=False)
        else:
            out = self.named_classifiers.copy()
            for name, step in six.iteritems(self.named_classifiers):
                for key, value in six.iteritems(step.get_params(deep=True)):
                    out[f'{name}__{key}'] = value
            return out
