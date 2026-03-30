"""
main.py
-------
Main entry point for the Student Task Manager.

This file ties all modules together:
  - storage.py      → load_tasks, save_tasks
  - add_task.py     → add_task
  - view_tasks.py   → view_all_tasks, view_todays_tasks, view_pending_tasks
  - mark_done.py    → mark_done
  - delete_task.py  → delete_task
  - summary.py      → show_summary

Run this file to start the program:
    python main.py
"""

# ── Import functions from each module ─────────────────────────────────────────
from storage      import load_tasks
from add_task     import add_task
from view_tasks   import view_all_tasks, view_todays_tasks, view_pending_tasks
from mark_done    import mark_done
from delete_task  import delete_task
from summary      import show_summary
# ──────────────────────────────────────────────────────────────────────────────


def show_menu():
    """Display the main menu options."""
    print("\n" + "=" * 45)
    print("       🎓 STUDENT TASK MANAGER")
    print("=" * 45)
    print("  1. ➕  Add New Task")
    print("  2. 📋  View All Tasks")
    print("  3. 📅  View Today's Tasks")
    print("  4. ⏳  View Pending Tasks")
    print("  5. ✅  Mark Task as Done")
    print("  6. 🗑️   Delete a Task")
    print("  7. 📊  Summary")
    print("  0. 🚪  Exit")
    print("=" * 45)


def main():
    """
    Main function — runs the menu loop.
    Loads saved tasks at start, then repeatedly shows
    the menu and calls the appropriate module function.
    """
    print("\n🎓 Welcome to Student Task Manager!")
    print("Your personal academic to-do tracker.\n")

    # Load existing tasks from storage.py
    tasks = load_tasks()
    print(f"📂 Loaded {len(tasks)} task(s) from saved data.")

    while True:
        show_menu()
        choice = input("Enter your choice (0-7): ").strip()

        if choice == "1":
            add_task(tasks)           # → add_task.py

        elif choice == "2":
            view_all_tasks(tasks)     # → view_tasks.py

        elif choice == "3":
            view_todays_tasks(tasks)  # → view_tasks.py

        elif choice == "4":
            view_pending_tasks(tasks) # → view_tasks.py

        elif choice == "5":
            mark_done(tasks)          # → mark_done.py

        elif choice == "6":
            delete_task(tasks)        # → delete_task.py

        elif choice == "7":
            show_summary(tasks)       # → summary.py

        elif choice == "0":
            print("\n👋 Goodbye! Stay on top of your tasks!")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 0 and 7.")

        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()
