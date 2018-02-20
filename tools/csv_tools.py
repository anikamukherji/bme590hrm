def prepare_csv_line(row):
    """
    Takes in row from csv reader and returns a numpy
    array of floats
    :param row: Row from csv reader
    :type row: list

    :return: formatted numpy array of floats
    :rtype: numpy array
    :return: None if error is raised
    :rtype: NoneType
    """
    try:
        import numpy as np
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return None
    try:
        stripped_row = [x.strip() for x in row]
    except AttributeError as e:
        print("Value could not be stripped: {}".format(e))
        return None
    try:
        float_row = [float(x) for x in stripped_row]
    except TypeError as e:
        print("Value could not be cast to float: {}".format(e))
        return None
    except ValueError as e:
        print("Value could not be cast to float: {}".format(e))
        return None
    data_array = np.array(float_row)
    return data_array
