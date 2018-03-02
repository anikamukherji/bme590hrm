def test_heart_rate():
    """
    Tests the find_heart_rate function in the HeartRateMonitor class
    """
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


def test_find_heart_rates_for_interval():
    """
    Tests the find_heart_rates_for_interval function
    in the HeartRateMonitor class
    """
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test1 = HeartRateMonitor("test_data/test_data1.csv")
    ret1 = test1.find_heart_rates_for_interval(1)
    assert len(ret1) == 1
    ret2 = test1.find_heart_rates_for_interval(0.4)
    assert len(ret2) == 2


def test_find_beats():
    """
    Tests the find_beats function in the HeartRateMonitor class
    """
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test1 = HeartRateMonitor("test_data/test_data1.csv")
    test1.find_beats()


def test_num_beats():
    """
    Tests the find_num_beats function in the HeartRateMonitor class
    """
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    beats = np.array([1, 2, 3, 4])
    test1 = HeartRateMonitor("test_data/test_data1.csv", beats=beats)
    test1.find_num_beats()
    assert test1.num_beats == 4
    test2 = HeartRateMonitor("test_data/test_data1.csv")
    test2.find_beats()
    test2.find_num_beats()
    assert test2.num_beats == 35
