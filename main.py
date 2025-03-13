import click
import datetime
from tabulate import tabulate
from model import User, Task, Category, session

@click.group()
def cli():
    """Task Manager CLI"""
    pass

@cli.command()
@click.argument("name")
@click.argument("email")
def add_user(name, email):
    """Add a new user"""
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    click.echo(f"User '{name}' added successfully!")

@cli.command()
def list_users():
    """List all users"""
    users = session.query(User).all()
    table = [[u.id, u.name, u.email] for u in users]
    click.echo(tabulate(table, headers=["ID", "Name", "Email"]))

@cli.command()
@click.argument("name")
def add_category(name):
    """Add a new category"""
    category = Category(name=name)
    session.add(category)
    session.commit()
    click.echo(f"Category '{name}' added successfully!")

@cli.command()
def list_categories():
    """List all categories"""
    categories = session.query(Category).all()
    table = [[c.id, c.name] for c in categories]
    click.echo(tabulate(table, headers=["ID", "Category"]))

@cli.command()
@click.argument("title")
@click.argument("user_id", type=int)
@click.option("--description", "-d", help="Task description")
@click.option("--due", "-du", type=click.DateTime(formats=["%Y-%m-%d"]), help="Due date (YYYY-MM-DD)")
@click.option("--priority", "-p", type=click.Choice(["Low", "Medium", "High"]), default="Medium", help="Priority level")
@click.option("--category_id", "-c", type=int, help="Category ID")
def add_task(title, user_id, description, due, priority, category_id):
    """Add a new task"""
    task = Task(title=title, description=description, due_date=due, priority=priority, user_id=user_id, category_id=category_id)
    session.add(task)
    session.commit()
    click.echo(f"Task '{title}' added successfully!")

@cli.command()
@click.option("--user_id", type=int, help="Filter by user")
@click.option("--category_id", type=int, help="Filter by category")
@click.option("--status", type=click.Choice(["all", "completed", "pending"]), default="all", help="Filter by status")
def list_tasks(user_id, category_id, status):
    """List tasks"""
    query = session.query(Task)
    
    if user_id:
        query = query.filter(Task.user_id == user_id)
    if category_id:
        query = query.filter(Task.category_id == category_id)
    if status == "completed":
        query = query.filter(Task.completed == True)
    elif status == "pending":
        query = query.filter(Task.completed == False)

    tasks = query.all()
    if not tasks:
        click.echo("No tasks found.")
        return

    table = [[t.id, t.title, t.priority, t.due_date, "✅" if t.completed else "❌", t.user_id, t.category_id] for t in tasks]
    click.echo(tabulate(table, headers=["ID", "Title", "Priority", "Due Date", "Status", "User ID", "Category ID"]))

@cli.command()
@click.argument("task_id", type=int)
@click.option("--title", help="New title")
@click.option("--description", "-d", help="New description")
@click.option("--due", "-du", type=click.DateTime(formats=["%Y-%m-%d"]), help="New due date")
@click.option("--priority", "-p", type=click.Choice(["Low", "Medium", "High"]), help="New priority")
@click.option("--complete", is_flag=True, help="Mark as complete")
@click.option("--user_id", type=int, help="Change assigned user")
@click.option("--category_id", type=int, help="Change category")
def update_task(task_id, title, description, due, priority, complete, user_id, category_id):
    """Update a task"""
    task = session.query(Task).get(task_id)
    if not task:
        click.echo("Task not found!")
        return

    if title:
        task.title = title
    if description:
        task.description = description
    if due:
        task.due_date = due
    if priority:
        task.priority = priority
    if complete:
        task.completed = True
    if user_id:
        task.user_id = user_id
    if category_id:
        task.category_id = category_id

    session.commit()
    click.echo(f"Task {task_id} updated successfully!")

@cli.command()
@click.argument("task_id", type=int)
def delete_task(task_id):
    """Delete a task"""
    task = session.query(Task).get(task_id)
    if not task:
        click.echo("Task not found!")
        return

    session.delete(task)
    session.commit()
    click.echo(f"Task {task_id} deleted successfully!")

if __name__ == "__main__":
    cli()


