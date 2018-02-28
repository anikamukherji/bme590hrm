class HeartRateMonitor:
    """
    Class for a HeartRateMonitor object = takes in ECG data
    and analyzes  it
    Attributes:
        filename (string): filepath to ECG file
        num_entries (int): number of entries per line of ECG csv file
        data (numpy array): ECG data
        mean_hr_bpm (int): estimated average heart rate over a
                           user-specified number of minutes (default = 10 min)
        voltage_extremes (tuple): tuple containing minimum and maximum lead
                                  voltages
        duration (float): time duration of the ECG strip
        num_beats (int): number of detected beats in the strip
        beats (numpy array): numpy array of times when a beat occurred
    """

    def __init__(self, filename, num_entries=2, data=None, mean_hr_bpm=None,
                 voltage_extremes=None, duration=None, num_beats=None,
                 beats=None):
        """
        Initializes instance of class HeartRateMonitor
        :param filename: filename/path for ECG data
        :type filename: string
        :param num_entries: number of entries to expect per line in csv
        :type num_entries: int
        :param data: 2d numpy array containing time/voltages
        :type data: numpy array
        :param mean_hr_bpm: estimated average heart rate over a
                            user-specified number of minutes (default = 10 min)
        :type mean_hr_bpm: int
        :param voltage_extremes: tuple containing min & max lead voltages
        :type voltage_extremes: tuple
        :param duration: time duration of ECG strip
        :type duration: float
        :param num_beats: number of detected beats
        :type num_beats: int
        :param beats: numpy array of times when a beat occurred
        :type beats: numpy array
        """
        self.filename = filename
        self.num_entries = num_entries
        if not data:
            data = self.read_file(filename)
        self.data = data
        self.mean_hr_bpm = mean_hr_bpm
        self.voltage_extremes = voltage_extremes
        self.duration = duration
        self.num_beats = num_beats
        self.beats = beats

    def read_file(self, filename):
        """
        Reads file and returns 2d numpy array containing
        the data from the file

        :param filename: filename/path to ECG data .csv file
        :type filename: string
        :raises: IOError if file does not exist
        :raises: EmptyFileError if file is empty

        :return: 2d array of data from file
        :rtype: numpy array
        """
        try:
            import csv
            import logging
            import numpy as np
            from hrm.hrm_errors import EmptyFileError, FileFormatError
            from tools.csv_tools import prepare_csv_line
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        logging.basicConfig(filename='read_file.log', filemode='w',
                            level=logging.DEBUG)
        # first entry will always be all zeros
        data = np.array([np.zeros(self.num_entries)])
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            logging.warning("File does not exist")
            raise FileNotFoundError()
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 0:
                logging.debug("Found blank row in file")
                continue
            if len(row) != self.num_entries:
                logging.warning("Expected {} items per row in file but "
                                "found {}".format(self.num_entries, len(row)))
                raise FileFormatError()
            new_row = prepare_csv_line(row)
            try:
                if new_row.any():
                    data = np.append(data, [new_row], axis=0)
                else:
                    logging.warning("File contains non-numerical data")
                    raise FileFormatError()
            except AttributeError:
                break
        f.close()
        if len(data) == 1:
            logging.warning("File provided is empty")
            raise EmptyFileError()
        logging.info("Returning 2d numpy array with "
                     " {} values".format(len(data)))
        return data

    def graph_data(self, show=True):
        """
        Graphs ECG data
        :param show: whether the plot should appear
        :type show: boolean

        :return: True if no exceptions are cast
        :rtype: boolean
        """
        try:
            import numpy as np
            import matplotlib.pyplot as plt
            from tools.graphing_tools import simple_graph
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        x = self.return_times()
        y = self.return_voltages()
        simple_graph(x, y, x_label="Time", y_label="Voltage", show=show)
        return True

    def return_voltages(self, index=1):
        """
        Returns numpy array of recorded voltages
        :param index: index of voltage in self.data
        :type index: int

        :return: 2d numpy array of voltages
        :rtype: numpy array
        """
        try:
            from tools.hrm_tools import return_column
            import numpy as np
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        data_mat = np.matrix(self.data)
        return return_column(data_mat, index)

    def return_times(self, index=0):
        """
        Returns numpy array of times voltages were recorded
        :param index: index of time in self.data
        :type index: int

        :return: 2d numpy array of times
        :rtype: numpy array
        """
        try:
            from tools.hrm_tools import return_column
            import numpy as np
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        data_mat = np.matrix(self.data)
        return return_column(data_mat, index)

    def find_heart_rate(self):
        """
        Finds heart rate of HeartRateMonitor object data

        :return: heart rate
        :rtype: int
        """
        try:
            import numpy as np
            import matplotlib.pyplot as plt
            from tools.hrm_tools import autocorr_freq
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        voltages = self.return_voltages()
        times = self.return_times()
        v = voltages[0]
        t = times[0]
        last_sample = t[-1]
        # sampling frequency
        fs = round(t.size/last_sample)
        freq = autocorr_freq(v, fs)
        return freq
