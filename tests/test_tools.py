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
    with pytest.raises(TypeError):
        return_column(np.array([1]), 1)
    index_error = return_column(test, 5)
    assert index_error is None
    t0 = return_column(test, 0)
    assert np.array_equal(t0, np.array([[1, 3, 5]]))
    t1 = return_column(test, 1)
    assert np.array_equal(t1, np.array([[2, 4, 6]]))
