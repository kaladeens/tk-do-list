"""
    In this function we will have many functions that will help us to retrieve data and to manipulate this data
"""

import json

PATH = '../data/'

def read_file(filename: str):
    """
        This function will read the tasks from the file and return it as a list
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
            if not content:
                return []
            return json.loads(content)
        
    except (json.JSONDecodeError, FileNotFoundError) as e:
        # Handle the error or log it
        print(f"Error reading file {filename}: {e}")
        return []

def write_task_to_file(filename: str, data: any):
    with open(filename,'w') as file:
        # json.dump(data, file, indent=4, cls=TaskEncoder)
        pass
