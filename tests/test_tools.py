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


def test_simple_graph():
    try:
        import pytest
        import numpy as np
        from tools.graphing_tools import simple_graph
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    except RuntimeError as e:
        print("Necessary import failed: {}".format(e))
        return
    test1 = [np.array([-1, 0, 1, 2, 3, 4]), np.array([-1, 0, 1, 2, 3, 4])]
    result1 = simple_graph(test1[0], test1[1], show=False)
    result2 = simple_graph(test1[0], test1[1], x_label="x-axis",
                           y_label="y-axis", show=False)
    assert result1 is True
    assert result2 is True


def test_return_column():
    try:
        import pytest
        import numpy as np
        from tools.hrm_tools import return_column
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test = np.matrix([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(TypeError):
        return_column(test, 'a')
    with pytest.raises(TypeError):
        return_column(test, 3.0)
    with pytest.raises(TypeError):
        return_column(test, [9])
    with pytest.raises(TypeError):
        return_column(test, {9: 1})
    with pytest.raises(TypeError):
        return_column(4, 1)
    with pytest.raises(TypeError):
        return_column([4], 1)
    with pytest.raises(TypeError):
        return_column({9: 1}, 1)
    index_error = return_column(test, 5)
    assert index_error is None
    t0 = return_column(test, 0)
    assert np.array_equal(t0, np.array([[1, 3, 5]]))
    t1 = return_column(test, 1)
    assert np.array_equal(t1, np.array([[2, 4, 6]]))


def test_autocorr_freq():
    try:
        import pytest
        import numpy as np
        from tools.hrm_tools import autocorr_freq
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test1 = np.array([0, 0, 1, 0, 0, 1, 0, 0, 1, 0])
    freq1 = autocorr_freq(test1, len(test1))
    test2 = np.array([0, 0.1, 0.2, 1, 0.05, 0.1, 1, 0, 0.12, 1, 0])
    freq2 = autocorr_freq(test2, len(test2))
    assert int(freq1) == 3
    assert int(freq2) == 3


def test_find_max():
    try:
        import pytest
        import numpy as np
        from tools.hrm_tools import find_max
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    type_errs = [np.array([[1, 2], [1, 2]]), np.array(['a']), [3, 4],
                 'a', {1: 3}, np.array([])]
    for ex in type_errs:
        with pytest.raises(TypeError):
            find_max(ex)
    tests = [np.array([1, 2, 3]), np.array([-1, 4, -9]), np.array([0])]
    answers = [3.0, 4.0, 0.0]
    for t, a in zip(tests, answers):
        assert find_max(t) == a


def test_find_min():
    try:
        import pytest
        import numpy as np
        from tools.hrm_tools import find_min
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    type_errs = [np.array([[1, 2], [1, 2]]), np.array(['a']), [3, 4],
                 'a', {1: 3}, np.array([])]
    for ex in type_errs:
        with pytest.raises(TypeError):
            find_min(ex)
    tests = [np.array([1, 2, 3]), np.array([-1, 4, -9]), np.array([0])]
    answers = [1.0, -9.0, 0.0]
    for t, a in zip(tests, answers):
        assert find_min(t) == a
