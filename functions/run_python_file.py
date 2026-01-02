import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
        if os.path.isfile(target_path) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
    
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]
    
        if args != None:
            command.extend(args)

        complete_process = subprocess.run(
                command, 
                cwd=working_dir_abs, 
                capture_output=True, 
                text=True, 
                timeout=30)
        
        output_parts = []

        if complete_process.returncode != 0:
            output_parts.append(f"Process exited with code {complete_process.returncode}")

        if not complete_process.stdout and not complete_process.stderr:
            output_parts.append("No output produced")
        if complete_process.stdout:
            output_parts.append(f"STDOUT:\n{complete_process.stdout}")
        if complete_process.stderr:
            output_parts.append(f"STDERR:\n{complete_process.stderr}") 
    except Exception as e:
        return f"Error: executing Python file: {e}"

    return "\n".join(output_parts)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file based on the provided file_path and optional args.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the python file to be ran.",
            ), 
            "args": types.Schema( 
            type=types.Type.ARRAY,
            items=types.Schema(type=types.Type.STRING),
            description="Optional argument provided to the function to run."
            )
        },
    ),
)
    
