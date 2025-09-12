# contains all CLI code
import json
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

if __name__ == "__main__":

    list_tasks()

    with open('data.json', 'r') as f: 
        data=json.load(f)
        print(data)