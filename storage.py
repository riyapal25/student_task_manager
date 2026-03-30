"""
storage.py
----------
Module for loading and saving tasks to a JSON file.
This is the data persistence layer of the Student Task Manager.
"""

import json
import os

# The file where all tasks are stored
TASKS_FILE = "tasks.json"


def load_tasks():
    """
    Load tasks from the JSON file.
    Returns an empty list if the file doesn't exist yet.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """
    Save the current list of tasks to the JSON file.
    Overwrites the file each time to keep data up to date.
    """
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
