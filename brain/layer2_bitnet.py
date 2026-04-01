# Layer 2 — Intent Parser (Lightweight)
# Natural language understanding without heavy AI

def parse_intent(command: str):

    command = command.lower().strip()

    # -------------------------
    # CLOSE ALL
    # -------------------------
    if "close everything" in command or "close all" in command or "close all apps" in command:
        return {"action": "close_all"}

    # -------------------------
    # START ALL / REOPEN
    # -------------------------
    if (
        "start all" in command
        or "open all" in command
        or "reopen apps" in command
        or "start all apps" in command
    ):
        return {"action": "start_all"}

    # -------------------------
    # RESTORE SESSION
    # -------------------------
    if "restore session" in command or "restore apps" in command:
        return {"action": "restore_session"}

    # -------------------------
    # FAVORITES
    # -------------------------
    if "favorite apps" in command or "open favorites" in command:
        return {"action": "open_favorites"}

    # -------------------------
    # COMMON APPS
    # -------------------------
    if "common apps" in command or "open common" in command:
        return {"action": "open_common"}

    # -------------------------
    # volume increase
    # -------------------------
    if (
        "increase volume" in command
        or "turn volume up" in command
        or "raise volume" in command
        or "volume higher" in command
    ):
        return {"action": "volume", "value": "up"}

    # -------------------------
    # volume decrease
    # -------------------------
    if (
        "decrease volume" in command
        or "turn volume down" in command
        or "lower volume" in command
    ):
        return {"action": "volume", "value": "down"}

    # -------------------------
    # play music
    # -------------------------
    if "play music" in command:
        return {
            "action": "open_app",
            "value": "Music.app"
        }

    # -------------------------
    # open browser
    # -------------------------
    if "open browser" in command:
        return {
            "action": "open_app",
            "value": "Safari.app"
        }

    # -------------------------
    # open youtube
    # -------------------------
    if "open youtube" in command:
        return {
            "action": "open_url",
            "value": "https://youtube.com"
        }

    # -------------------------
    # search google
    # -------------------------
    if command.startswith("search "):

        query = command.replace("search ", "")
        query = query.replace(" ", "+")

        return {
            "action": "open_url",
            "value": f"https://www.google.com/search?q={query}"
        }

    # -------------------------
    # MODES
    # -------------------------
    if "development mode" in command or "enter development" in command:
        return {"action": "mode", "value": "development"}

    if "editing mode" in command or "enter editing" in command:
        return {"action": "mode", "value": "editing"}

    if "learning mode" in command or "enter learning" in command:
        return {"action": "mode", "value": "learning"}

    if "game mode" in command or "enter game" in command:
        return {"action": "mode", "value": "game"}

    if "private mode" in command or "enter private" in command:
        return {"action": "mode", "value": "private"}

    # exit mode
    if "exit mode" in command or "leave mode" in command:
        return {"action": "exit_mode"}

    return None