import os
import json

DATA_FILE = os.path.join(os.path.dirname(__file__), 'task.json')

def load_tasks():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)