# shebang line for Unix-based systems
#!/usr/bin/env python3

# contains all CLI code
import json
import sys
#call the .bat file to run the CLI and make it globally accessible
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = 'data.json'


    
#Adding a new task
def add_task(task):
    with open('data.json', 'r+') as file:
        data = json.load(file)          
        data['tasks'].append(task)
        file.seek(0)
        json.dump(data, file, indent=4)

#Listing all tasks
def list_tasks():
    with open('data.json','r') as file:
        data= json.load(file)
        for task in data['tasks']:
            print(task)

#Input from command line
def input_tasks():
    with open('data.json', 'r+') as file:
        data =json.load(file)
        task=input("Enter a new task: ")
        data['tasks'].append(task)
        file.seek(0)
        json.dump(data, file, indent=4)

def remove_tasks():
    with open('data.json','r+') as file:
        data.json.load(file)
        task=input("Enter a task to remove")
        data['tasks'].remove(task)
        file.seek(0)
        json.dump(data,file,indent=4)

# Main function to run the CLI
if __name__ == "__main__":
    with open('data.json', 'r') as f: 
        data=json.load(f)
    for i in data['tasks']:
    
        print (i)
   
