"""
mark_done.py
------------
Module for marking a task as completed in the Student Task Manager.
User selects a task by its ID and its status is updated to "Done".
"""

from storage import save_tasks
from view_tasks import view_all_tasks


def mark_done(tasks):
    """
    Mark a specific task as 'Done' by its ID.

    Steps:
    1. Show all tasks so the user can pick the right ID.
    2. Ask the user to enter the task ID.
    3. Find the task and update its status to 'Done'.
    4. Save the updated list.
    """
    print("\n--- Mark Task as Done ---")

    # Show current tasks so user can choose
    view_all_tasks(tasks)

    if not tasks:
        return  # Nothing to mark if list is empty

    try:
        task_id = int(input("\nEnter Task ID to mark as done: "))

        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "Done":
                    print(f"ℹ️  Task '{task['title']}' is already marked as done.")
                else:
                    task["status"] = "Done"
                    save_tasks(tasks)
                    print(f"✅ Task '{task['title']}' marked as done!")
                return

        print("❌ Task ID not found.")

    except ValueError:
        print("❌ Please enter a valid number.")
