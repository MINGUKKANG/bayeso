# example_gp_mml_large_y
# author: Jungtaek Kim (jtkim@postech.ac.kr)
# last updated: July 12, 2018

import numpy as np
import os

from bayeso import gp
from bayeso.utils import utils_plotting


PATH_SAVE = '../figures/gp/'

def main():
    X_train = np.array([
        [-3.0],
        [-2.0],
        [-1.0],
        [2.0],
        [1.2],
        [1.1],
    ])
    Y_train = np.cos(X_train) * 100000.0
    num_test = 200
    X_test = np.linspace(-3, 3, num_test)
    X_test = X_test.reshape((num_test, 1))
    Y_test_truth = np.cos(X_test) * 100000.0
    mu, sigma = gp.predict_optimized(X_train, Y_train, X_test, is_fixed_noise=True)
    utils_plotting.plot_gp(X_train, Y_train, X_test, mu, sigma, Y_test_truth, PATH_SAVE, 'test_optimized_large_y')


if __name__ == '__main__':
    if not os.path.isdir(PATH_SAVE):
        os.makedirs(PATH_SAVE)
    main()

