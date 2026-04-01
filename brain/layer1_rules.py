# FINAL Layer 1 — Universal App Controller (fixed)

import os

OPEN_WORDS = ["open", "launch", "start", "run"]
CLOSE_WORDS = ["close", "quit", "kill", "stop", "die"]


SEARCH_PATHS = [
    "/Applications",
    "/System/Applications",
    os.path.expanduser("~/Applications"),
]


def find_app(app_name):

    app_name = app_name.lower().strip()

    for path in SEARCH_PATHS:

        if not os.path.exists(path):
            continue

        for app in os.listdir(path):

            if not app.lower().endswith(".app"):
                continue

            clean = app.lower().replace(".app", "")

            # exact match
            if app_name == clean:
                return app

            # contains match
            if app_name in clean:
                return app

            # multi word match
            if all(word in clean for word in app_name.split()):
                return app

    return None


def match_rule(command: str):

    command = command.lower().strip()

    # --------------------------
    # OPEN COMMANDS
    # --------------------------

    for word in OPEN_WORDS:
        if command.startswith(word + " "):

            app_name = command.replace(word, "", 1).strip()
            app = find_app(app_name)

            if app:
                return {
                    "action": "open_app",
                    "value": app
                }

    # --------------------------
    # CLOSE COMMANDS
    # --------------------------

    for word in CLOSE_WORDS:
        if command.startswith(word + " "):

            app_name = command.replace(word, "", 1).strip()
            app = find_app(app_name)

            if app:
                return {
                    "action": "close_app",
                    "value": app
                }

    # --------------------------
    # APP NAME ONLY
    # --------------------------

    app = find_app(command)
    if app:
        return {
            "action": "open_app",
            "value": app
        }

    # --------------------------
    # SCROLL
    # --------------------------

    if "scroll down" in command:
        return {"action": "scroll", "value": -500}

    if "scroll up" in command:
        return {"action": "scroll", "value": 500}

    # --------------------------
    # VOLUME
    # --------------------------

    if "volume up" in command or "increase volume" in command:
        return {"action": "volume", "value": "up"}

    if "volume down" in command or "decrease volume" in command:
        return {"action": "volume", "value": "down"}

    if "mute" in command:
        return {"action": "volume", "value": "mute"}

    # --------------------------
    # WINDOW
    # --------------------------

    if "close window" in command:
        return {
            "action": "hotkey",
            "value": ["command", "w"]
        }

    # screenshot
    if "screenshot" in command:
        return {
            "action": "hotkey",
            "value": ["command", "shift", "3"]
        }

    return None