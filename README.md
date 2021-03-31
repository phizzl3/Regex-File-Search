# FileSearch

A quick, reusable file search module using a regular expression to search
a file path for a filename.

## Usage

Drop it into your working folder and import to use.

```py
import file_search

needed_file = file_search.get_path('/Users/dev/Downloads/', 'Invoice.*pdf')

print(needed_file)
# '/Users/dev/Downloads/Invoice_1234.pdf'
print(needed_file.name)
# 'Invoice_1234.pdf'
```
