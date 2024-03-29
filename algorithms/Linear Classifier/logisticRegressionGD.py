""" классификатор на основе логистической регрессии, использующий градиентный спуск """
import numpy as np
import matplotlib.pyplot as plt


class LogisticRegressionGD(object):
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
        Логистические издержки, показывающие успешность алгоритма
    """

    def __init__(self, eta=0.001, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        y (vector)  целевые значения (0|1)
        :return self
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.05, size=1 + X.shape[1])

        self.cost_ = []
        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = y - output  # отклонения расчетных результатов от истинных меток классов
            self.w_[1:] += self.eta * X.T.dot(errors)  # обновляем веса, вычислив градиент
            self.w_[0] += self.eta * errors.sum()
            cost = -y.dot(np.log(output)) - ((1 - y).dot(np.log(1 - output)))
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        """  вычисляет общий вход """
        return X @ self.w_[1:] + self.w_[0]

    def activation(self, z):
        """ вычиляет логистическкую сигмоидальную активацию """
        # clip() интервал [5,10] --> все значения <5 превращаются в 5
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))

    def predict(self, X):
        """ возращает метку класса после единичного шага"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)


def showErrors(errors):
    """ график ошибки неправильной классификации """
    plt.plot(range(1, len(errors) + 1),
             errors, marker='o')
    plt.xlabel('Эпохи')
    plt.ylabel('Логистические ошибки')
    plt.show()


if __name__ == '__main__':
    import pandas as pd

    df = pd.read_csv('fruits.csv')
    X = df.iloc[:, [0, 1]].values
    y = df.iloc[:, 2].values

    lrgd = LogisticRegressionGD(eta=0.05, n_iter=20, random_state=42)
    lrgd.fit(X, y)

    from plot_decision_regions import plot_decision_regions

    plot_decision_regions(X, y, classifier=lrgd)
    plt.title('Logistic Regression Classifier using gradient descent')
    plt.xlabel('yellowness')
    plt.ylabel('symmetry')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

    showErrors(lrgd.cost_)
