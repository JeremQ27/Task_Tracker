import json
from datetime import date



"""
        task_database format
        {
            'counter': int
        }
        {
            'tasks': [
        {
            "id": int,
            "description": str,
            "status": todo, in-progress, done,
            "createdAt": date
            "updatedAt": date
        },
        ]
"""

DB_PATH = 'tracker_db.json'


def load_tasks(fp):
    with open(fp, 'r') as f:
        return json.load(f)


def save_tasks(fp, data):
    with open(fp, 'w') as f:
        return json.dump(data, f, indent=4)


def add_task(database, args):
    database["counter"] += 1
    new_task = {
        "id": database["counter"],
        "description": args[0],
        "status": "todo",
        "createdAt": str(date.today()),
        "updatedAt": str(date.today())
    }
    database["tasks"].append(new_task)


def update_task(database, args):
    target_id = int(args[0])
    updated_desc = args[1]
    for task in database["tasks"]:
        if task["id"] == target_id:
            task["description"] = updated_desc
            task["updatedAt"] = str(date.today())
            break


def delete_task(database, args):
    found = False
    target_id = int(args[0])
    updated_tasks = []
    for task in database["tasks"]:
        if target_id == task['id']:
            found = True
        else:
            updated_tasks.append(task)
    database["tasks"] = updated_tasks
    if not found:
        print(f'ID {target_id} not found. Delete not possible')


def mark_task(database, command, args):
    found = False
    command = command[5:]
    target_id = int(args[0])
    for task in database["tasks"]:
        if task['id'] == target_id:
            if command == 'done':
                task['status'] = 'done'
            elif command =='in-progress':
                task['status'] = 'in-progress'
            found = True
    if not found:
        print(f'ID {target_id} not found. Update not possible.')


def list_tasks(database, args):
    check_str = None
    if args:
        check_str = args[0]
    for task in database['tasks']:
        if check_str and task['status'] == check_str or check_str is None:
            print(f"Task: {task['description']}\nStatus: {task['status']}\nCreation Date: {task['createdAt']}\nLast Update: {task['updatedAt']}")
            print('\n\n')


def process_command(command, args):
    database = load_tasks(DB_PATH)

    if command == "add":
        add_task(database, args)

    elif command == 'update':
        update_task(database, args)

    elif command == 'delete':
        delete_task(database, args)

    elif command == 'mark-in-progress' or command == 'mark-done':
        mark_task(database, command, args)

    elif command == 'list':
        list_tasks(database, args)

    save_tasks(DB_PATH, database)



