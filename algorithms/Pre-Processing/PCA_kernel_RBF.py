from scipy.spatial.distance import pdist, squareform
import numpy as np
import pandas as pd


def PCA_kernel_RBF(X, *, gamma, k_features):
    """
    ядро (гаусово) - радиальная базисная функция

    X (matrix)
            обучающие векторы, shape = [примеры, переменные(d)]
    gamma (float)
            параметр для настройки ядра
    k_features (int)
            количество главных признаков, который будут оставлены
    :return X_pr (matrix)
                Спроецированные данные shape = [примеры, переменные(k)] k>>d
            eigen_vals (vector)
                значения для дообучения
    """
    # попарные квадратичные эвклидовы расстояния (vector)
    pair_sq_dist = pdist(X, 'sqeuclidean')
    matrix_pair_sq_dist = squareform(pair_sq_dist)
    K = np.exp(-gamma * matrix_pair_sq_dist)  # симметричная матрица ядра
    N = K.shape[0]
    one_k = np.ones((N, N)) / N
    K_center = K - one_k @ K - K @ one_k + (one_k @ K) @ one_k  # центрированная матрица ядра
    # Разложение матрицы на вектора и значения
    eigen_vals, eigen_vecs = np.linalg.eigh(K_center)
    eigen_vals, eigen_vecs = eigen_vals[::-1], eigen_vecs[:, ::-1]

    X_pr = np.column_stack([eigen_vecs[:, i] for i in range(k_features)])
    vals = [eigen_vals[i] for i in range(k_features)]
    return X_pr, vals


if __name__ == '__main__':
    df = pd.read_csv('wine.csv')
    X, y = df.drop(['Class label'], axis=1), df[['Class label']]
    print(PCA_kernel_RBF(X, gamma=0.3, k_features=3))
