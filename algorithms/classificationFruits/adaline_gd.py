""" классификатор на основе адаптивного линейного нейрона """
import numpy as np
import matplotlib.pyplot as plt


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
        это сумма квадратичных ошибок, показывающие успешность алгоритма
    """

    def __init__(self, eta=0.001, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, x, y):
        """
        X (matrix) обучающие векторы, shape = [примеры, переменные]
        y (vector)  целевые значения (1|-1)
        :return self
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + x.shape[1])

        self.cost_ = []
        for i in range(self.n_iter):
            net_input = self.net_input(x)
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


def plot_decision_regions(X, y, classifier, resolution=0.02):
    """график областей решения"""
    from matplotlib.colors import ListedColormap
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # выводим поверхность решения
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1  # находим минимум и максимум для 1 признака
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1  # находим минимум и максимум для 2 признака
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))  # получаем матрицу координат

    # идентифицируем метки классов и преобразуем в матрицу с размерностями как у xx1 и xx2
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    # рисуем контурный график
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    """ для вывода объектов """
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.2,
                    c=colors[idx - 1],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')
    plt.show()


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
    plt.xlabel('Эпохи')
    plt.ylabel('Сумма квадратичных ошибок')
    plt.show()


df = np.loadtxt("fruits.csv", delimiter=",")
y_raw = df[:, 2]
y = np.where(y_raw == 1, -1, 1)
X = df[:, [0, 1]]

# Для улучшения надо стандартизировать
X_std = np.copy(X)
X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()


ada = AdalineGD(eta=0.001, n_iter=155).fit(X, y)

plot_decision_regions(X_std, y, classifier=ada)
plt.title('Adaline - Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

showErrors(ada.cost_)
