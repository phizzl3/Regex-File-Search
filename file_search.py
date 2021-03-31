"""
Recursively searches the passed directory (searchdir) for a file that 
matches the passed regular expression (regex) and returns it's location 
as a Path object if found. (Return None if not.)
"""

import os
import re
from pathlib import Path


def get_path(searchdir: Path, regex: str) -> Path:
    """
    Recursively searches the passed directory (searchdir) for a file that 
    matches the passed regular expression (regex) and returns it's location 
    as a Path object if found. (Returns None if not.)

    Args:
        searchdir (Path): Directory to search for file.
        regex (str): Regular expression to search filenames for a match.

    Returns:
        Path: Path object pointing to to found file.
    """
    for root, _dirs, files in os.walk(searchdir):
        for file in files:
            if re.search(regex, file):
                return Path(f'{root}/{file}')
    else:
        return None
