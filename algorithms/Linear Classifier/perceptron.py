""" perceptron.py -  классификатор на основе пепрсептрона.

Простейший блок нейронных сетей — перцептрон (perceptron).
Изначально перцептрон был создан как очень отдаленная модель биологического нейрона.
Как и у биологического нейрона, у него есть вход и выход, а также поток «сигналов», идущих от входа к выходу
Разделяющая поверхность задается формулой (x @ w) + b = 0
"""
import matplotlib.pyplot as plt
import numpy as np


class Perceptron(object):
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
    errors_ ( list )
        Количество ошибочных классификаций в каждой эпохе.
    """

    def __init__(self, eta=0.01, random_state=1, n_iter=50):
        self.eta = eta
        self.random_state = random_state
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        X (matrix) обучающие векторы, shape = [n_samples, n_features]
        y (vector)  целевые значения (1|-1),  shape = [n_samples]
        :return self
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0, scale=0.01, size=X.shape[1])
        self.bias_ = 0
        self.errors_ = []

        for _ in range(self.n_iter):
            error = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.bias_ += update
                error += int(update != 0)
            self.errors_.append(error)
        return self

    def net_input(self, X):
        """ Вычисляет общий вход z"""
        return X @ self.w_ + self.bias_

    def predict(self, X):
        """
        Пороговая функция активации f(z) (нужна для смещения весов)
        :return -1|1
        """
        return np.where(self.net_input(X) > 0, 1, -1)


def make_plote(df):
    """График рассеивания"""
    pears = df[:, 2] == 1  # [true|false, ... ,]
    apples = np.logical_not(pears)
    plt.scatter(df[apples][:, 0], df[apples][:, 1], color="red")
    plt.scatter(df[pears][:, 0], df[pears][:, 1], color="yellow")
    plt.xlabel("Yellowness")
    plt.ylabel("Symmetry")
    plt.show()


def show_errors(errors):
    """График ошибок неправильной классификации """
    plt.plot(range(1, len(errors) + 1), errors, marker='o')
    plt.xlabel('Эпохи')
    plt.ylabel('Кол-во обновлений')
    plt.show()


if __name__ == '__main__':
    df = np.loadtxt("src/fruits.csv", delimiter=",")
    y_raw = df[:, 2]
    y = np.where(y_raw == 1, -1, 1)
    X = df[:, [0, 1]]

    ppn = Perceptron(n_iter=20).fit(X, y)

    make_plote(df)
    show_errors(ppn.errors_)
    from src.plot_decision_regions import plot_decision_regions
    plot_decision_regions(X, y, classifier=ppn)
    plt.xlabel('Yellowness')
    plt.ylabel('Symmetry')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
