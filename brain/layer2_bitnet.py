# Layer 2 — Intent Parser (Lightweight)
# Natural language understanding without heavy AI

def parse_intent(command: str):

    command = command.lower().strip()

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
    # close everything
    # -------------------------
    if "close everything" in command or "close all" in command:
        return {
            "action": "close_all"
        }

    return None