from itertools import combinations
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


class SBS():
    """
    k_features (int)
            количество главных признаков, который будут оставлены
    estimator (class)
            обучающаяся модель

    subsets_ [best combinations] * (w_count - k_features)
             массив из лучших по результату комбинаций
    scores_ [best score] * (w_count - k_features)
             массив из лучших по результатов комбинаций
    k_score (float)
            результат предсказания при количестве признаков k_features
    """

    def __init__(self, estimator, k_features, test_size=0.3):
        self.estimator = estimator
        self.k_features = k_features
        self.test_size = test_size

    def fit(self, X, y):
        """
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        y (vector)  целевые значения (0|1|2)
        :return self
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=42, stratify=y)
        w_count = X_train.shape[1]  # количество признаков
        self.w_indxes_ = tuple(range(w_count))  # индексы признаков
        self.subsets_ = [self.w_indxes_]
        score = self._calc_score(X_train, X_test, y_train, y_test, self.w_indxes_)
        self.scores_ = [score]

        while w_count > self.k_features:
            scores = []
            subsets = []
            for combination in combinations(self.w_indxes_, r=w_count - 1):
                score = self._calc_score(X_train, X_test, y_train, y_test, combination)
                subsets.append(combination)
                scores.append(score)

            best = np.argmax(scores)  # индекс максимального результата
            self.w_indxes_ = subsets[best]
            self.scores_.append(scores[best])
            self.subsets_.append(subsets[best])
            w_count -= 1

        self.k_score = self.scores_[-1]
        return self

    def _calc_score(self, X_train, X_test, y_train, y_test, w_indxes):
        """ Счиает точность предсказания на определённых признаках"""
        self.estimator.fit(X_train[:, w_indxes], y_train)
        return self.estimator.score(X_test[:, w_indxes], y_test)


if __name__ == '__main__':
    df = pd.read_csv('wine.csv')
    X, y = df.drop(['Class label'], axis=1), df[['Class label']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    from sklearn.preprocessing import StandardScaler

    stdsc = StandardScaler()
    X_train_std = stdsc.fit_transform(X_train)

    from sklearn.neighbors import KNeighborsClassifier

    knn = KNeighborsClassifier(n_neighbors=5)

    sbs = SBS(knn, k_features=2)
    sbs.fit(X_train_std, y_train.values.ravel())
    print(*sbs.subsets_, sep='\n')