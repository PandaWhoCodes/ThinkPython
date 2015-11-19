"""
The os module provides a function called walk that is similar
to this one but more
versatile. Read the documentation and use it to print the
names of the files in a given directory and
its subdirectories.
"""

import os

for root, dirs, files in os.walk(".", topdown=False):
    # printing the folders names
    for name in files:
        print(os.path.join(root, name))
    # printing the file names
    for name in dirs:
        print(name)
