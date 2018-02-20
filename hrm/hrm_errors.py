class HRMCustomError(BaseException):
    """
    Custom set of exceptions for hrm package
    """
    def __init__(self, message=""):
        """
        Creating an instance of an exception
        :param message: optional message to explain exception
        :type message: string
        """
        self.message = message


class EmptyFileError(HRMCustomError):
    """
    Exception to be thrown if given file is empty
    """
    pass


class FileFormatError(HRMCustomError):
    """
    Exception to be thrown if given file with
    wrong format
    """
    pass
