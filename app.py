import json
import sys, os
from task_processes import process_command
"""
    main function, initial handling of tacker_db.json and main file handling
"""


def create_json_file_if_not_exists(fp):

    if not os.path.exists(fp):
        try:
            with open(fp, 'w') as f:
                data = {
                    "counter": 0,
                    "tasks": []
                }
                json.dump(data, f, indent=4)
            print(f'File created: {fp}')
        except OSError as e:
            print(f"Error creating file: {e}")



if __name__ == "__main__":
    create_json_file_if_not_exists('tracker_db.json')
    if len(sys.argv) >= 1:
        command = sys.argv[1]
        if sys.argv[2:]:
            args = sys.argv[2:]
        else:
            args = None
        process_command(command, args)
    else:
        print("Arguments requirement to run command")