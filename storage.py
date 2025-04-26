# storage.py

import json
import os

FILE_PATH = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE_PATH, "w") as file:
        json.dump(contacts, file, indent=4)
