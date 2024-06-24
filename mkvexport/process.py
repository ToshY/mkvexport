import subprocess as sp

from mkvexport.exception import MKVmergeError, ProcessError


class ProcessCommand:
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
        Runs the specified process with the given command.

        Args:
            process (str): The name of the process being executed.
            command (List[str]): The command to be executed.

        Returns:
            CompletedProcess: The result of the command execution.

        Raises:
            MKVmergeError: If the process is 'mkvmerge' and it fails with a non-zero exit code.
            ProcessError: If the process fails with a non-zero exit code and no specific exception is defined.
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
