# task_manager.py
# Task Manager Application Project

# Task Manager
This is a simple command-line task manager application written in Python. It allows users to register, log in, and perform various actions based on their user type (regular user or admin). Users can add tasks, view all tasks, view their own tasks, and admins can also register new users and view task statistics.

# Getting Started
## Prerequisites
- Python 3.x
## Setup
a. Clone the repository:
bash
Copy code
git clone https://github.com/your-username/task_manager.git
cd task_manager.
b. Place the user.txt file in the same directory as task_manager.py. The user.txt file should contain existing user credentials in the format username, password.
c. Place the **'tasks.txt'** file in the same directory as **'task_manager.py'**. The **'tasks.txt'** file should contain existing         tasks in the format **'assigned_to, task, task_description, assigned_date, due_date, task_status'**.

## Usage
- To run the task manager application, execute the following command in the terminal:
bash,
Copy code,
python task_manager.py.

## Features
### 1.User Login:
- Users are prompted to enter their username and password to log in.
- Regular users can view their tasks and add new tasks.
- Admin users can view all tasks, view their tasks, add new tasks, register new users, and view task statistics.

### 2.Add Task:
- Users (both regular and admin) can add new tasks to the system.
- When adding a task, the user needs to provide the username of the person the task is assigned to, a task title, description, assigned 
  date, due date, and task status (completed or not).

### 3.View All Tasks:
- Admin users can view all the tasks in the system.
- Tasks are displayed in a formatted manner, showing details such as assigned username, task title, description, assigned date, due 
  date, and task status.

### 4.View My Tasks:
- Users (both regular and admin) can view their own tasks.
- Tasks are displayed in a formatted manner, showing details such as assigned username, task title, description, assigned date, due 
  date, and task status.

### 5. Register New User (Admin Only):
- Admin users can register new users by providing a username and password.
- The new user's credentials are added to the **'user.txt'** file.
 
### 6. Task Statistics (Admin Only):
- Admin users can view task statistics, including the total number of tasks and the total number of registered users.

### 7. Exit:
- Users can exit the application by selecting the 'e' option from the menu.

## Example Usage:
sql,
Copy code,
Please enter your username: admin,
Please enter your password: adminpass.

**Select one of the following Options below:**
- r - Registering a user
- a - Adding a task
- va - View all tasks
- vm - view my task
- ds - display statistics
- e - Exit
: a

Please enter the username of the person whom the task is assigned to: john_doe
Please enter a title of the task: Complete Project Report
Please enter the description of the task: Write a detailed report on the project progress.
Please enter the due date of the task: 2023-08-15
Please indicate if the task has been completed or not? not completed

Task added successfully.

**Select one of the following Options below:**
- r - Registering a user
- a - Adding a task
- va - View all tasks
- vm - view my task
- ds - display statistics
- e - Exit
: vm

————————————————————————

Assigned to:     john_doe
Task:            Complete Project Report
Description:     Write a detailed report on the project progress.
Assigned Date:   2023-07-27
Due Date:        2023-08-15
Task Status:     not completed

————————————————————————

**Select one of the following Options below:**
- r - Registering a user
- a - Adding a task
- va - View all tasks
- vm - view my task
- ds - display statistics
- e - Exit
: e

**Goodbye!!!**

