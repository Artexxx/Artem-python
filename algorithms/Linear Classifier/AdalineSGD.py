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


class AdalineSGD(object):
    """
    Params:
    ----------
    eta (float) = 0.01
         Скорость обучения между 0.0 и 1.0
    n_iter (int) = 50
         Количесто проходов по обучающему набору данных
    random_state (int) = 1
        Начальное значение генератора случайных чисел для инициализации весов
    shuffle (bool)
        Данные будут перемешиваться каждую эпоху

    Attributes:
    -----------
    w_ (nd-array)
        Веса после подгонки, shape = [n_features]
    costs_ ( list )
        Сумма квадратичных ошибок, усреднённая по всем обучающим образцам, показывает успешность алгоритма
    """

    def __init__(self, eta=0.001, n_iter=20, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.shuffle = shuffle
        self.random_state = random_state
        self.w_initialized = True

    def fit(self, X, y):
        """
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        y (vector)  целевые значения (1|-1)
        :return self
        """
        self._initialize_weigth(X.shape[1])
        self.costs_ = []

        for _ in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            total_cost = .0
            for xi, target in zip(X, y):
                total_cost += self._update_weights(xi, target)
            avg_cost = total_cost / len(y)
            self.costs_.append(avg_cost)
        return self

    def partial_fit(self, X, y):
        """ Подгонка под тренировочные данные без повторной инициализации весов"""
        if not self.w_initialized:
            self._initialize_weigth(X.shape[1])
        if len(y.ravel()) > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)
        return self

    def _initialize_weigth(self, len_features):
        """ Нужно для инициализации весов небольшими рандомными числами """
        self.rgen = np.random.RandomState(self.random_state)
        self.w_ = self.rgen.normal(loc=0.0, scale=0.01, size=1 + len_features)
        self.w_initialized = True

    def _shuffle(self, X, y):
        """ Перемешивает обучающие данные"""
        r = self.rgen.permutation(len(y))
        return X[r], y[r]

    def _update_weights(self, xi, target):
        """ Обновляет веса и возращает меру успешности алгоритма"""
        output = self.activation(self.net_input(xi))
        error = target - output
        self.w_[0] += self.eta * error
        self.w_[1:] += self.eta * xi.dot(error)
        cost = (error ** 2) / 2
        return cost

    def net_input(self, X):
        """ Вычисляет общий вход z"""
        return X @ self.w_[1:] + self.w_[0]

    def activation(self, X):
        """ Вычиляет линейную активацию f(z)"""
        return X

    def predict(self, X):
        """
        Возвращает предсказанную метку класса
        :return -1|1
        """
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)


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

    ada = AdalineSGD(eta=0.001, n_iter=15)
    ada.fit(X_std, y)

    # Обновить модель на индивидуальных образцах
    ada.partial_fit(X_std[0, :], y[0])

    show_errors(ada.costs_)
    from src.plot_decision_regions import plot_decision_regions

    plot_decision_regions(X_std, y, classifier=ada)
    plt.title('Adaline (Стохастический градиентный спуск)')
    plt.xlabel('Длина чашелистика [стандартизованная]')
    plt.ylabel('Длина лепестка [стандартизованная]')

    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
