def return_column(matrix, index):
    """
    Returns numpy array of some column
    :param matrix: numpy matrix to take col from
    :type index: numpy matrix
    :param index: index of desired column
    :type index: int

    :return: 1d numpy array of voltages
    :rtype: numpy array
    :return: None if exception is raised
    :rtype: NoneType
    """
    try:
        import numpy as np
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    if type(index) is not int:
        print("Incorrect type given to index: {}".format(type(index)))
        raise TypeError()
    if type(matrix) is not type(np.matrix([0])):
        print("Incorrect type given to matrix: {}".format(type(matrix)))
        raise TypeError()
    try:
        ret = matrix[:, index]
    except IndexError:
        print("Index given is out of bounds")
        return None
    flat_mat = ret.flatten()
    return np.array(flat_mat)
