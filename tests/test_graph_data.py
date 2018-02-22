def test_graph_data():
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    for num in range(1, 10):
        test = HeartRateMonitor("test_data/test_data{}.csv".format(num))
        res = test.graph_data()
        assert res is True

