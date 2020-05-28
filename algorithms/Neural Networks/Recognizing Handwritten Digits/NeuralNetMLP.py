"""
Классификатор на основе многослойного перцсептрона (нейронка прямого распространения)
https://youtu.be/t-Jpm1axBko ~~ теория про нейронку
"""
import numpy as np
import sys


class NeuralNetMLP(object):
    """
    n_hidden (int) =30
        количесво элементов в скрытом слое
    l2 (float) = 0
        значение для регуляризации l2 (отсутствует)
    max_iter (int) = 100
        количесто итераций
    shuffle (bool) = True
        данные тасуются каждую итерацию (предотвращает циклы)
    eta (float) = 0.001
        скорость обучения
    minibatch_size (int) = 1
        количество обучающихся образцов в мини-пакетах
    random_state (int) = None
        начальное значение для тасовки и инициализации весов

    self.eval_ (dict)
            показатели издержек, правильность при обучение и испытание на каждой итерации
    """

    def __init__(self, n_hidden=30, l2=0, max_iter=100, eta=.001, shuffle=True, minibatch_size=1, random_state=None):
        self.random = np.random.RandomState(random_state)
        self.minibatch_size = minibatch_size
        self.n_hidden = n_hidden
        self.max_iter = max_iter
        self.shuffle = shuffle
        self.eta = eta
        self.l2 = l2

    def fit(self, X_train, y_train, X_valid, y_valid):
        """
        X_train   shape=(n_samples, n_features)
            - входной слой
        y_train   shape=(n_samples)
            - целевые значения (0-9)
        X_valid   shape=(n_samples, n_features)
            - признаки для проверки во время обучения
        y_valid   shape=(n_samples)
            - целевые значения для проверки во время обучения (0-9)
        :return self
        """
        n_output = len(np.unique(y_train))
        n_features = X_train.shape[1]
        # ~~~~~~~~~~~~~~~~~~~~~~~~| Инициализация весов |~~~~~~~~~~~~~~~~~~~~~~~~~
        # 1. входной слой ~~> скрытый слой
        self.b_h = np.zeros(self.n_hidden)
        self.w_h = self.random.normal(loc=0, scale=.1, size=(n_features, self.n_hidden))

        # 2. скрытый слой ~~> выходной слой
        self.b_out = np.zeros(n_output)
        self.w_out = self.random.normal(loc=0, scale=.1, size=(self.n_hidden, n_output))

        self.eval_ = {'cost': [], 'train_acc': [], 'valid_acc': []}
        y_train_enc = self._onehot(y_train, n_output)

        for i in range(self.max_iter):
            indices = np.arange(X_train.shape[0])
            if self.shuffle: self.random.shuffle(indices)

            # ~~~~~~~~~~~~~~~~~~~~~~~~| Итерация мини-пакетами |~~~~~~~~~~~~~~~~~~~~~~~~~
            for start_idx in range(0, indices.shape[0] - self.minibatch_size + 1, self.minibatch_size):
                batch_idx = indices[start_idx:start_idx + self.minibatch_size]
                # прямое распространение (forward propagation)
                z_h, a_h, z_out, a_out = self._forward(X_train[batch_idx])

                # обратное распространение (back propagation)
                # [n_samples, n_classlabels]
                sigma_out = a_out - y_train_enc[batch_idx]  # ошибка сети
                # [n_samples, n_hidden]
                sigmoid_derivative_h = a_h * (1 - a_h)  # производная

                # [n_samples, n_classlabels] dot [n_classlabels, n_hidden]
                # ~~> [n_samples, n_hidden]
                sigma_h = (np.dot(sigma_out, self.w_out.T) * sigmoid_derivative_h)

                # перенос ошибки на скрытый слой
                # [n_features, n_samples] dot [n_samples, n_hidden]
                # ~~> [n_features, n_hidden]
                grad_w_h = np.dot(X_train[batch_idx].T, sigma_h)
                grad_b_h = np.sum(sigma_h, axis=0)

                # перенос ошибки на входной слой
                # [n_hidden, n_samples] dot [n_samples, n_classlabels]
                # ~~> [n_hidden, n_classlabels]
                grad_w_out = np.dot(a_h.T, sigma_out)
                grad_b_out = np.sum(sigma_out, axis=0)

                # регуляризация и обновление весов
                delta_w_h = (grad_w_h + self.l2 * self.w_h)
                delta_b_h = grad_b_h  # bias is not regularized
                self.w_h -= self.eta * delta_w_h
                self.b_h -= self.eta * delta_b_h

                delta_w_out = (grad_w_out + self.l2 * self.w_out)
                delta_b_out = grad_b_out  # bias is not regularized
                self.w_out -= self.eta * delta_w_out
                self.b_out -= self.eta * delta_b_out

            # ~~~~~~~~~~~~~~~~~~~~~~~~| Оценка модели после итерации |~~~~~~~~~~~~~~~~~~~~~~~~~
            z_h, a_h, z_out, a_out = self._forward(X_train)

            cost = self._compute_cost(y_enc=y_train_enc, output=a_out)

            y_train_pred = self.predict(X_train)
            y_valid_pred = self.predict(X_valid)

            train_acc = np.sum(y_train == y_train_pred).astype(np.float) / X_train.shape[0]
            valid_acc = np.sum(y_valid == y_valid_pred).astype(np.float) / X_valid.shape[0]

            self.eval_['cost'].append(cost)
            self.eval_['train_acc'].append(train_acc)
            self.eval_['valid_acc'].append(valid_acc)

            sys.stderr.write('\r%0*d/%d | Cost: %.2f '
                             '| Train/Valid Acc: %.2f%%/%.2f%% ' %
                             (len(str(self.max_iter)), i + 1, self.max_iter, cost,
                              train_acc * 100, valid_acc * 100))
            sys.stderr.flush()
        return self

    def _onehot(self, y_train, n_classes):
        """
        Разбивает вектор, содержащего числовые категориальные данные, на множество вектороа в зависимости от количества классов
            - Каждый новый вектор содержит 0 или 1
        y_train shape=(n_samples)
        :return onehot shape=(n_samples, n_labels)
        """
        onehot = np.zeros((n_classes, y_train.shape[0]))
        for idx, val in enumerate(y_train.astype(int)):
            onehot[val, idx] = 1.
        return onehot.T

    def _forward(self, X):
        """Вычисляет шаг прямого распространения (forward propagation)"""
        # 1. общий вход скрытого слоя
        # [n_samples, n_features] dot [n_features, n_hidden] ~~> [n_samples, n_hidden]
        z_h = (X @ self.w_h) + self.b_h

        # 2. активация скрытого слоя
        a_h = self._sigmoid(z_h)

        # 3. общий вход выходного слоя
        # [n_samples, n_hidden] dot [n_hidden, n_classlabels] ~~> [n_samples, n_classlabels]
        z_out = (a_h @ self.w_out) + self.b_out

        # 4. активация выходного слоя
        a_out = self._sigmoid(z_out)
        return z_h, a_h, z_out, a_out

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))

    def _compute_cost(self, y_enc, output):
        """ Вычисляет издержки, для оценки эффективности, в основе логистическая функция
        y_enc   shape = (n_samples, n_labels)
            метки классов в унитарном коде (one-hot encoded)
        output  shape = (n_samples, n_output_units)
            активация выходного слоя (forward propagation)

        :return cost (float)
            регуляризованные издержки
        """
        L2_term = (self.l2 * (np.sum(self.w_h ** 2) + np.sum(self.w_out ** 2)))

        term1 = -y_enc * (np.log(output))
        term2 = (1 - y_enc) * np.log(1 - output)
        cost = np.sum(term1 - term2) + L2_term
        return cost

    def predict(self, X):
        """предсказывает метки классов
        X shape = [n_samples, n_features]
            - входной слой с первоначальными признаками
        :return y_pred shape = [n_samples]
            - предсказанные метки классов (0-9)
        """
        z_h, a_h, z_out, a_out = self._forward(X)
        y_pred = np.argmax(z_out, axis=1)
        return y_pred
