import json
import sys, os
from task_processes import process_command
"""
    Steps for this project:
     - Create a basic CLI structure to handle user inputs.

     - Utilize a database that utilizes JSON file to save files
        {
            "id": int,
            "description": str,
            "status": todo, in-progress, done,
            "createdAt": date
            "updatedAt": date
        }
     -



     Note:
        Create a README file
"""


def create_json_file_it_not_exists():
    filepath = 'tracker_db.json'
    if not os.path.exists(filepath):
        try:
            with open(filepath, 'w') as f:
                data = {
                    "counter": 0,
                    "tasks": []
                }
                json.dump(data, f, indent=4)
            print(f'File created: {filepath}')
        except OSError as e:
            print(f"Error creating file: {e}")



if __name__ == "__main__":
    create_json_file_it_not_exists()
    if len(sys.argv) >= 1:
        command = sys.argv[1]
        if sys.argv[2:]:
            args = sys.argv[2:]
        else:
            args = None
        process_command(command, args)
    else:
        print("Arguments requirement to run command")