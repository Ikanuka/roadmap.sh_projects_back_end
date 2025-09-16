# shebang line for Unix-based systems
#!/usr/bin/env python3

# contains all CLI code
import json
import sys
from datetime import datetime
import os

# Path absolute to data file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data.json')

# Upload ou create file
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)
        # Create an empty list if file does not exist
        # dump() writes the JSON data to the file

with open(DATA_FILE) as file:
    try: 
        tasks= json.load(file)
        if not isinstance(tasks, list) :
            tasks = []
            # Ensure tasks is a list
        # Load existing tasks
    except json.JSONDecodeError:
        tasks = []
        # Initialize with empty list if file is empty or corrupted

#Function CLI
def add_task(description):
    now = datetime.now().isoformat(timespec='seconds')
    task_id = len(tasks) + 1
    task = {
        "id":task_id,
        "description": description,
        "status": "todo",
        "created_at": now,
        "updated_at": now
    }
    tasks.append(task)
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)
    print(f"Task added: {description}")

# #Listing all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        print(f"[{t['id']}]{t ['description']} - {t['status']} (Created at: {t['created_at']})")
    
def delete_tasks(task_id):
    global tasks
    task_id = int(task_id)
    for t in tasks: 
        if t['id'] == task_id:
            tasks.remove(t)
            with open (DATA_FILE, 'w') as file:
                json.dump(tasks, file, indent=2)
            print(f"Task {task_id} deleted.")
            return
    print(f"Task {task_id} not found.")
    

def update_tasks(task_id, new_description):
    global tasks
    task_id = int(task_id)
    for t in tasks:
        if t['id'] == task_id:
            t['description']= new_description
            t['uptaded_at']= datetime.now().isoformat(timespec='seconds')
            with open (DATA_FILE, 'w') as file:
                json.dump(tasks, file, indent=2)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")

   

# Command gestion from command line
if len(sys.argv) < 2:
    print("Please provide a task description, available commands: add, list.")
    sys.exit(1)


command = sys.argv[1].lower()
if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)

elif command == "list":
    list_tasks()

elif command == 'delete':
    delete_tasks(sys.argv[2])

elif command == 'update':
    update_tasks(sys.argv[2], " ".join(sys.argv[3:]))
else :
    print(f'Unknown command: {command}')
    sys.exit(1)
    