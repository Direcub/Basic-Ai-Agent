import os
import sys

def get_files_info(working_directory, directory=None):
    if directory is None:
        return "No directory provided."
    directory = os.path.abspath(directory)