"""
delete_task.py
--------------
Module for deleting a task from the Student Task Manager.
User selects a task by ID and confirms before it is removed.
"""

from storage import save_tasks
from view_tasks import view_all_tasks


def delete_task(tasks):
    """
    Delete a task permanently by its ID.

    Steps:
    1. Show all tasks so the user can pick the right ID.
    2. Ask the user to enter the task ID.
    3. Ask for confirmation before deleting.
    4. Remove the task and save the updated list.
    """
    print("\n--- Delete Task ---")

    # Show current tasks so user can choose
    view_all_tasks(tasks)

    if not tasks:
        return  # Nothing to delete if list is empty

    try:
        task_id = int(input("\nEnter Task ID to delete: "))

        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                # Ask for confirmation before deleting
                confirm = input(f"Are you sure you want to delete '{task['title']}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    tasks.pop(i)
                    save_tasks(tasks)
                    print("🗑️  Task deleted successfully.")
                else:
                    print("Deletion cancelled.")
                return

        print("❌ Task ID not found.")

    except ValueError:
        print("❌ Please enter a valid number.")
