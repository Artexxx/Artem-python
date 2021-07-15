""" Классификатор на основе адаптивного линейного нейрона """
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class AdalineGD(object):
    """
    eta (float)
         скорость обучения
    n_iter (int)
         проходы по обучающимся наборам данных
    random_state (int)
         начадьное значение генератора случайных чисел
         для инициализации случайными весами
    w_ (ld-array)
         Веса после прогонки
    cost_ (list)
        сумма квадратичных ошибок, показывающие успешность алгоритма
    """

    def __init__(self, eta=0.001, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        y (vector)  целевые значения (1|-1)
        :return self
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

        self.cost_ = []
        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = y - output  # отклонения расчетных результатов от истинных меток классов
            self.w_[1:] += self.eta * X.T @ errors  # обновляем веса, вычислив градиент
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        """  вычисляет общий вход """
        return X @ self.w_[1:] + self.w_[0]

    def activation(self, X):
        """ вычиляет линейную активацию """
        return X

    def predict(self, X):
        """ возращает метку класса после единичного шага"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)


def showErrors(errors):
    """ график ошибки неправильной классификации """
    plt.plot(range(1, len(errors) + 1),
             errors, marker='o')
    plt.xlabel('Эпохи')
    plt.ylabel('Сумма квадратичных ошибок')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('iris.csv')
    X = df.iloc[0:100, [2, 3]].values
    y_raw = df.iloc[0:100, 4].values
    y = np.where(y_raw == 'Iris-setosa', -1, 1)

    # Для обучения  надо стандартизировать
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

    ada = AdalineGD(eta=0.001, n_iter=23)
    ada.fit(X_std, y)

    from plot_decision_regions import plot_decision_regions
    plot_decision_regions(X_std, y, classifier=ada)
    plt.title('Adaline - градиентный спуск')
    plt.xlabel('petal length [стандартизированный]')
    plt.ylabel('petal width [стандартизированный]')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

    showErrors(ada.cost_)
