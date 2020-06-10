import numpy as np
import matplotlib.pyplot as plt
import h5py


def sigmoid(Z):
    """
    Реализует активацию сигмоидaльную активацию.

    Z -- выход линейного слоя, любой формы

    returns:
       A - параметр после активации, имеющий ту же форму, что и Z
       cache - (dict), содержащий "A"; хранится для эффективного вычисления обратного прохода
    """

    A = 1. / (1. + np.exp(-Z))
    cache = Z

    return A, cache


def relu(Z):
    """
    Реализует функцию RELU.

    Z -- выход линейного слоя, любой формы

    returns:
        A - параметр после активации, имеющий ту же форму, что и Z
        cache - (dict), содержащий "A"; хранится для эффективного вычисления обратного прохода
    """
    A = np.maximum(0, Z)

    assert (A.shape == Z.shape)
    cache = Z
    return A, cache


def relu_backward(dA, cache):
    """
    Реализует обратное распространение для одной RELU еденицы.

    dA -- градиент после активации, любой формы
    cache -- 'Z', где мы храним для эффективного вычисления обратного распространения

    Returns: dZ -- Градиент стоимости по отношению к Z
    """

    Z = cache
    dZ = np.array(dA, copy=True)  # просто преобразуем dz в правильный объект.

    # Когда z <= 0, вы также должны установить dz в 0.
    dZ[Z <= 0] = 0

    assert (dZ.shape == Z.shape)
    return dZ


def sigmoid_backward(dA, cache):
    """
    Реализует обратное распространение для одной SIGMOID еденицы.

    dA -- градиент после активации, любой формы
    cache -- 'Z', где мы храним для эффективного вычисления обратного распространения

    Returns: dZ -- Градиент стоимости по отношению к Z
    """

    Z = cache

    s = 1. / (1 + np.exp(-Z))
    dZ = dA * s * (1. - s)

    assert (dZ.shape == Z.shape)
    return dZ


def load_data():
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


def initialize_parameters(n_x, n_h, n_y):
    """
    n_x -- size of the input layer
    n_h -- size of the hidden layer
    n_y -- size of the output layer

    returns: parameters (dict) содержащий параметры:
                    W1 -- weight (matrix) shape (n_h, n_x)
                    b1 -- bias (vector)   shape (n_h, 1)
                    W2 -- weight (matrix) shape (n_y, n_h)
                    b2 -- bias (vector)   shape (n_y, 1)
    """

    np.random.seed(1)
    W1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.zeros((n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros((n_y, 1))

    assert (W1.shape == (n_h, n_x))
    assert (b1.shape == (n_h, 1))
    assert (W2.shape == (n_y, n_h))
    assert (b2.shape == (n_y, 1))
    parameters = {"W1": W1, "b1": b1,
                  "W2": W2, "b2": b2}
    return parameters


def initialize_parameters_deep(layer_dims):
    """
    layer_dims (list) cодержит размеры каждого слоя в нашей сети

    returns: parameters (dict) содержащий параметры "W1", "b1", ..., "WL", "bL":
                    Wl -- weight (matrix) shape (layer_dims[l], layer_dims[l-1])
                    bl -- bias (vector)   shape (layer_dims[l], 1)
    """
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)  # количество слоев в сети

    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) / \
                                   np.sqrt(layer_dims[l - 1])  # *0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))

        assert (parameters['W' + str(l)].shape == (layer_dims[l], layer_dims[l - 1]))
        assert (parameters['b' + str(l)].shape == (layer_dims[l], 1))
    return parameters


def linear_forward(A, W, b):
    """
    линейная часть forward propagation.

    A -- активации с предыдущего слоя (или input data): (size of previous layer, number of examples)
    W -- weights (matrix): numpy array shape (size of current layer, size of previous layer)
    b -- bias (vector), numpy array    shape (size of the current layer, 1)

    returns:
        Z -- входной сигнал функции активации, также называемый параметром предварительной активации
        cache (dict) содержащий "A", " W " и "b"; хранится для эффективного вычисления backward
    """
    Z = W @ A + b

    assert (Z.shape == (W.shape[0], A.shape[1]))
    cache = (A, W, b)
    return Z, cache


