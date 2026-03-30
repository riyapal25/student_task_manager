"""
summary.py
----------
Module for displaying a summary report in the Student Task Manager.
Shows overall counts, breakdown by category, and pending by priority.
"""

from datetime import date


def show_summary(tasks):
    """
    Display a summary of all tasks including:
    - Total, Done, Pending, and Overdue counts
    - Breakdown by category (Assignment / Exam / Project / Personal)
    - Pending tasks grouped by priority with a visual bar
    """
    print("\n--- Task Summary ---")

    if not tasks:
        print("📭 No tasks to summarize.")
        return

    # --- Overall counts ---
    total   = len(tasks)
    done    = sum(1 for t in tasks if t["status"] == "Done")
    pending = total - done

    # Count overdue tasks (pending + due date already passed)
    today = date.today().strftime("%Y-%m-%d")
    overdue = sum(
        1 for t in tasks
        if t["due_date"] and t["due_date"] < today and t["status"] == "Pending"
    )

    print(f"\n📊 Overall:")
    print(f"   Total Tasks  : {total}")
    print(f"   ✅ Done      : {done}")
    print(f"   ⏳ Pending   : {pending}")
    print(f"   🚨 Overdue   : {overdue}")

    # --- Breakdown by category ---
    categories = ["Assignment", "Exam", "Project", "Personal"]
    print(f"\n📁 By Category:")
    for cat in categories:
        cat_tasks = [t for t in tasks if t["category"] == cat]
        if cat_tasks:
            cat_done    = sum(1 for t in cat_tasks if t["status"] == "Done")
            cat_pending = len(cat_tasks) - cat_done
            print(f"   {cat:<12}: {len(cat_tasks)} total, {cat_done} done, {cat_pending} pending")

    # --- Pending tasks by priority with a visual bar ---
    print(f"\n🔥 Pending by Priority:")
    for pri in ["High", "Medium", "Low"]:
        count = sum(1 for t in tasks if t["priority"] == pri and t["status"] == "Pending")
        bar = "█" * count
        print(f"   {pri:<8}: {bar} ({count})")
