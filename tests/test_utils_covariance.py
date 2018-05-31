# test_utils_covariance
# author: Jungtaek Kim (jtkim@postech.ac.kr)
# last updated: May 30, 2018

import pytest
import numpy as np

from bayeso.utils import utils_covariance


def test_get_hyps():
    with pytest.raises(AssertionError) as error:
        utils_covariance.get_hyps(1.2, 2.1)
    with pytest.raises(AssertionError) as error:
        utils_covariance.get_hyps(1.2, 2)
    with pytest.raises(AssertionError) as error:
        utils_covariance.get_hyps('se', 2.1)
    with pytest.raises(ValueError) as error:
        utils_covariance.get_hyps('abc', 2)
    
    cur_hyps =  utils_covariance.get_hyps('se', 2)
    assert cur_hyps['noise'] == 0.1
    assert cur_hyps['signal'] == 1.0
    assert (cur_hyps['lengthscales'] == np.array([1.0, 1.0])).all()

def test_convert_hyps():
    with pytest.raises(AssertionError) as error:
        utils_covariance.convert_hyps(1.2, 2.1)
    with pytest.raises(AssertionError) as error:
        utils_covariance.convert_hyps(1.2, dict())
    with pytest.raises(AssertionError) as error:
        utils_covariance.convert_hyps('se', 2.1)
    with pytest.raises(AssertionError) as error:
        utils_covariance.convert_hyps('abc', 2.1)

    cur_hyps = {'noise': 0.1, 'signal': 1.0, 'lengthscales': np.array([1.0, 1.0])}
    converted_hyps = utils_covariance.convert_hyps('se', cur_hyps)
    assert converted_hyps[0] == cur_hyps['noise']
    assert converted_hyps[1] == cur_hyps['signal']
    assert (converted_hyps[2:] == cur_hyps['lengthscales']).all()
