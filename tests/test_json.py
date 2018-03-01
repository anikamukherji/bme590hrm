def test_write_json():
    try:
        import pytest
        from hrm.heart_rate_monitor import HeartRateMonitor
        from datetime import date
        import json
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    test = HeartRateMonitor("tests/basic_test2.csv", mean_hr_bpm=6,
                            data=[0], voltage_extremes=(2, 3),
                            duration=4, num_beats=5, beats=[6], 
                            units='minute')
    test.write_json()
    data = json.load(open('tests/basic_test2.json'))
    values = {
              "mean_hr_bpm": test.mean_hr_bpm,
              "duration": test.duration,
              "units": test.units,
              "voltage_extremes": list(test.voltage_extremes),
              "num_beats": test.num_beats,
              "beats": test.beats
              }
    assert data == values


def test_return_values_dict():
    try:
        import pytest
        from hrm.heart_rate_monitor import HeartRateMonitor
        from datetime import date
    except ImportError as e:
        print("necessary import failed: {}".format(e))
        return
    test = HeartRateMonitor("tests/basic_test2.csv", mean_hr_bpm=6,
                            data=[0], voltage_extremes=(2, 3),
                            duration=4, num_beats=5, beats=[6], 
                            units='minute')
    ret = test.return_values_dict()
    values = {
              "mean_hr_bpm": test.mean_hr_bpm,
              "duration": test.duration,
              "units": test.units,
              "voltage_extremes": test.voltage_extremes,
              "num_beats": test.num_beats,
              "beats": test.beats
             }
    assert ret == values
