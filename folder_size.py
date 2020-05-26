"""
This script finds size of a folder.
"""

import os

folder = r"C:/Users/Desktop/docs"
folder_size = 0

for (path, dirs, files) in os.walk(folder):
    for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)
        
def convert_bytes(number):
    """
    This function will convert bytes to MB.... GB... etc
    """
    for memory_representation  in ['Bytes', 'KB', 'MB', 'GB', 'TB']:
        if number < 1024.0:
            return "%3.1f %s" % (number, memory_representation)
        number /= 1024.0
       
print(convert_bytes(folder_size))
