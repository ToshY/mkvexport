# pylint: disable=missing-module-docstring

import subprocess as sp
from rich.console import Console
from src.exception import MKVmergeError, MKVextractError, ProcessError

console = Console()


# pylint: disable=too-few-public-methods
class Process:
    """Subprocess console display"""

    def __init__(self):
        self.process_exceptions = {
            "mkvmerge": MKVmergeError,
            "mkvextract": MKVextractError,
            "other": ProcessError,
        }

        self.colors = {"ok": "green", "busy": "cyan"}

    def run(self, process, command, process_color="#F79EDE"):
        """Run specified command"""

        console.print(
            f"> The following [{process_color}]{process}[/{process_color}] command will be executed:\r"
        )
        console.print(f"[{self.colors['ok']}]{' '.join(command)}[/{self.colors['ok']}]")
        console.print(
            f"\r> [{process_color}]{process}[/{process_color}] [{self.colors['busy']}]running...[/"
            f"{self.colors['busy']}]",
            end="\r",
        )

        response = sp.run(command, stdout=sp.PIPE, stderr=sp.PIPE, check=False)
        return_code = response.returncode
        if return_code == 0:
            console.print(
                f"> [{process_color}]{process}[/{process_color}] [{self.colors['ok']}]completed[/"
                f"{self.colors['ok']}]!\r\n"
            )
            return response

        if command[0] not in self.process_exceptions:
            exception = self.process_exceptions["other"]
        else:
            exception = self.process_exceptions[command[0]]

        message_exception = response.stdout.decode("utf-8")
        if bool(
            response.stderr.decode("utf-8")
            and not response.stderr.decode("utf-8").isspace()
        ):
            message_exception = response.stderr.decode("utf-8")

        raise exception(
            f"Process returned exit code `{return_code}`.\r\n\r\n{message_exception}"
        )
