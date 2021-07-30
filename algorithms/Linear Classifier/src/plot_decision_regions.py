import numpy as np
import matplotlib.pyplot as plt


def plot_decision_regions(X, y, classifier, resolution=0.02, test_idx=None):
    """Строит график областей решения"""
    from matplotlib.colors import ListedColormap

    markers = ('o', '^', 's', 'x', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # Выводим поверхность решения
    x1_min, x1_max = X[:, 0].min(), X[:, 0].max()  # минимум и максимум для 1 признака
    x2_min, x2_max = X[:, 1].min(), X[:, 1].max()  # минимум и максимум для 2 признака
    # Матрица координат
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    # Идентифицируем метки классов и преобразуем в матрицу с размерностями как у xx1 и xx2
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    # Контурный график
    plt.contourf(xx1, xx2, Z, alpha=0.2, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # Для вывода объектов
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.9,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')
    # Для выделения образцов из испытательного набора
    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0],
                    X_test[:, 1],
                    linewidth=1,
                    marker='o',
                    edgecolor='black',
                    s=100,
                    color='',
                    label='Test data', )
