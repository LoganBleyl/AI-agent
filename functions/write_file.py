import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
    valid_target_dir = os.path.commonpath([abs_working_dir, target_path]) == abs_working_dir
    parent_directory = os.path.dirname(target_path)
    
    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_path) == True:
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    os.makedirs(parent_directory, exist_ok=True)
    with open(target_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
