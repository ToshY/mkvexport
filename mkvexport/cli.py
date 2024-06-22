import json
from pathlib import Path

import click
from loguru import logger  # noqa

from mkvexport.args import InputPathChecker
from mkvexport.helper import get_subtitle_extension_from_codec_id
from mkvexport.process import ProcessCommand


@logger.catch
@click.command(
    context_settings={"help_option_names": ["-h", "--help"]},
    epilog="Repository: https://github.com/ToshY/mkvexport",
)
@click.option(
    "--input-path",
    "-i",
    type=click.Path(exists=True, dir_okay=True, file_okay=True, resolve_path=True),
    required=False,
    multiple=True,
    callback=InputPathChecker(),
    default=["./input"],
    show_default=True,
    help="Path to input file or directory",
)
def cli(input_path):
    process = ProcessCommand(logger)

    for item in input_path:
        current_input_files = item.get("input").get("resolved")

        for current_file_path_index, current_file_path in enumerate(
            current_input_files
        ):
            mkvmerge_identify_process = process.run(
                process="MKVmerge identify",
                command=[
                    "mkvmerge",
                    "-J",
                    current_file_path.as_posix(),
                ],
            )
            mkvmerge_identify_output = json.loads(mkvmerge_identify_process.stdout)

            file_directory = current_file_path.with_suffix("")
            attachments_directory = f"{file_directory}/attachments"
            Path(attachments_directory).mkdir(parents=True, exist_ok=True)

            for track in mkvmerge_identify_output["tracks"]:
                if track["type"] != "subtitles":
                    continue

                track_properties = track["properties"]
                subtitle_language = "und"
                if bool(
                    track_properties["language"]
                    and not track_properties["language"].isspace()
                ):
                    subtitle_language = track_properties["language"]

                subtitle_extension = get_subtitle_extension_from_codec_id(
                    track_properties["codec_id"]
                )
                subtitle_number = track_properties["number"]

                process.run(
                    f"MKVextract track with codec `{track['codec']}`",
                    [
                        "mkvextract",
                        current_file_path.as_posix(),
                        "tracks",
                        f"{track['id']}:{file_directory}/track{subtitle_number}_{subtitle_language}."
                        f"{subtitle_extension}",
                    ],
                )

            for attachment in mkvmerge_identify_output["attachments"]:
                process.run(
                    f"MKVextract attachment with name `{attachment['file_name']}`",
                    [
                        "mkvextract",
                        current_file_path.as_posix(),
                        "attachments",
                        f"{attachment['id']}:{attachments_directory}/{attachment['file_name']}",
                    ],
                )

            process.run(
                "MKVextract chapters",
                [
                    "mkvextract",
                    current_file_path.as_posix(),
                    "chapters",
                    f"{file_directory}/chapters.xml",
                ],
            )

            process.run(
                "MKVextract tags",
                [
                    "mkvextract",
                    current_file_path.as_posix(),
                    "tags",
                    f"{file_directory}/tags.xml",
                ],
            )
