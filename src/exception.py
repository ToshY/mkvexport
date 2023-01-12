# pylint: disable=missing-module-docstring


class SubtitleExtensionError(Exception):
    """Exception raised when unable to identify subtitle extension from codec id"""


class MKVmergeError(Exception):
    """Exception raised when MKVmerge identify fails"""


class MKVextractError(Exception):
    """Exception raised when MKVextract fails"""


class ProcessError(Exception):
    """Exception raised when a custom subprocess fails"""
