# My First CLI Project

**Link to project:** [Task Tracker](https://roadmap.sh/projects/task-tracker)

---

## How It's Made

**Tech used:** Python, JSON, .bat file  

---

## Lessons Learned

- Function declaration and scope (global vs local variables)  
- Using Python modules like `sys`, `os`, and `datetime`  
- Creating a script that communicates directly via a CLI  
- The importance of configuring the PATH so that the CLI detects Python  
- Handling JSON file read/write and basic file operations  
- Building a simple task tracker CLI from scratch  

---

## How to Use It

1. **Install Python** if you don’t already have it:  
[Download Python 😎](https://www.python.org/downloads/)  

2. **Clone the repository** or download the ZIP.  

3. Open a CLI (PowerShell or Command Prompt) and navigate to the project folder:  

```powershell
cd C:\roadmap.sh_projects_back_end\task_tracker_cli

| Command            | Description                                                   | Example                                               |
| ------------------ | ------------------------------------------------------------- | ----------------------------------------------------- |
| `add`              | Add a new task                                                | `.\task-cli add "Buy groceries"`                      |
| `update`           | Update the description of a task by ID                        | `.\task-cli update 1 "Buy groceries and cook dinner"` |
| `delete`           | Delete a task by ID                                           | `.\task-cli delete 1`                                 |
| `mark-in-progress` | Mark a task as in progress by ID                              | `.\task-cli mark-in-progress 1`                       |
| `mark-done`        | Mark a task as done by ID                                     | `.\task-cli mark-done 1`                              |
| `list`             | List all tasks                                                | `.\task-cli list`                                     |
| `list <status>`    | List tasks filtered by status (`todo`, `in-progress`, `done`) | `.\task-cli list done`                                |

Example Output
ID    Description                    Status       Created At           Updated At
------------------------------------------------------------------------------------------
1     Buy groceries                  todo         2025-09-16T15:30:00 2025-09-16T15:30:00
2     Cook dinner                    in-progress  2025-09-16T16:00:00 2025-09-16T16:05:00
3     Take out trash                 done         2025-09-16T16:10:00 2025-09-16T16:15:00

Tips & Tricks (Windows / PowerShell)

To run the CLI from anywhere, make sure the folder containing task-cli.bat is added to your PATH environment variable.

Use quotes " " around task descriptions if they contain spaces.

You can combine commands to update or mark tasks as done directly after adding them.

If Python is not recognized, check that Python is installed and its Scripts folder is in PATH:

C:\Users\<YourUser>\AppData\Local\Programs\Python\Python313\
C:\Users\<YourUser>\AppData\Local\Programs\Python\Python313\Scripts\
