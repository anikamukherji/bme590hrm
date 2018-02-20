def test_HeartRateMonitor_init():
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test1 = HeartRateMonitor("tests/basic_test2.csv", data=[1])
    test2 = HeartRateMonitor("tests/basic_test2.csv", data=[2])
    test3 = HeartRateMonitor("tests/basic_test2.csv", 6,
                             [0], 1, (2, 3), 4, 5, [6])
    assert test1.num_entries == 2
    assert test1.data == [1]
    assert test1.mean_hr_bpm is None
    assert test1.voltage_extremes is None
    assert test1.duration is None
    assert test1.num_beats is None
    assert test1.beats is None
    assert test2.num_entries is 2
    assert test2.data == [2]
    assert test2.mean_hr_bpm is None
    assert test2.voltage_extremes is None
    assert test2.duration is None
    assert test2.num_beats is None
    assert test2.beats is None
    assert test3.num_entries == 6
    assert test3.data == [0]
    assert test3.mean_hr_bpm == 1
    assert test3.voltage_extremes == (2, 3)
    assert test3.duration == 4
    assert test3.num_beats == 5
    assert test3.beats == [6]
