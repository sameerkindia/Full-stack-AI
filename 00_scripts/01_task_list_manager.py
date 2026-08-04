import os
TASK_FILE = 'tasks.txt'

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding='utf-8') as f:
            for line in f:
               text, status = line.strip().rsplit('||', 1)
               tasks.append({"text" : text, "done": status == "done"})

    return tasks



def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']} || {status}\n")


def display_tasks(tasks):
    if not tasks:
        print(f"NO tasks found")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()