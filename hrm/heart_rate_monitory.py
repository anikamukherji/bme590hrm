class HeartRateMonitor:
    """
    Class for a HeartRateMonitor object = takes in ECG data
    and analyzes  it
    Attributes:
        data (numpy array): ECG data
        mean_hr_bpm (int): estimated average heart rate over a
                           user-specified number of minutes (default = 10 min)
        voltage_extremes (tuple): tuple containing minimum and maximum lead
                                  voltages
        duration (float): time duration of the ECG strip
        num_beats (int): number of detected beats in the strip
        beats (numpy array): numpy array of times when a beat occurred
    """

    def __init__(self, filename, data=None, mean_hr_bpm=None,
                 voltage_extremes=None, duration=None, num_beats=None,
                 beats=None):
        """
        Initializes instance of class HeartRateMonitor
        :param filename: filename/path for ECG data
        :type filename: string
        :param data: numpy array of tuples containing time/voltages
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
        if not self.data:
            data = self.read_file(filename)
        self.data = data
        self._check_data()
        self.mean_hr_bpm = mean_hr_bpm
        self.voltage_extremes = voltage_extremes
        self.duration = duration
        self.num_beats = num_beats
        self.beats = beats

    def read_file(filename):
        """
        """
        pass

    def _check_data(data):
        """
        Ensures that data passed into HeartRateMonitor object is of
        appropriate format
        :param data: input passed into HeartRateMonitor for self.data
        :type data: list

        :returns: whether data is formatted correctly
        :rtype: boolean
        """
        pass
