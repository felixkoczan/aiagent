import os
from config import MAX_CHARS
import google.genai as genai

def get_file_content(file_path, working_directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return(f"Error: {file_path} is not in the working directory")
    
    if not os.path.isfile(abs_file_path):
        return f"\n\nError {file_path} is not a file\n"
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (
                    f"\n\n... File {file_path} truncated at 10000 characters.\n"
                )
        return file_content_string
    
    except Exception as e:
        return f"Excpetion reading file: {e}"
    
schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of files in the specified directory, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to retrieve files from, relative to the working directory.",
            ),
        },
    ),
)