import numpy as np
import pandas as pd


def get_real_data():
    df = pd.read_csv('src/states.csv')
    x, y = df.hs_grad, df.poverty
    scaled_x = (x - x.mean()) / x.std()
    scaled_y = (y - y.mean()) / y.std()
    return scaled_x.values, scaled_y.values


def update_weights_SSE(w, b, X, Y, learning_rate):
    w_deriv = 0
    b_deriv = 0

    N = len(X)
    for i in range(N - 1):
        # Вычисление частных производных
        w_deriv += (- 2 * X[i]) * (- w * X[i] - b + Y[i])
        b_deriv += 2 * w * X[i] + 2 * b - 2 * Y[i]

    w -= learning_rate * (w_deriv / float(N))
    b -= learning_rate * (b_deriv / float(N))
    return w, b


def L2(yhat, y):
    """
    Arguments:
        yhat - predicted labels
        y - true labels
    """
    loss = np.sum(np.square(y - yhat))
    return loss
