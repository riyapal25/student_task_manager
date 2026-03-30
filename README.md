# Student Task Manager

A command-line Python application that helps students track assignments, exams, projects, and personal tasks all in one place.

---

## The Problem

As a student, tasks are scattered everywhere like WhatsApp messages, notebooks, sticky notes, and memory. There is no single place to track them, and things slip through the cracks. This app solves that by giving you a simple, organized task manager right in your terminal.

---

## Features

- ➕ **Add tasks** with title, category, priority, and due date
- 📋 **View all tasks** in a formatted table
- 📅 **View today's tasks** — see what's due today
- ⏳ **View pending tasks** — sorted by priority (High → Medium → Low)
- ✅ **Mark tasks as done**
- 🗑️ **Delete tasks**
- 📊 **Summary report** — pending vs done, by category and priority
- 💾 **Persistent storage** — tasks are saved to a `tasks.json` file

---

## Project Structure

```
student_task_manager/
│
├── main.py          # Entry point — menu & calls all modules
├── storage.py       # load_tasks() and save_tasks() — JSON file handling
├── add_task.py      # add_task() — collect and save a new task
├── view_tasks.py    # view_all_tasks(), view_todays_tasks(), view_pending_tasks()
├── mark_done.py     # mark_done() — update task status to Done
├── delete_task.py   # delete_task() — remove a task by ID
└── summary.py       # show_summary() — stats and overview
```

Each feature is separated into its own module (file) and imported into `main.py`. This follows the **modular programming** principle.

---

## Requirements

- Python 3.x
- No external libraries needed — uses only Python's built-in modules:
  - `json`
  - `os`
  - `datetime`

---

## How to Run

### Run the program
```bash
python main.py
```

> If `python` doesn't work, try `python3 main.py`

---

## How to Use

When you run the program, you will see this menu:

```
=============================================
       🎓 STUDENT TASK MANAGER
=============================================
  1. ➕  Add New Task
  2. 📋  View All Tasks
  3. 📅  View Today's Tasks
  4. ⏳  View Pending Tasks
  5. ✅  Mark Task as Done
  6. 🗑️   Delete a Task
  7. 📊  Summary
  0. 🚪  Exit
=============================================
```

Enter a number (0–7) to choose an option.

### Adding a Task (Option 1)
You will be asked to enter:
- **Title** — e.g., `Submit Python Assignment`
- **Category** — Assignment / Exam / Project / Personal
- **Priority** — High / Medium / Low
- **Due Date** — in DD-MM-YYYY format (optional)

### Viewing Tasks (Options 2, 3, 4)
- Option 2 shows all tasks
- Option 3 shows only tasks due today
- Option 4 shows pending tasks sorted by priority

### Summary (Option 7)
Shows total tasks, done count, pending count, overdue count, and a breakdown by category and priority.

### Screenshots

<img width="1138" height="710" alt="Screenshot 2026-03-30 220439" src="https://github.com/user-attachments/assets/db56aabe-0881-426f-a0fb-dd2d873303a2" />

<img width="1080" height="460" alt="Screenshot 2026-03-30 220542" src="https://github.com/user-attachments/assets/17b2ee2e-e231-4827-83e1-eb65b3be72f4" />

<img width="1068" height="598" alt="Screenshot 2026-03-30 220629" src="https://github.com/user-attachments/assets/311ccd48-f1a7-4f83-a1e7-42488df46c27" />

<img width="1085" height="445" alt="Screenshot 2026-03-30 220830" src="https://github.com/user-attachments/assets/3bfbac46-a7d2-4a2e-9a1a-f64d6e55999b" />

---

## Data Storage

All tasks are automatically saved to a file called `tasks.json` in the same folder. This means your tasks are preserved even after you close and reopen the program.

---

## Python Concepts Used

| Concept | Where Used |
|---|---|
| Functions | Every module |
| Modules & Imports | `main.py` imports from all other files |
| Lists & Dictionaries | Task storage and manipulation |
| File I/O (JSON) | `storage.py` |
| `datetime` module | Due date handling |
| String formatting | Displaying task tables |
| Loops & Conditionals | Menu logic, task filtering |
| Exception Handling | Input validation (`try/except`) |

---

## Author

Riya Pal
