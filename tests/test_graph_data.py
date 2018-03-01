def test_graph_data():
    """
    Tests graph_data function in the HeartRateMonitor class
    """
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    for num in range(1, 4):
        test = HeartRateMonitor("test_data/test_data{}.csv".format(num))
        res = test.graph_data(show=False)
        assert res is True


def test_return_voltages():
    """
    Tests return_voltages function in the HeartRateMonitor class
    """
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test = HeartRateMonitor("tests/basic_test2.csv")
    res = test.return_voltages()
    assert np.array_equal(res, np.array([1.0, 2.0, 4.0]))
    pass


def test_return_times():
    """
    Tests return_times function in the HeartRateMonitor class
    """
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test = HeartRateMonitor("tests/basic_test2.csv")
    res = test.return_times()
    assert np.array_equal(res, np.array([0.0, 1.0, 3.0]))
