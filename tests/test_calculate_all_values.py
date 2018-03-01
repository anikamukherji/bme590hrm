def test_calculate_all_values():
    """
    Runs the calculate_all_values function on every
    CSV file in the test_data directory to identity any
    exceptions raised
    """
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    for num in range(1, 33):
        test = HeartRateMonitor("test_data/test_data{}.csv".format(num))
        assert test.calculate_all_values() is True
        assert test.num_beats == test.beats.size
