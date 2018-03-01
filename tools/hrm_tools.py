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
    try:
        ret = matrix[:, index]
    except IndexError:
        print("Index given is out of bounds")
        return None
    except AttributeError:
        print("Incorrect type given to matrix: {}".format(type(matrix)))
        raise TypeError()
    flat_mat = ret.flatten()
    return np.array(flat_mat)


def autocorr_freq(signal, fs):
    """
    Estimates frequency of periodic signal
    using autocorrelation
    Inspiration: https://gist.github.com/endolith/255291/
    71cafad1820118a190a3752388350f1c97acd6de

    :param signal: signal to be analyzed
    :type signal: 1-d numpy array
    :param fs: sampling frequency
    :type fs: float

    :return: frequency
    :rtype: float
    """
    try:
        import numpy as np
        from matplotlib.mlab import find
        from scipy.signal import fftconvolve
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    ret = fftconvolve(signal, signal[::-1], mode='full')
    # get rid of negative lags
    corr = ret[ret.size//2:]
    d = np.diff(corr, axis=0)
    start = find(d > 0)[0]
    peak = np.argmax(corr[start:]) + start
    steps_per_peak = fs/peak
    return steps_per_peak


def find_max(array):
    """
    Finds max value of a given numpy array

    :param array: array filled with some numerical values
    :type array: 1-d numpy array

    :return: max value
    :rtype: float
    """
    try:
        import numpy as np
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    try:
        if array.ndim != 1 or array.size == 0:
            raise TypeError()
    except AttributeError as e:
        print("Wrong type passed in: {}".format(e))
        raise TypeError()
    try:
        float_arr = np.array([float(i) for i in array])
    except TypeError as e:
        print("Wrong type passed in: {}".format(e))
        raise TypeError()
    except ValueError as e:
        print("Wrong type passed in: {}".format(e))
        raise TypeError()
    return np.amax(float_arr)


def find_min(array):
    """
    Finds max value of a given numpy array

    :param array: array filled with some numerical values
    :type array: 1-d numpy array

    :return: max value
    :rtype: float
    """
    try:
        import numpy as np
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    try:
        if array.ndim != 1 or array.size == 0:
            raise TypeError()
    except AttributeError as e:
        print("Wrong type passed in: {}".format(e))
        raise TypeError()
    try:
        float_arr = np.array([float(i) for i in array])
    except TypeError as e:
        print("Wrong type passed in: {}".format(e))
        raise TypeError()
    except ValueError as e:
        print("Wrong type passed in: {}".format(e))
        raise TypeError()
    return np.amin(float_arr)
