"""
In a large collection of MP3 files, there may be more than one copy of the same song,
stored in different directories or with different file names. The goal of this exercise is to search for
duplicates.
1. Write a program that searches a directory and all of its subdirectories, recursively, and returns
a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides
several useful functions for manipulating file and path names.
2. To recognize duplicates, you can use md5sum to compute a "checksum" for each files. If two
files have the same checksum, they probably have the same contents.
3. To double-check, you can use the Unix command diff.
"""
import os
import sys
import hashlib

#function to return the MD5 of a file

def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

#function to scan the directory for duplicates

def findDup(parentFolder):
    # Duplicates in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate MD5hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups

"""
When findDup finishes traversing the directory,
it returns a dictionary with the duplicated files.
If we are going to traverse several directories
we need a method to merge two dictionaries:"""

# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]



def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')

    else:
        print('No duplicate files found.')


if __name__ == '__main__':
    paths=input("Enter the directory")
    if len(paths) > 1:
        dups = {}

         # Find the duplicated files and append them to the dups
        joinDicts(dups, findDup(paths))

        printResults(dups)
    else:
        print('Usage: python dupFinder.py folder or python dupFinder.py folder1 folder2 folder3')
