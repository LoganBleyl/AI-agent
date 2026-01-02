import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a new file or overwrites based on the provided file_path and contents.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path where a new file wille be written or a file will be overwritten.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content provided to be written in the new file or used to rewrite the file."
            )
        },
    ),
)
