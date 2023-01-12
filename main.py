# pylint: disable=missing-module-docstring

import sys
import json
import argparse
from pathlib import Path
from rich.traceback import install
from rich.console import Console
from src.banner import cli_banner
from src.args import FileDirectoryCheck, parse_input_files
from src.process import Process
from src.exception import SubtitleExtensionError, MKVmergeError

console = Console()
install()


def cli_args() -> list:
    """Parse command line arguments"""

    parser = argparse.ArgumentParser(
        description="Extract subtitles, attachments, chapters and tags.",
        epilog="Repository: https://github.com/ToshY/mkvextract-subs",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=False,
        action=FileDirectoryCheck,
        default=[
            {FileDirectoryCheck.base_input_path: FileDirectoryCheck.type_directory}
        ],
        nargs="+",
        help="Path to input file or directory containing MKV files",
    )

    args = parser.parse_args()

    return parse_input_files(args.input)


def _get_subtitle_extension_from_codec_id(codec_id: str) -> str:
    match codec_id:
        case "S_TEXT/ASS":
            return "ass"
        case "S_TEXT/UTF8":
            return "srt"
        case "S_TEXT/PGS":
            return "sup"
        case "S_VOBSUB":
            return "sub"
        case "S_HDMV/USF":
            return "usf"
        case _:
            raise SubtitleExtensionError(
                f"Subtitle extension for codec id `{codec_id}` could not be determined."
            )


def _mkvidentify_run(process: Process, process_name: str, mkvidentify_arguments: list):
    mkvmerge_result = json.loads(
        process.run(process_name, mkvidentify_arguments).stdout
    )

    if mkvmerge_result["errors"]:
        raise MKVmergeError(
            f"MKVmerge identify encountered the following error: {mkvmerge_result['errors'][0]}"
        )

    return mkvmerge_result


def main():
    """Main"""

    process = Process()
    for input_file in cli_args():
        input_file_string = str(input_file)
        mkvmerge_identify_result = _mkvidentify_run(
            process=process,
            process_name="MKVmerge identify",
            mkvidentify_arguments=[
                "mkvmerge",
                "-J",
                input_file_string,
            ],
        )

        # Prepare attachment directory
        file_directory = input_file.with_suffix("")
        attachments_directory = f"{file_directory}/attachments"
        Path(attachments_directory).mkdir(parents=True, exist_ok=True)

        # Tracks
        for track in mkvmerge_identify_result["tracks"]:
            if track["type"] != "subtitles":
                continue

            track_properties = track["properties"]
            subtitle_language = "und"
            if bool(
                track_properties["language"]
                and not track_properties["language"].isspace()
            ):
                subtitle_language = track_properties["language"]

            subtitle_extension = _get_subtitle_extension_from_codec_id(
                track_properties["codec_id"]
            )
            subtitle_number = track_properties["number"]

            process.run(
                f"MKVextract track with codec `{track['codec']}`",
                [
                    "mkvextract",
                    input_file_string,
                    "tracks",
                    f"{track['id']}:{file_directory}/track{subtitle_number}_{subtitle_language}."
                    f"{subtitle_extension}",
                ],
            )

        # Attachments
        for attachment in mkvmerge_identify_result["attachments"]:
            process.run(
                f"MKVextract attachment with name `{attachment['file_name']}`",
                [
                    "mkvextract",
                    input_file_string,
                    "attachments",
                    f"{attachment['id']}:{attachments_directory}/{attachment['file_name']}",
                ],
            )

        # Chapters
        process.run(
            "MKVextract chapters",
            [
                "mkvextract",
                input_file_string,
                "chapters",
                f"{file_directory}/chapters.xml",
            ],
        )

        # Tags
        process.run(
            "MKVextract tags",
            [
                "mkvextract",
                input_file_string,
                "tags",
                f"{file_directory}/tags.xml",
            ],
        )


if __name__ == "__main__":
    cli_banner("MKVextract  Subs")

    try:
        main()
    except KeyboardInterrupt:
        console.print("\r\n\r\n> [red]Execution cancelled by user[/red]")
        sys.exit()
