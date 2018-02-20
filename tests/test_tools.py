def test_prepare_csv_line():
    try:
        import pytest
        import numpy as np
        from tools.csv_tools import prepare_csv_line
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    assert prepare_csv_line(['a', 'b', 'c']) is None
    assert prepare_csv_line(['abc', 'bcd', 'cef']) is None
    assert prepare_csv_line([True, False]) is None
    assert prepare_csv_line([[1, 1], [2, 1]]) is None
    assert prepare_csv_line([{1: 1}, {2: 1}]) is None
    tests = [['1 ', ' 2 ', '3'], ['8.9', ' 10.5']]
    answers = [np.array([1.0, 2.0, 3.0]), np.array([8.9, 10.5])]
    for tst, ans in zip(tests, answers):
        assert np.array_equal(prepare_csv_line(tst), ans)