def linear_activation_forward(A_prev, W, b, activation):
    """
    forward propagation для слоя LINEAR->ACTIVATION

    A_prev -- активации с предыдущего слоя (или input data): (size of previous layer, number of examples)
    W -- weights matrix: numpy array  shape (size of current layer, size of previous layer)
    b -- bias vector, numpy array     shape (size of the current layer, 1)
    activation -- {"sigmoid"|"relu"} активация, которая будет использоваться в этом слое

    returns:
        A  -- вывод функции активации, также называемой значением после активации
        cache -- (dict) содержащий "linear_cache" и " activation_cache";
            сохраненный для эффективного вычисления backward
    """

    # Inputs: "A_prev, W, b". Outputs: "A, activation_cache".
    if activation == "sigmoid":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = sigmoid(Z)

    elif activation == "relu":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = relu(Z)

    assert (A.shape == (W.shape[0], A_prev.shape[1]))
    cache = (linear_cache, activation_cache)
    return A, cache


def L_model_forward(X, parameters):
    """
    Прямое распространение для [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID

    X -- (matrix) shape (input size, number of examples)
    parameters -- вывод initialize_parameters_deep()

    returns:
        AL -- последнее значение post-activation
        caches (list) - каждый cache из linear_relu_forward() (there are L-1 of them, indexed from 0 to L-2)
               cache из linear_sigmoid_forward() (there is one, indexed L-1)
    """

    caches = []
    A = X
    L = len(parameters) // 2  # количество слоев в нейронной сети

    # [LINEAR -> RELU]*(L-1)
    for l in range(1, L):
        A_prev = A
        A, cache = linear_activation_forward(A_prev, parameters['W' + str(l)], parameters['b' + str(l)],
                                             activation="relu")
        caches.append(cache)

    # LINEAR -> SIGMOID
    AL, cache = linear_activation_forward(A, parameters['W' + str(L)], parameters['b' + str(L)], activation="sigmoid")
    caches.append(cache)

    assert (AL.shape == (1, X.shape[1]))
    return AL, caches


def compute_cost(AL, Y):
    """
    AL -- вероятностный вектор, соответствующий вашим прогнозам по меткам, shape (1, number of examples)
    Y -- (vector) {0:non-cat, 1: cat}, shape (1, number of examples)

    returns: cost - cross-entropy cost
    """

    m = Y.shape[1]

    # потери от aL и Y.
    # TODO cost = -1 / m * np.sum(Y * np.log(AL) + (1 - Y) * np.log(1 - AL), axis=1, keepdims=True)
    cost = (1. / m) * (-np.dot(Y, np.log(AL).T) - np.dot(1 - Y, np.log(1 - AL).T))

    cost = np.squeeze(cost)
    assert (cost.shape == ())
    return cost


def linear_backward(dZ, cache):
    """
    Линейная часть обратного распространения для одного слоя (слой l)

    dZ -- градиент стоимости по отношению к линейному выходу (текущего слоя l)
    cache -- кортеж значений (A_prev, W, b), поступающих из прямого распространения в текущем слое

    returns:
        dA_prev - градиент стоимости по отношению к активации (предыдущего слоя l-1), такой же формы, как и A_prev
        db - градиент стоимости по отношению к b (текущий слой l), такой же формы, как и b
    """
    A_prev, W, b = cache
    m = A_prev.shape[1]

    dW = 1. / m * np.dot(dZ, A_prev.T)
    db = 1. / m * np.sum(dZ, axis=1, keepdims=True)
    dA_prev = np.dot(W.T, dZ)

    assert (dA_prev.shape == A_prev.shape)
    assert (dW.shape == W.shape)
    assert (db.shape == b.shape)
    return dA_prev, dW, db


def linear_activation_backward(dA, cache, activation):
    """
    метод обратного распространения ошибки для слоя LINEAR->ACTIVATION

    dA -- post-activation градиент для текущего слоя l
    cache -- кортеж значений (linear_cache, activation_cache) мы храним для эффективного вычисления обратного распространения
    activation -- {"sigmoid", "relu"} активация, которая будет использоваться в этом слое

    returns:
        dA_prev -- градиент стоимости по отношению к активации (предыдущего слоя l-1), такой же формы, как и A_prev
        dW -- градиент стоимости по отношению к активации (предыдущего слоя l-1), такой же формы, как и A_prev
        db -- градиент стоимости по отношению к b (текущий слой l), такой же формы, как и b
    """
    linear_cache, activation_cache = cache

    if activation == "relu":
        dZ = relu_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)

    elif activation == "sigmoid":
        dZ = sigmoid_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)

    return dA_prev, dW, db


