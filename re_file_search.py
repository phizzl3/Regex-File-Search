"""
Recursively searches the passed directory (searchdir) for files matching
the passed regular expression (regex) and returns either the first match
or a list of matches formatted as a Path objects if found.
"""

import os
import re
from pathlib import Path


def get_file(searchdir: str, regex: str) -> Path:
    """
    Recursively searches the passed directory (searchdir) for files matching
    the passed regular expression (regex) and returns the first match found
    formatted as a pathlib.Path object. 

    Args:
        searchdir (str/pathlib.Path): Directory to search for file.
        regex (str): Regular expression pattern to search filenames 
        for a match.

    Returns:
        pathlib.Path: File path of first file matching the searched regex. 
    """
    return _find_matches(searchdir, regex, first=True)[0]


def get_list(searchdir: str, regex: str) -> list:
    """
    Recursively searches the passed directory (searchdir) for files matching
    the passed regular expression (regex) and returns a list of matches
    formatted as pathlib.Path objects if found. 

    Args:
        searchdir (str/pathlib.Path): Directory to search for file.
        regex (str): Regular expression pattern to search filenames 
        for a match.

    Returns:
        list: List of file paths (pathlib.Path objects) that includes all 
        matching filenames. 
    """
    return _find_matches(searchdir, regex)


def _find_matches(searchdir: str, regex: str, first: bool = False) -> list:
    """
    This function is called by the other included functions to generate 
    their output.

    Recursively searches the passed directory (searchdir) for files matching
    the passed regular expression (regex) and returns a list of matches
    formatted as pathlib.Path objects if found. Returns a list with a single 
    match (first one found) if first=True.

    Args:
        searchdir (str/pathlib.Path): Directory to search for file.
        regex (str): Regular expression pattern to search filenames 
        for a match.
        first (bool, optional): T/F flag that determines if a list 
        with only the first item found is returned. Defaults to False.

    Returns:
        list: List of file paths (pathlib.Path objects) that includes all 
        matching filenames. Only includes a single item if first=True.
    """
    paths_list = []
    for root, _dirs, files in os.walk(searchdir):
        for file in files:
            if re.search(regex, file):
                paths_list.append(Path(f'{root}/{file}'))
            if paths_list and first:
                return paths_list
    return paths_list


if __name__ == '__main__':
    # Test run...
    p = Path(__file__).parent
    sp = r'.+\..[md|py]$'

    # First file found:
    f = get_file(p, sp)
    print(f"\nFirst found:\n{f}")

    # List of matching files:
    l = get_list(p, sp)
    print("\nList:")
    for each in l:
        print(each)
