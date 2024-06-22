from pathlib import Path

from mkvexport.exception import SubtitleCodecError


def files_in_dir(path: Path, file_types=["*.mkv"]):
    """
    Returns a list of files in the specified directory that match the given file types.

    Args:
        path (Path): The path to the directory.
        file_types (List[str], optional): A list of file types to match. Defaults to ["*.mkv"].

    Returns:
        List[Path]: A list of Path objects representing the files in the directory that match the given file types.
    """

    flist = [f for f_ in [path.rglob(e) for e in file_types] for f in f_]

    return flist


def get_subtitle_extension_from_codec_id(codec_id: str) -> str:
    match codec_id:
        case "S_TEXT/ASS" | "S_TEXT/SSA":
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
            raise SubtitleCodecError(codec_id)
