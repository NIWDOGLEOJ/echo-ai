import os
import pyautogui
import subprocess


def execute(action):

    if action is None:
        return

    act = action.get("action")
    value = action.get("value")

    # OPEN APP
    if act == "open_app":
        subprocess.Popen(["open", "-a", value])
        print(f"Opening {value}")

    # CLOSE APP
    elif act == "close_app":
        subprocess.Popen(
            ["osascript", "-e", f'tell application "{value}" to quit']
        )
        print(f"Closing {value}")

    # SCROLL
    elif act == "scroll":
        pyautogui.scroll(value)

    # HOTKEY
    elif act == "hotkey":
        pyautogui.hotkey(*value)

    # VOLUME
    elif act == "volume":

        if value == "up":
            os.system(
                "osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'"
            )

        elif value == "down":
            os.system(
                "osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'"
            )

        elif value == "mute":
            os.system("osascript -e 'set volume with output muted'")

    # OPEN URL
    elif act == "open_url":
        subprocess.Popen(["open", value])

    # CLOSE ALL (SAFE)
    elif act == "close_all":

        protected = [
            "Terminal",
            "iTerm",
            "LM Studio",
            "Finder",
            "System Settings",
            "Python",
            "python",
            "WindowServer",
            "Dock",
        ]

        script = '''
        osascript -e 'tell application "System Events" to get name of (processes where background only is false)'
        '''

        result = subprocess.getoutput(script)
        apps = [a.strip() for a in result.split(",")]

        for app in apps:

            skip = False
            for p in protected:
                if p.lower() in app.lower():
                    skip = True
                    break

            if skip:
                continue

            subprocess.Popen(
                ["osascript", "-e", f'tell application "{app}" to quit']
            )

            print(f"Closing {app}")

    else:
        print("Unknown action:", action)