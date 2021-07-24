"""
Классификатор на основе адаптивного линейного нейрона

Решает задачу бинарной классификации.
    Есть датасет: m образцов, каждый образец — n-мерная точка.
    Для каждого образца мы знаем к какому классу он относится (зелёный или красный).
    Также известно, что датасет является линейно разделимым, т.е. существует n-мерная гиперплоскость такая, что зелёные точки лежат по одну сторону от неё, а красные — по другую.
Разделяющая поверхность задается формулой (x @ w) + b = 0
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class AdalineGD(object):
    """
    eta (float)
         Скорость обучения
    n_iter (int)
         Проходы по обучающимся наборам данных
    random_state (int)
        Начальное значение генератора случайных чисел для инициализации весов
    w_ (nd-array)
         Веса после прогонки
    cost_ (list)
         Сумма квадратичных ошибок, усреднённая по всем обучающим образцам, показывает успешность алгоритма
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
            errors = y - output  # Отклонения расчетных результатов от истинных меток классов
            self.w_[1:] += self.eta * X.T @ errors  # Обновляем веса, вычислив градиент
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        """ Вычисляет общий вход z"""
        return X @ self.w_[1:] + self.w_[0]

    def activation(self, X):
        """ Вычиляет линейную активацию """
        return X

    def predict(self, X):
        """
        Пороговая функция активации f(z) (нужна для смещения весов)
        :return -1|1
        """
        return np.where(self.net_input(X) >= 0.0, 1, -1)


def show_errors(errors):
    """ График ошибок неправильной классификации """
    plt.plot(range(1, len(errors) + 1), errors, marker='o')
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
    plt.xlabel('Petal length [стандартизированный]')
    plt.ylabel('Petal width [стандартизированный]')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

    show_errors(ada.cost_)
