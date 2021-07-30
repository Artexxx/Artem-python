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
    Params:
    ----------
    eta (float) = 0.01
         Скорость обучения между 0.0 и 1.0
    n_iter (int) = 50
         Количесто проходов по обучающему набору данных
    random_state (int) = 1
        Начальное значение генератора случайных чисел для инициализации весов

    Attributes:
    -----------
    w_ (nd-array)
        Веса после подгонки, shape = [n_features]
    bias_ (float)
        Смещение.
    costs_ ( list )
        Сумма квадратичных ошибок, усреднённая по всем обучающим образцам, показывает успешность алгоритма
    """

    def __init__(self, eta=0.001, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """
        X (matrix) обучающие векторы, shape = [n_samples, n_features]
        y (vector)  целевые значения (1|-1),  shape = [n_samples]
        :return self
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.bias_ = 0
        self.costs_ = []

        for _ in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = y - output  # Отклонения расчетных результатов от истинных меток классов
            self.w_ += self.eta * X.T @ errors  # Обновляем веса, вычислив градиент
            self.bias_ += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2
            self.costs_.append(cost)
        return self

    def net_input(self, X):
        """ Вычисляет общий вход z"""
        return X @ self.w_ + self.bias_

    def activation(self, X):
        """ Вычиляет линейную активацию f(z)"""
        return X

    def predict(self, X):
        """
        Возвращает предсказанную метку класса
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
    df = pd.read_csv('src/iris.csv')
    X = df.iloc[0:100, [2, 3]].values
    y_raw = df.iloc[0:100, 4].values
    y = np.where(y_raw == 'Iris-setosa', -1, 1)

    # Для обучения  надо стандартизировать
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

    ada = AdalineGD(eta=0.001, n_iter=23)
    ada.fit(X_std, y)

    from src.plot_decision_regions import plot_decision_regions
    plot_decision_regions(X_std, y, classifier=ada)
    plt.title('Adaline (Градиентный спуск)')
    plt.xlabel('Длина чашелистика [стандартизованная]')
    plt.ylabel('Длина лепестка [стандартизованная]')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

    show_errors(ada.costs_)
