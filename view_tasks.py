"""
view_tasks.py
-------------
Module for displaying tasks in the Student Task Manager.
Contains three view functions:
  - view_all_tasks()    : Show every task
  - view_todays_tasks() : Show tasks due today
  - view_pending_tasks(): Show only pending tasks sorted by priority
"""

from datetime import datetime, date


def view_all_tasks(tasks):
    """
    Display all tasks in a formatted table.
    Shows ID, Title, Category, Priority, Due Date, and Status.
    """
    print("\n--- All Tasks ---")
    if not tasks:
        print("📭 No tasks found. Add some tasks first!")
        return

    print(f"\n{'ID':<5} {'Title':<25} {'Category':<12} {'Priority':<10} {'Due Date':<12} {'Status'}")
    print("-" * 80)

    for task in tasks:
        # Format the due date for display
        due = "No date"
        if task["due_date"]:
            try:
                due = datetime.strptime(task["due_date"], "%Y-%m-%d").strftime("%d-%m-%Y")
            except ValueError:
                due = task["due_date"]

        status_icon = "✅" if task["status"] == "Done" else "⏳"
        print(f"{task['id']:<5} {task['title']:<25} {task['category']:<12} "
              f"{task['priority']:<10} {due:<12} {status_icon} {task['status']}")


def view_todays_tasks(tasks):
    """
    Display only the tasks that are due today.
    Compares task due_date with today's date.
    """
    print("\n--- Today's Tasks ---")
    today = date.today().strftime("%Y-%m-%d")
    todays = [t for t in tasks if t["due_date"] == today]

    if not todays:
        print("🎉 No tasks due today!")
        return

    print(f"\n{'ID':<5} {'Title':<25} {'Priority':<10} {'Status'}")
    print("-" * 55)

    for task in todays:
        status_icon = "✅" if task["status"] == "Done" else "⏳"
        print(f"{task['id']:<5} {task['title']:<25} {task['priority']:<10} {status_icon} {task['status']}")


def view_pending_tasks(tasks):
    """
    Display only pending (not yet done) tasks.
    Tasks are sorted by priority: High → Medium → Low.
    This helps students know what to focus on first.
    """
    print("\n--- Pending Tasks ---")

    # Define sort order for priorities
    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    # Filter and sort pending tasks
    pending = [t for t in tasks if t["status"] == "Pending"]
    pending.sort(key=lambda x: priority_order.get(x["priority"], 4))

    if not pending:
        print("🎉 No pending tasks! You're all caught up.")
        return

    print(f"\n{'ID':<5} {'Title':<25} {'Category':<12} {'Priority':<10} {'Due Date'}")
    print("-" * 65)

    for task in pending:
        due = "No date"
        if task["due_date"]:
            try:
                due = datetime.strptime(task["due_date"], "%Y-%m-%d").strftime("%d-%m-%Y")
            except ValueError:
                due = task["due_date"]
        print(f"{task['id']:<5} {task['title']:<25} {task['category']:<12} {task['priority']:<10} {due}")
