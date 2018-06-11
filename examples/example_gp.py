import numpy as np

from bayeso import gp
from bayeso.utils import utils_common
from bayeso.utils import utils_plot


def main():
    X_train = np.array([
        [-3],
        [-1],
        [1],
        [2],
    ])
    Y_train = np.cos(X_train) + np.random.randn(X_train.shape[0], 1) * 0.2
    num_test = 200
    X_test = np.linspace(-3, 3, num_test)
    X_test = X_test.reshape((num_test, 1))
    Y_test_truth = np.cos(X_test)
    hyps = {
        'signal': 0.5,
        'lengthscales': 0.5,
        'noise': 0.02,
    }
    mu, sigma = gp.predict_test(X_train, Y_train, X_test, hyps)
    utils_plot.plot_gp(X_train, Y_train, X_test, mu, sigma, Y_test_truth, path_save='../results/gp/', str_postfix='test')

if __name__ == '__main__':
    main()

