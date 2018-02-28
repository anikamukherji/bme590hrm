def test_heart_rate():
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test = HeartRateMonitor("test_data/test_data1.csv")
    freq = test.find_heart_rate()
    pass
