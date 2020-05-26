"""
This script finds size of a file in 'Bytes', 'KB', 'MB', 'GB' or 'TB'. Also finds 
the file or files with minimum size, maximum size and avearge of all files in a folder.  
    
Reference:
    https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python
    https://unix.stackexchange.com/questions/200316/how-to-find-maximum-and-minimum-file-size-along-with-their-path-in-a-directory
"""

import os


def convert_bytes(number):
    """
    This function will convert bytes to MB.... GB... etc
    """
    for memory_representation  in ['Bytes', 'KB', 'MB', 'GB', 'TB']:
        if number < 1024.0:
            return "%3.1f %s" % (number, memory_representation)
        number /= 1024.0


def file_size(file_path):
    """
    This function will return the file size
    """
    if os.path.isfile(file_path):
        return (file_path, os.stat(file_path).st_size)


# To get size of one file

one_file_size = os.path.getsize(r"C:\Users\Desktop\image1.jpg")
print(convert_bytes(one_file_size))


# To get size of different files

filepath_with_filesize = []

for root, dirs, files in os.walk(r"C:/Users/Desktop/docs"):
    for file in files:
        file_path = (os.path.join(root, file))  # Access files with any extension
        filepath_with_filesize.append(file_size(file_path))

filesizes = [filesize[1] for filesize in filepath_with_filesize]

minimum_file_size = min(filesizes)
maximum_file_size = max(filesizes)
average_file_size = 0

if len(filesizes) > 0:
    average_file_size = sum(filesizes) / len(filesizes)

minimum_file = [file[0] for file in filepath_with_filesize if file[1] == minimum_file_size]
maximum_file = [file[0] for file in filepath_with_filesize if file[1] == maximum_file_size]

print("\nMinimum file size: {0} or {1}".format(minimum_file_size, convert_bytes(minimum_file_size)))
for file in minimum_file: 
    print(file)

print("\nMaximum file size: {0} or {1}".format(maximum_file_size, convert_bytes(maximum_file_size)))
for file in maximum_file:
    print(file)

print("\nAverage file size: {0} or {1}".format(average_file_size, convert_bytes(average_file_size)))
