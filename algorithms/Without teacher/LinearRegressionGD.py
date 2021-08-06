import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionGD(object):
    """
    eta (float)
         скорость обучения
    n_iter (int)
         проходы по обучающимся наборам данных
    w_ (nd-array)
         Веса после прогонки
    cost_ (list)
        Сумма квадратичных ошибок, усреднённая по всем обучающим образцам, показывает успешность алгоритма
    """

    def __init__(self, eta=0.001, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        y (vector)  целевые значения (1|-1)
        :return self
        """

        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)  # отклонения расчетных результатов от истинных меток классов
            self.w_[1:] += self.eta * X.T @ errors  # обновляем веса, вычислив градиент
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        """  Вычисляет общий вход """
        return X @ self.w_[1:] + self.w_[0]


    def predict(self, X):
        """ Возвращает метку класса после единичного шага"""
        return self.net_input(X)


def show_errors(errors):
    """ График ошибок неправильной классификации """
    plt.plot(range(1, len(errors) + 1), errors, marker='o')
    plt.xlabel('Эпохи')
    plt.ylabel('Сумма квадратичных ошибок')
    plt.show()


if __name__ == '__main__':
    import pandas as pd

    df = pd.read_csv('../Linear Classifier/fruits.csv')
    X = df.iloc[:, [0, 1]].values
    y = df.iloc[:, 2].values

    lr = LinearRegressionGD()
    lr.fit(X, y)
    show_errors(lr.cost_)