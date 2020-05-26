""" perceptronApple.py --  классификатор на основе пепрсептрона """
import matplotlib.pyplot as plt
import numpy as np


class Perceptron(object):
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
    errors ( list )
        количество ошибочных классификаций
    """

    def __init__(self, eta=0.01, random_state=1, n_iter=50):
        self.eta = eta
        self.random_state = random_state
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        y (vector)  целевые значения (1|-1)
        :return self
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []
        for i in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[0] += update
                self.w_[1:] += update * xi
                errors += int(update != 0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """  вычисляет общий вход """
        return X @ self.w_[1:] + self.w_[0]

    def predict(self, X):
        """ :return -1|1 (нужно для смещения весов) """
        return np.where(self.net_input(X) > 0, 1, -1)


def makePlote(df):
    """график рассеивания"""
    pears = df[:, 2] == 1  # [true|false, ... ,]
    apples = np.logical_not(pears)
    plt.scatter(df[apples][:, 0], df[apples][:, 1], color="red")
    plt.scatter(df[pears][:, 0], df[pears][:, 1], color="yellow")
    plt.xlabel("желтизна")
    plt.ylabel("симметричность")
    plt.show()


def showErrors(errors):
    """ график ошибки неправильной классификации """
    plt.plot(range(1, len(errors) + 1),
             errors, marker='o')
    plt.xlabel('эпохи')
    plt.ylabel('кол-во обновлений')
    plt.show()


if __name__ == '__main__':
    df = np.loadtxt("fruits.csv", delimiter=",")
    y_raw = df[:, 2]
    y = np.where(y_raw == 1, -1, 1)
    X = df[:, [0, 1]]

    ppn = Perceptron(n_iter=20).fit(X, y)

    makePlote(df)
    showErrors(ppn.errors_)

    from plot_decision_regions import plot_decision_regions

    plot_decision_regions(X, y, classifier=ppn)
    plt.xlabel('желтизна')
    plt.ylabel('симметричность')
    plt.show()
