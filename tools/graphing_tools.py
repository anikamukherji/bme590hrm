def simple_graph(x, y, x_label=None, y_label=None, show=True):
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
    :param show: if graph should pop-up
    :type show: boolean

    :return: True if no exception is raised
    :rtype: boolean
    """
    try:
        import matplotlib
        # if graph is not showing
        # comment out the line below
        matplotlib.use('Agg')
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    if x_label:
        plt.xlabel(str(x_label))
    if y_label:
        plt.ylabel(str(y_label))
    plt.plot(x, y, 'bo')
    if show:
        plt.show()
    return True
