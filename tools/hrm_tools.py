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

    :return: frequency
    :rtype: int
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
    last_half = ret[ret.size//2:]
    corr = last_half[last_half.size//2:]
    d = np.diff(last_half)
    start = find(d > 0)[0]
    peak = np.argmax(corr[start:]) + start
    # sampling frequency
    freq = fs/peak
    return freq
