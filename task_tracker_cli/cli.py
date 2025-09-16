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

# Upload or create file
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
    if task_id == task_id:
        task_id += 1
# #Listing all tasks

def list_tasks(status=None):
    if status:
        filtered_tasks = [t for t in tasks if t['status'] == status]
    else:
        filtered_tasks = tasks

    if not filtered_tasks: 
        print(f"No tasks with status '{status}' found." if status else "No tasks found.")
        return

     # Affichage de l'en-tête
    print(f"{'ID':<5} {'Description':<30} {'Status':<12} {'Created At':<20} {'Updated At':<20}")
    print("-" * 90)

        # Affichage des tâches
    for t in filtered_tasks:
        print(f"{t['id']:<5} {t['description']:<30} {t['status']:<12} "
        f"{t['created_at']:<20} {t['updated_at']:<20}")
                
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

def marking_task_in_progess(task_id):
    global tasks
    task_id = int (task_id)
    for t in tasks:
        if t['id'] == task_id:
            t['status']= "in-progress"
            with open (DATA_FILE, 'w') as file:
                json.dump(tasks, file, indent=2)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")

def marking_task_done(task_id):
    global tasks
    task_id = int (task_id)
    for t in tasks:
        if t['id'] == task_id:
            t['status']= "done"
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
    status = sys.argv[2].lower() if len(sys.argv) > 2 else None
    list_tasks(status)


elif command == 'delete':
    delete_tasks(sys.argv[2])

elif command == 'update':
    update_tasks(sys.argv[2], " ".join(sys.argv[3:]))
    
elif command == 'mark-in-progress':
    marking_task_in_progess(sys.argv[2])

elif command == 'mark-done':
    marking_task_done(sys.argv[2])
else :
    print(f'Unknown command: {command}')
    sys.exit(1)
    