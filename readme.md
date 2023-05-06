# Ignore Zipper

Puts everything in the current directory in a zip file except for files 
whose names are in a txt file called "exclude.txt"

# Sample "exclude.txt"
"""
env
.gitignore
ex1.py
ex2.txt
ex3
ex5.txt
.zip
"""
# Current features:
- Can be run as a CLI with the cdxzip command
- Can also be put on regedit to run from a context menu
- Excludable files:
  - File Literals
  - Directories
  - Extensions