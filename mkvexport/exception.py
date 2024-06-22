class MKVmergeError(Exception):
    """
    Custom exception class for MKVmerge-related errors.

    This exception is raised when MKVmerge fails with a non-zero exit code.

    Attributes:
        exit_code (int): The exit code of the failed MKVmerge process.
        message (str): The error message associated with the failure.

    Args:
        message (str): The error message associated with the failure.
        exit_code (int): The exit code of the failed MKVmerge process.
    """

    ERROR_MESSAGE = "MKVmerge failed with exit code `{exit_code}`: {message}."

    def __init__(self, message, exit_code):
        self.exit_code = exit_code
        self.message = self.ERROR_MESSAGE.format(message=message, exit_code=exit_code)
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ProcessError(Exception):
    """
    Custom exception class for process-related errors.

    This exception is raised when a process fails with a non-zero exit code.

    Attributes:
        exit_code (int): The exit code of the failed process.
        message (str): The error message associated with the failure.

    Args:
        message (str): The error message associated with the failure.
        exit_code (int): The exit code of the failed process.
    """

    ERROR_MESSAGE = "Process failed with exit code `{exit_code}`: {message}."

    def __init__(self, message, exit_code):
        self.exit_code = exit_code
        self.message = self.ERROR_MESSAGE.format(message=message, exit_code=exit_code)
        super().__init__(self.message)

    def __str__(self):
        return self.message


class SubtitleCodecError(Exception):
    """
    Custom exception class for subtitle codec-related errors.

    This exception is raised when an invalid subtitle codec is provided.

    Attributes:
        message (str): The error message associated with the failure.

    Args:
        message (str): The error message associated with the failure.
    """

    ERROR_MESSAGE = "Invalid subtitle codec `{codec}` provided."

    def __init__(self, message):
        self.message = self.ERROR_MESSAGE.format(codec=message)
        super().__init__(self.message)

    def __str__(self):
        return self.message
