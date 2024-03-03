# Regex-File-Search

A quick, reusable file search module using a regular expression to search
a file path for a filename.  

Recursively searches the passed directory *search_dir* for files matching
the passed regular expression *regex* and returns either the first match
or a list of matches formatted as a Path objects if found.  

## Usage

```py
import regexfilesearch

# Get a single file path (first found):
needed_file = regexfilesearch.regex_search_file('/Users/dev/Downloads/', 'Invoice.*pdf$')

# Get a list of file paths:
files_list = regexfilesearch.regex_search_files('/Users/dev/Downloads/', 'Invoice.*pdf$') 
```
