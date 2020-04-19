""" perceptronApple.py --  классификатор на основе пепрсептрона """
import matplotlib.pyplot as plt
import numpy as np


class Perceptron(object):
    """
    eta    | float |: скорость обучения
    n_iter | int |: проходы по обучающим выборкам
    random_state | int |: начальное значение для рандомных весов
    w_ | ld-array | веса после прогонки
    errors | list | количество ошибочных классификаций
    """

    def __init__(self, eta=0.01, random_state=1, n_iter=50):
        self.eta = eta
        self.random_state = random_state
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        X | matrix | .shape = (примеры, переменные)
        y | vector | целевые значения (1|-1)
        :return Object
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
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

    def predict(self, X):
        """ :return -1|1 (нужно для смещения весов) """
        pr = X @ self.w_[1:] + self.w_[0]
        return np.where(pr > 0, 1, -1)


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


def plot_decision_regions(X, y, classifier, resolution=0.02):
    """график областей решения"""
    from matplotlib.colors import ListedColormap
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min(), X[:, 0].max()
    x2_min, x2_max = X[:, 1].min(), X[:, 1].max()
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    """ для вывода объектов """
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx - 1],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')
    plt.show()


df = np.loadtxt("fruits.csv", delimiter=",")
y = df[:, 2]
y = np.where(y == 1, -1, 1)
X = df[:, [0, 1]]

ppn = Perceptron(n_iter=20)
ppn.fit(X, y)

makePlote(df)
showErrors(ppn.errors_)
plot_decision_regions(X, y, classifier=ppn)
