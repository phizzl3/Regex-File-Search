__version__ = "1.1.1"

import os
import re
from pathlib import Path


def regex_search_file(search_dir: str, regex: str) -> Path:
    try:
        return __find_matches(search_dir, regex, first_found=True)[0]
    except IndexError:
        return None


def regex_search_files(search_dir: str, regex: str) -> list[Path]:
    return __find_matches(search_dir, regex)


def __find_matches(
    search_dir: str, regex: str, first_found: bool = False
) -> list[Path]:
    paths_list = []
    for root, _dirs, files in os.walk(search_dir):
        for file in files:
            if re.search(regex, file):
                paths_list.append(Path(f"{root}/{file}"))
            if paths_list and first_found:
                return paths_list
    return paths_list


if __name__ == "__main__":
    # Test run...
    p = Path(__file__).parent
    sp = r".+\..[md|py]$"

    # First file found:
    f = regex_search_file(p, sp)
    print(f"\nFirst found:\n{f}")

    # List of matching files:
    l = regex_search_files(p, sp)
    print("\nList:")
    for each in l:
        print(each)
