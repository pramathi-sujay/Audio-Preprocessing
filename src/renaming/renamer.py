"""
renamer.py

Generates standardized filenames for audio files.
"""

import re

from .config import FILE_NUMBER_PADDING


def generate_filename(
    class_name: str,
    file_number: int,
    extension: str = ".wav",
) -> str:
    """
    Generate a standardized filename.

    Parameters
    ----------
    class_name : str
        Name of the class.

    file_number : int
        Sequential file number.

    extension : str
        File extension.

    Returns
    -------
    str
        Standardized filename.
    """

    # Convert to lowercase
    prefix = class_name.lower()

    # Replace spaces, hyphens and underscores with a single underscore
    prefix = re.sub(r"[\s\-_]+", "_", prefix)

    # Remove non-alphanumeric characters
    prefix = re.sub(r"[^a-z0-9_]", "", prefix)

    # Remove leading/trailing underscores
    prefix = prefix.strip("_")

    filename = (
        f"{prefix}_"
        f"{file_number:0{FILE_NUMBER_PADDING}d}"
        f"{extension}"
    )

    return filename