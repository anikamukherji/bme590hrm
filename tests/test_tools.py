def test_prepare_csv_line():
    try:
        import pytest
        import numpy as np
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
