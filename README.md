# RE-File-Search

A quick, reusable file search module using a regular expression to search
a file path for a filename.  

Recursively searches the passed directory (search_dir) for files matching
the passed regular expression (regex) and returns either the first match
or a list of matches formatted as a Path objects if found.  

## Usage

Drop it into your working folder and import to use.

```py
import regexsearch

# Get a single file path:
needed_file = regexsearch.searchfile('/Users/dev/Downloads/', 'Invoice.*pdf$')

# Get a list of file paths:
files_list = regexsearch.searchfiles('/Users/dev/Downloads/', 'Invoice.*pdf$') 
```
