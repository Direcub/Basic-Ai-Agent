import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    if file_path:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    if not os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(os.path.dirname(abs_file_path)):
            os.makedirs(os.path.dirname(abs_file_path))
        
        with open(abs_file_path, 'w') as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: Could not create directory for "{file_path}": {str(e)}'
    
