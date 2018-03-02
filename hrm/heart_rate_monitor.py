class HeartRateMonitor:
    """
    Class for a HeartRateMonitor object = takes in ECG data
    and analyzes  it
    Attributes:
        filename (string): filepath to ECG file
        num_entries (int): number of entries per line of ECG csv file
        data (numpy array): ECG data
        mean_hr_bpm (int): estimated average heart rate over a
                           user-specified number of minutes (default = 1 min)
        voltage_extremes (tuple): tuple containing minimum and maximum lead
                                  voltages
        duration (float): time duration of the ECG strip
        num_beats (int): number of detected beats in the strip
        beats (numpy array): numpy array of times when a beat occurred
        units (string): represents the units of time (default = seconds)
    """

    def __init__(self, filename, num_entries=2, data=None, mean_hr_bpm=None,
                 voltage_extremes=None, duration=None, num_beats=None,
                 beats=None, units='second'):
        """
        Initializes instance of class HeartRateMonitor
        :param filename: filename/path for ECG data
        :type filename: string
        :param num_entries: number of entries to expect per line in csv
        :type num_entries: int
        :param data: 2d numpy array containing time/voltages
        :type data: numpy array
        :param mean_hr_bpm: estimated average heart rate over a
                            user-specified number of minutes (default = 1 min)
        :type mean_hr_bpm: int
        :param voltage_extremes: tuple containing min & max lead voltages
        :type voltage_extremes: tuple
        :param duration: time duration of ECG strip
        :type duration: float
        :param num_beats: number of detected beats
        :type num_beats: int
        :param beats: numpy array of times when a beat occurred
        :type beats: numpy array
        :param units: units of time from the csv file (default = seconds)
        :type units: string
        """
        self._filename = filename
        self.num_entries = num_entries
        if not data:
            data = self.read_file(filename)
        self.data = data
        self.mean_hr_bpm = mean_hr_bpm
        self.voltage_extremes = voltage_extremes
        if not duration:
            self.find_duration()
        else:
            self.duration = duration
        self.num_beats = num_beats
        self.beats = beats
        self.units = units

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self.data = self.read_file(filename)
        self._filename = filename
        self.calculate_all_values()

    def calculate_all_values(self):
        """
        Calculates all values of the HRM object based on its
        data array

        :return: True if no exceptions thrown
        :rtype: boolean
        """
        try:
            import logging
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        logging.basicConfig(filename='calculate_all_values.log', filemode='w',
                            level=logging.DEBUG)
        try:
            self.find_duration()
            self.find_heart_rate()
            self.find_beats()
            self.find_num_beats()
            self.find_extreme_voltages()
        except BaseException as e:
            logging.warning("Error encountered: {}".format(e))
            return False
        logging.info("All values calculated")
        try:
            self.write_json()
        except BaseException as e:
            logging.warning("Error encountered writing JSON: {}".format(e))
            return False
        return True

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
            import logging
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
        # remove zero placeholder
        data = np.delete(data, (0), axis=0)
        if len(data) == 0:
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

        :return: 1d numpy array of voltages
        :rtype: numpy array
        """
        try:
            from tools.hrm_tools import return_column
            import numpy as np
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        data_mat = np.matrix(self.data)
        arr = return_column(data_mat, index)
        return arr[0]

    def return_times(self, index=0):
        """
        Returns numpy array of times voltages were recorded
        :param index: index of time in self.data
        :type index: int

        :return: 1d numpy array of times
        :rtype: numpy array
        """
        try:
            from tools.hrm_tools import return_column
            import numpy as np
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        data_mat = np.matrix(self.data)
        arr = return_column(data_mat, index)
        return arr[0]

    def find_duration(self):
        """
        Sets duration of HeartRateMonitor object
        """
        t = self.return_times()
        if t.size == 0:
            self.duration = 0
            return
        last_sample = t[-1]
        self.duration = last_sample

    def find_fs(self):
        """
        Finds the average sampling frequency

        :return: sampling frequency
        :rtype: float
        """
        try:
            import numpy as np
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        v = self.return_voltages()
        t = self.return_times()
        t_diff = np.diff(t)
        fs = 1/np.mean(t_diff)
        return fs

    def find_heart_rate(self):
        """
        Finds heart rate of HeartRateMonitor object data
        """
        try:
            import numpy as np
            from tools.hrm_tools import autocorr_freq
            import logging
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        logging.basicConfig(filename='find_heart_rate.log', filemode='w',
                            level=logging.DEBUG)
        v = self.return_voltages()
        fs = self.find_fs()
        hr = autocorr_freq(v, fs)
        if hr == 0:
            logging.warning("HR calculated to be 0, "
                            " possible error in data format")
        logging.info("Returned value from "
                     "autocorr_freq: {}".format(hr))
        if self.units == 'second' or self.units == 's':
            hr *= 60
        if self.units == 'millisecond' or self.units == 'ms':
            hr *= 60000
        logging.info("Setting self.mean_hr_bpm "
                     "to: {}".format(hr))
        self.mean_hr_bpm = hr

    def find_heart_rates_for_interval(self, minutes):
        """
        Finds heart rate of HeartRateMonitor object data over a
        user specified number of minutes

        :param minutes: number of minutes to average heart rate
        :type minutes: int

        :return: array of heart rates
        :rtype: 1d numpy array
        """
        try:
            import numpy as np
            from tools.hrm_tools import autocorr_freq
            import logging
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        hr_array = []
        volts = self.return_voltages()
        times = self.return_times()
        fs = self.find_fs()
        start = 0.0
        end = curr = 0
        curr_volts = []
        if self.units == 'second' or self.units == 's':
            step = minutes*60
        if self.units == 'millisecond' or self.units == 'ms':
            step = minutes*60000
        for v, t in zip(volts, times):
            if t > step + start:
                hr = autocorr_freq(curr_volts, fs)
                if self.units == 'second' or self.units == 's':
                    hr *= 60
                if self.units == 'millisecond' or self.units == 'ms':
                    hr *= 60000
                hr_array += [hr]
                # this v,t pair is out of range
                # so start new array wih only that voltage
                step_volts = [v]
                start = step + start
                end = curr
            else:
                curr_volts.append(v)
            curr += 1
        # voltages that are left
        hr = autocorr_freq(curr_volts, fs)
        if self.units == 'second' or self.units == 's':
            hr *= 60
        if self.units == 'millisecond' or self.units == 'ms':
            hr *= 60000
        hr_array += [hr]
        return np.array(hr_array)

    def find_extreme_voltages(self):
        """
        Finds extreme voltage tuple (min, max) for ECG strip
        """
        try:
            import numpy as np
            from tools.hrm_tools import find_max, find_min
            import logging
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        logging.basicConfig(filename='find_extreme_voltages.log', filemode='w',
                            level=logging.DEBUG)
        v = self.return_voltages()
        maximum = find_max(v)
        minimum = find_min(v)
        logging.info("Setting self.extreme_voltages"
                     "to: {}".format((minimum, maximum)))
        self.voltage_extremes = (minimum, maximum)

    def find_beats(self):
        """
        Finds times of detected beats in ECG strip
        """
        try:
            import numpy as np
            from tools.hrm_tools import autocorr_freq
            import logging
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        logging.basicConfig(filename='find_beats.log', filemode='w',
                            level=logging.DEBUG)
        fs = self.find_fs()
        volts = self.return_voltages()
        times = self.return_times()
        hr = autocorr_freq(volts, fs)
        try:
            step = 1/hr
        except ZeroDivisionError:
            logging.error("autocorr_freq returned value of 0")
            return []
        beats_list = []
        start = 0.0
        end = curr = 0
        step_volts = np.array([])
        for v, t in zip(volts, times):
            if t > step + start:
                max_index = np.argmax(step_volts) + end
                try:
                    beats_list.append(times[max_index])
                except IndexError:
                    logging.warning("Index out of range")
                    continue
                # this v,t pair is out of range
                # so start new array wih only that voltage
                step_volts = np.array(v)
                start = step + start
                end = curr
            else:
                step_volts = np.append(step_volts, v)
            curr += 1
        logging.info("Setting self.beats"
                     "to array of len: {}".format(len(beats_list)))
        self.beats = np.array(beats_list)

    def find_num_beats(self):
        """
        Finds number of detected beats in ECG strip
        """
        try:
            import numpy as np
            import logging
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        logging.basicConfig(filename='find_num_beats.log', filemode='w',
                            level=logging.DEBUG)
        logging.info("Setting self.num_beats"
                     "to: {}".format(self.beats.size))
        self.num_beats = self.beats.size

    def write_json(self):
        """
        Dumps important attributes from HRM object into
        a JSON file with the same filename/filepath as the
        CSV file the data came from
        """
        try:
            import json
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        filename = self.filename
        try:
            json_file = filename.replace('.csv', '.json')
        except AttributeError as e:
            print("self.filename has wrong type: {}".format(e))
            raise TypeError()
        vals = self.return_values_dict()
        with open(json_file, 'w') as f:
            json.dump(vals, f)

    def return_values_dict(self):
        """
        Returns a dictionary of important attributes

        :return: dict of attributes
        :rtype: dict
        """
        try:
            from datetime import date
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return
        values = {
                  "mean_hr_bpm": self.mean_hr_bpm,
                  "duration": self.duration,
                  "units": self.units,
                  "voltage_extremes": self.voltage_extremes,
                  "num_beats": (self.num_beats),
                  "beats": list(self.beats)
                 }
        return values
