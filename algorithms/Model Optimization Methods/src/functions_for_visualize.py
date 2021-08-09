import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def visualize(func, title=None, c='r'):
    x = np.arange(-10.0, 10.0, 0.1)
    y = func(x)
    if title == None: title = func.__name__.capitalize().replace('_', ' of ')
    plt.plot(x, y, c, linewidth=5)
    plt.title(title, fontsize=18)
    plt.xlabel('x', fontsize=15);
    plt.ylabel('y', fontsize=15)
    plt.axvline(x=0, c='gray');
    plt.axhline(y=0, c='gray')
    plt.grid(True)
    plt.show()


def visualize_gradient_descent(X, Y,
                               best_w, best_b, errors,
                               title_loss_func='Loss Function',
                               title_first_plot='Test data',
                               ylabel_second_plot='Costs', ):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 7))
    fig.suptitle(title_loss_func, fontsize=29)

    sns.regplot(X, Y, line_kws={"color": "b", "lw": 0, }, ci=100, ax=ax1)
    ax1.set_title(title_first_plot, fontsize=19)
    ax1.plot(
        [X.min(), X.max()],
        [best_w * X.min() + best_b, best_w * X.max() + best_b],
        color='blue',
        linewidth=3,
    )
    ax2.plot(range(1, len(errors) + 1), errors, marker='o')
    ax2.set_title('График ошибок неправильной классификации', fontsize=19)
    ax2.set_xlabel('Эпохи', fontsize=19)
    ax2.set_ylabel(ylabel_second_plot, fontsize=13)
    plt.show()


def visualize_logistic_loss():
    sigmoid = lambda x: 1 / (1 + np.exp(-x))
    first = lambda z: -np.log(sigmoid(z))
    second = lambda z: -np.log(1 - sigmoid(z))
    x = np.arange(-10.0, 10.0, 0.1)
    plt.plot(sigmoid(x), first(x), label='J(w), если y=1', linewidth=3)
    plt.plot(sigmoid(x), second(x), label='J(w), если y=0', c='orange', linewidth=2)
    plt.title('Logistic loss', fontsize=18)
    plt.xlabel('$\phi(z)$', fontsize=13); plt.ylabel('J(w)', fontsize=13)
    plt.legend(loc='best', fontsize=13); plt.grid(True)
    plt.show()


def visualize_dots(X, Y, Z, xlist, ylist, zlist, title='Result'):
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet', edgecolor='none', alpha=0.6)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.plot(xlist, ylist, zlist, 'ro', markersize=10)
    ax.set_title(title, fontsize=20)
