def test_read_file():
    try:
        import pytest
        import numpy as np
        from hrm.heart_rate_monitor import HeartRateMonitor
        from hrm.hrm_errors import EmptyFileError, FileFormatError
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    with pytest.raises(FileNotFoundError):
        test1 = HeartRateMonitor("missing.csv")
    with pytest.raises(EmptyFileError):
        test2 = HeartRateMonitor("tests/basic_test1.csv")
    with pytest.raises(FileFormatError):
        test2 = HeartRateMonitor("tests/basic_test2.csv", num_entries=3)
    with pytest.raises(FileFormatError):
        test3 = HeartRateMonitor("requirements.txt", num_entries=3)
    test4 = HeartRateMonitor("tests/basic_test2.csv")
    ans4 = np.array([[0, 0], [0, 1], [1, 2], [3, 4]])
    assert np.array_equal(test4.data, ans4)
