def simple_graph(x, y, x_label=None, y_label=None):
    """
    Graphs given x and y values
    :param x: Values to go on x-axis
    :type x: numpy array
    :param y: Values to go on y-axis
    :type y: numpy array
    :param x_label: Title for x-axis
    :type x_label: string
    :param y_label: Title for y-axis
    :type y_label: string
    :raises ImportError: if necessary import fails

    :return: True if no exception is raised
    :rtype: boolean
    """
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    plt.plot(x, y, 'bo')
    plt.show()
    return True
