# set_pattern_finder
recursively assess a folder of files and return hints towards repeating header patterns


# Usage 

Given a folder of unknown files this tool allows you to work through the whole folder and given a specific sequence lenght start to look for patterns in the binary items. 

Its intended for use when you have files with no positive format ID via PRONON / DROID. 

The sequence length is variable

The tool can dump all the header sequences it finds, or just the summary. 

Example summary: 

Count: 242	 Patterns: 0100 '\x01\x00'
Count: 112	 Patterns: 5343 'SC'
Count: 97	 Patterns: 0207 '\x02\x07'
Count: 17	 Patterns: 001c '\x00\x1c'
Count: 11	 Patterns: 0020 '\x00 '
Count: 10	 Patterns: 0000 '\x00\x00'

The patterns are the raw hex and text (python repr()) encoded versions of the sequence. 

# How to use

There are 4 settable values

`folder`: Just point this at your chosen folder. Use python os.walk to interate through subfolders. 

`start`: Set the starting offset. Defaults to 0

`end` : Set the ending offset, Defaults to 16

`show_all` : if true, dumps every sequence of every file as well as the summary. 

