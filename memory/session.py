import json
import os

SESSION_FILE = "memory/session.json"


def load():

    if not os.path.exists(SESSION_FILE):
        return {
            "last_closed": [],
            "last_session": [],
            "favorites": [],
            "common": ["Safari", "Music", "Notes"]
        }

    with open(SESSION_FILE, "r") as f:
        return json.load(f)


def save(data):
    with open(SESSION_FILE, "w") as f:
        json.dump(data, f)


def store_closed(apps):

    data = load()
    data["last_closed"] = apps
    save(data)


def get_last_closed():
    data = load()
    return data["last_closed"]


def store_session(apps):

    data = load()
    data["last_session"] = apps
    save(data)


def get_last_session():
    data = load()
    return data["last_session"]


def get_favorites():
    data = load()
    return data["favorites"]


def get_common():
    data = load()
    return data["common"]