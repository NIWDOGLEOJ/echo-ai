import json
import os
from collections import Counter

FILE = "memory/recommend.json"


def load():
    if not os.path.exists(FILE):
        return {
            "history": []
        }

    with open(FILE, "r") as f:
        return json.load(f)


def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


def log(command):

    data = load()

    data["history"].append(command)

    # keep last 50
    data["history"] = data["history"][-50:]

    save(data)


def suggest():

    data = load()
    history = data["history"]

    if len(history) < 3:
        return None

    # frequency
    freq = Counter(history)
    top = freq.most_common(1)[0][0]

    return top