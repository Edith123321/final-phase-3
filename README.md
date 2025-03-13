# final-phase-3
# Task Manager CLI

## Overview
Task Manager CLI is a command-line interface application that allows users to manage tasks, categories, and users efficiently. It provides functionalities for adding, listing, updating, and deleting tasks, as well as managing users and categories.

## Features
- Add and list users
- Add and list categories
- Add, list, update, and delete tasks
- Filter tasks by user, category, and status

## Requirements
- Python 3.8+
- SQLAlchemy
- Alembic
- Click
- Tabulate

## Installation

### Clone the repository
```bash
git clone https://github.com/your-username/task-manager-cli.git
cd task-manager-cli
```
### Set up the virtual environment
``` bash
python3 -m venv venv
source venv/bin/activate 
```
### Install dependencies
``` bash
pip install -r requirements.txt
```
### Set up the database
``` bash
alembic upgrade head
```

## Usage

### Add a user
``` bash 
python main.py add-user <name> <email>
```
### List all users
``` bash
python main.py list-users
```
### Add a category
``` bash
python main.py add-category <category_name>
```
### List all categories
``` bash
python main.py list-categories

```

### List all tasks
``` bash
python main.py list-tasks [--user_id <user_id>] [--category_id <category_id>] [--status <status>]
```

### Update a task
``` bash 
python main.py update-task <task_id> [--title <new_title>] [--description <new_description>] [--due <new_due_date>] [--priority <new_priority>] [--complete] [--user_id <new_user_id>] [--category_id <new_category_id>]
```
 ### Delete a task
 ``` bash
 python main.py delete-task <task_id>
 ```

 ## License
 This project is licensed under the MIT License 

## Acknowledgments

- **SQLAlchemy** for ORM and database management
- **Alembic** for database migrations
- **Click** for building the command-line interface
- **Tabulate** for displaying data in a tabular format


