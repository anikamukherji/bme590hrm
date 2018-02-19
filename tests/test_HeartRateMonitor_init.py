def test_HeartRateMonitor_init():
    try:
        import pytest
        import numpy as np
        import hrm.heart_rate_monitor import HeartRateMonitor
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
    test1 = HeartRateMonitor("")
    test2 = HeartRateMonitor("my_file")
    test3 = HeartRateMonitor("my_file", [], 1, (2, 3), 4, 5, [6])
    assert test1.data == None
    assert test1.mean_hr_bpm == None
    assert test1.voltage_extremes == None
    assert test1.duration == None
    assert test1.num_beats == None
    assert test1.beats == None
    assert test2.data == None
    assert test2.mean_hr_bpm == None
    assert test2.voltage_extremes == None
    assert test2.duration == None
    assert test2.num_beats == None
    assert test2.beats == None
    assert test3.data == []
    assert test3.mean_hr_bpm == 1
    assert test3.voltage_extremes == (2, 3)
    assert test3.duration == 4
    assert test3.num_beats == 5
    assert test3.beats == [6]
    pass
