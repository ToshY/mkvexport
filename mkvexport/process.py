import subprocess as sp
from mkvexport.exception import MKVmergeError, ProcessError


class ProcessCommand:
    """
    Class for displaying subprocess information on the console.

    Attributes:
        logger: The logger object used for logging information.
        process_exceptions: A dictionary mapping process names to corresponding exceptions.
    """

    def __init__(self, logger):
        """
        Initializes a new instance of the ProcessCommand class.

        Args:
            logger (Logger): The logger object used for logging messages.

        Initializes the following instance variables:
            - logger (Logger): The logger object used for logging messages.
            - process_exceptions (dict): A dictionary mapping process names to their corresponding exception classes.
        """
        self.logger = logger
        self.process_exceptions = {
            "mkvmerge": MKVmergeError,
            "custom": ProcessError,
        }

    def run(self, process, command):
        """
        Run a subprocess command and display information on the console.

        Args:
            process: The name of the process being executed.
            command: The command to be executed.
        Raises:
            MKVmergeError: If the MKVmerge command fails.
            ProcessError: If the subprocess fails.
        Returns:
            The response object from the subprocess execution.
        """
        self.logger.info(
            f"The following {process} command will be executed: {' '.join(command)}"
        )

        response = sp.run(command, stdout=sp.PIPE, stderr=sp.PIPE)
        return_code = response.returncode
        if return_code == 0:
            self.logger.info(f"{process} completed.")

            return response

        if command[0] not in self.process_exceptions:
            exception = self.process_exceptions["custom"]
        else:
            exception = self.process_exceptions[command[0]]

        self.logger.critical(response)
        raise exception(
            message=response.stderr.decode("utf-8"),
            exit_code=return_code,
        )
