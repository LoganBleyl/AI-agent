import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(abs_working_dir, directory))
    valid_target_dir = os.path.commonpath([abs_working_dir, target_path]) == abs_working_dir
    
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isdir(target_path) == False:
        return f'Error: "{directory}" is not a directory'

    lines = []

    for file in os.listdir(target_path):
        full_path = os.path.join(target_path, file)
        file_size = os.path.getsize(full_path)
        is_dir = os.path.isdir(full_path)
        line = f"{file}: file_size={file_size} bytes, is_dir={is_dir}"
        lines.append(line)
    return "\n".join(lines)



