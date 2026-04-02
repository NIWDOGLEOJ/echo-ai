def parse_intent(command: str):

    command = command.lower().strip()

    # -------------------------
    # CLOSE ALL
    # -------------------------
    if "close all" in command:
        return {"action": "close_all"}

    if "stop all apps" in command:
        return {"action": "close_all"}

    # -------------------------
    # START ALL
    # -------------------------
    if "start all" in command:
        return {"action": "start_all"}

    if "resume last session" in command:
        return {"action": "start_all"}

    if "restore session" in command:
        return {"action": "restore_session"}

    # -------------------------
    # MODES
    # -------------------------
    if "development mode" in command:
        return {"action": "mode", "value": "development"}

    if "editing mode" in command:
        return {"action": "mode", "value": "editing"}

    if "learning mode" in command:
        return {"action": "mode", "value": "learning"}

    if "game mode" in command:
        return {"action": "mode", "value": "game"}

    if "private mode" in command:
        return {"action": "mode", "value": "private"}

    if "go private" in command:
        return {"action": "mode", "value": "private"}

    if "exit mode" in command:
        return {"action": "exit_mode"}

    if "exit development mode" in command:
        return {"action": "exit_mode"}

    # -------------------------
    # FAVORITES
    # -------------------------
    if "favorite apps" in command:
        return {"action": "open_favorites"}

    # -------------------------
    # COMMON
    # -------------------------
    if "common apps" in command:
        return {"action": "open_common"}

    return None