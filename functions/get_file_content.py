import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    if file_path:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    if not os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    
    try:
        with open(abs_file_path, 'r') as f:
            content = f.read(MAX_CHARS)
        if len(content) == MAX_CHARS:
            return content + f' [...File "{file_path}" truncated at 10000 characters]'
        else:
            return content

    except Exception as e:
        return f'Error: Could not read file "{file_path}": {str(e)}'