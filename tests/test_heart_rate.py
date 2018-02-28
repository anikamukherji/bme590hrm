def test_heart_rate():
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test1 = HeartRateMonitor("test_data/test_data1.csv")
    test1.find_heart_rate()
    assert int(test1.mean_hr_bpm) == int(35*(60/test1.duration))
