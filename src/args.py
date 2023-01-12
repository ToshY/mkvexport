# pylint: disable=missing-module-docstring

import argparse
from pathlib import Path
from rich.traceback import install

install()


def _get_files_in_directory(file_path: str) -> list:
    """Get the files in the specified directory"""

    return [Path(f) for f_ in [Path(file_path).rglob(e) for e in ["*.mkv"]] for f in f_]


def parse_input_files(input_files: list) -> list:
    """Parse argument list to retrieve input files"""

    batch = []
    for input_file in input_files:
        input_value = [*input_file][0]
        input_type = str(*input_file.values())

        if input_type == FileDirectoryCheck.type_file:
            batch.append(Path(input_value))
            continue

        batch.extend(_get_files_in_directory(input_value))

    return batch


class FileDirectoryCheck(argparse.Action):
    """
    Checks if the specified input file or directory exists.
    If constant is set to false, directories that do not exist will be created.
    """

    base_input_path = Path("/input")
    type_directory = "directory"
    type_file = "file"

    def __call__(self, parser, args, values, option_string=None):
        """File/Directory argument checks"""

        all_values = []
        for input_file in values:
            path_file = self.base_input_path.joinpath(Path(input_file)).resolve()

            if not path_file.exists():
                raise FileNotFoundError(
                    f"The specified filepath `{path_file}` does not exist."
                )

            if path_file.is_file():
                all_values.append({path_file: self.type_file})
                continue

            all_values.append({path_file: self.type_directory})

        setattr(args, self.dest, all_values)
