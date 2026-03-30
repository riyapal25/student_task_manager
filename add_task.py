"""
add_task.py
-----------
Module for adding a new task to the Student Task Manager.
Collects task details from the user and saves to the task list.
"""

from datetime import datetime, date
from storage import save_tasks


def add_task(tasks):
    """
    Add a new task by collecting details from the user:
    - Title
    - Category (Assignment / Exam / Project / Personal)
    - Priority (High / Medium / Low)
    - Due Date (optional)

    The task is then appended to the tasks list and saved.
    """
    print("\n--- Add New Task ---")

    # Get task title
    title = input("Task title: ").strip()
    if not title:
        print("❌ Task title cannot be empty.")
        return

    # Get category
    print("Categories: 1) Assignment  2) Exam  3) Project  4) Personal")
    cat_choice = input("Choose category (1-4): ").strip()
    categories = {"1": "Assignment", "2": "Exam", "3": "Project", "4": "Personal"}
    category = categories.get(cat_choice, "Personal")

    # Get priority
    print("Priority: 1) High  2) Medium  3) Low")
    pri_choice = input("Choose priority (1-3): ").strip()
    priorities = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priorities.get(pri_choice, "Medium")

    # Get due date (optional)
    due_date_str = input("Due date (DD-MM-YYYY) or press Enter to skip: ").strip()
    due_date = None
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y").strftime("%Y-%m-%d")
        except ValueError:
            print("⚠️  Invalid date format. Due date skipped.")

    # Build the task dictionary
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "category": category,
        "priority": priority,
        "due_date": due_date,
        "status": "Pending",
        "created_at": date.today().strftime("%Y-%m-%d")
    }

    # Add to list and save
    tasks.append(task)
    save_tasks(tasks)
    print(f"\n✅ Task '{title}' added successfully!")
