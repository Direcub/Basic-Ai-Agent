import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    if file_path:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        return f'Error: File "{file_path}" not found.'
    
    if not os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(('.py')):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(['python3', abs_file_path], cwd=working_directory, capture_output=True, text=True, timeout=30)
        if not result.stdout and not result.stderr:
            return "No output produced"
        return f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nReturn code: {result.returncode}'

    except Exception as e:
        return f'Error: executing Python file: {str(e)}'