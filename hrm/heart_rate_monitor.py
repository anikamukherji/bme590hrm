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
        self._check_data()
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
            if new_row.any():
                data = np.append(data, [new_row], axis=0)
            else:
                logging.warning("File contains non-numerical data")
                raise FileFormatError()
        f.close()
        if len(data) == 1:
            logging.warning("File provided is empty")
            raise EmptyFileError()
        logging.info("Returning 2d numpy array with "
                     " {} values".format(len(data)))
        return data

    def _check_data(self):
        """
        Ensures that data passed into HeartRateMonitor object is of
        appropriate format
        :param data: input passed into HeartRateMonitor for self.data
        :type data: list

        :return: whether data is formatted correctly
        :rtype: boolean
        """
        pass
