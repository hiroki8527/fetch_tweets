import sys
sys.path.append('../script')
import common

def test_set_limit_with_given_limit():
    limit = 6
    default = 30
    assert common.set_limit(limit, default) == 6

def test_set_limit_without_given_limit():
    limit = None
    default = 30
    assert common.set_limit(limit, default) == 30
