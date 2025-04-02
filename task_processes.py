import json
from datetime import date

"""
        task_format
        {
            'counter': int
        }
        {tasks:[
        {
            "id": int,
            "description": str,
            "status": todo, in-progress, done,
            "createdAt": date
            "updatedAt": date
        },
        ]
"""
def load_tasks():
    with open('tracker_db.json', 'r') as f:
        return json.load(f)

def save_tasks(data):
    with open('tracker_db.json', 'w') as f:
        return json.dump(data, f, indent=4)


def process_command(command, args):
    if command == "add":
        add_task(args)

    elif command == 'update':
        print('Update Command')
        print(args)
    elif command == 'delete':
        print('Delete Command')
        print(args)


def add_task(args):
    data = load_tasks()
    data["counter"] += 1
    new_task = {
        "id": data["counter"],
        "description": args[0],
        "status": "todo",
        "createdAt": str(date.today()),
        "updatedAt": str(date.today())
    }
    data["tasks"].append(new_task)
    save_tasks(data)