def L_model_backward(AL, Y, caches):
    """
    backward propagation для [LINEAR->RELU] * (L-1) -> LINEAR -> SIGMOID

    AL - вероятностный вектор, выходной сигнал прямого распространения (L_model_forward())
    Y  - vector целевых переменных {0 - non-cat, 1-cat}
    caches -- список кэшов, содержащих:
        каждый кэш linear_activation_forward() с "relu" (это кэш[l], for l in range(L-1) т.e l = 0...L-2)
        кэш linear_activation_forward () с "sigmoid" (это кэш[L-1])

    returns: grads (dict) с градиентами
             grads["dA" + str(l)] = ...
             grads["dW" + str(l)] = ...
             grads["db" + str(l)] = ...
    """
    grads = {}
    L = len(caches)  # количество слоев
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)  # после этой линии Y имеет ту же форму, что и AL

    # Initializing backpropagation
    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))

    '''
    Lth layer (SIGMOID -> LINEAR) gradients. 
     Inputs: "AL, Y, caches". 
     Outputs: "grads["dAL"], grads["dWL"], grads["dbL"]
    '''
    current_cache = caches[L - 1]
    (grads["dA" + str(L)],
     grads["dW" + str(L)],
     grads["db" + str(L)]) = linear_activation_backward(dAL, current_cache, activation="sigmoid")

    for l in reversed(range(L - 1)):
        '''
        lth layer: (RELU -> LINEAR) gradients.
         Inputs: "grads["dA" + str(l + 2)], caches".
         Outputs: "grads["dA" + str(l + 1)] , grads["dW" + str(l + 1)] , grads["db" + str(l + 1)] 
        '''
        current_cache = caches[l]
        (grads["dA" + str(l + 1)],
         grads["dW" + str(l + 1)],
         grads["db" + str(l + 1)]) = \
            linear_activation_backward(grads["dA" + str(l + 2)], current_cache, activation="relu")
    return grads


def update_parameters(parameters, grads, learning_rate):
    """
    Обновление параметров с помощью градиентного спуска

    parameters - (dict), содержащий параметры
    grads - (dict), содержащий градиенты, (вывод L_model_backward)

    returns: parameters - (dict), содержащий обновленные параметры
                  parameters["W" + str(l)] = ...
                  parameters["b" + str(l)] = ...
    """

    L = len(parameters) // 2  # количество слоев в нейронной сети

    for l in range(L):
        parameters["W" + str(l + 1)] = parameters["W" + str(l + 1)] - learning_rate * grads["dW" + str(l + 1)]
        parameters["b" + str(l + 1)] = parameters["b" + str(l + 1)] - learning_rate * grads["db" + str(l + 1)]
    return parameters


def predict(X, y, parameters):
    """
    Эта функция используется для прогнозирования результатов работы L-слойной нейронной сети.

    X -- набор данных примеров, по которым будет прогноз
    parameters -- Параметры обучаемой модели

    Returns:
        p - прогнозы для данного набора данных X
    """

    m = X.shape[1]
    n = len(parameters) // 2  # количество слоев в нейронной сети
    p = np.zeros((1, m), dtype=np.int)

    # Forward propagation
    probas, caches=L_model_forward(X, parameters)

    # convert probas ~~> 0/1 predictions
    for i in range(0, probas.shape[1]):
        if probas[0, i] > 0.5:
            p[0, i] = 1
        else:
            p[0, i] = 0

    # print("predictions: " + str(p))
    # print("true labels: " + str(y))
    print(f"Accuracy: {np.sum((p == y) / m):.2%} ")
    return p


def print_mislabeled_images(classes, X, y, p):
    """
    рисует изображения, предсказания по которым ложны
    X -- dataset
    y -- true labels
    p -- predictions
    """
    a = p + y
    mislabeled_indices = np.asarray(np.where(a == 1))
    plt.rcParams['figure.figsize'] = (40.0, 40.0)  # plots size
    num_images = len(mislabeled_indices[0])
    for i in range(num_images):
        index = mislabeled_indices[1][i]

        plt.subplot(2, num_images, i + 1)
        plt.imshow(X[:, index].reshape(64, 64, 3), interpolation='nearest')
        plt.axis('off')
        plt.title("Prediction: " + classes[int(p[0, index])].decode("utf-8") +
                  " \n Class: " + classes[y[0, index]].decode("utf-8"))
