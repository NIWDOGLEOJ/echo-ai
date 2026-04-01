import os
import pyautogui
import subprocess

from memory.session import (
    store_closed,
    get_last_closed,
    get_last_session,
    get_favorites,
    get_common
)

from memory.modes import enter_mode, exit_mode


def get_running_apps():

    script = '''
    osascript -e 'tell application "System Events" to get name of (processes where background only is false)'
    '''

    result = subprocess.getoutput(script)
    apps = [a.strip() for a in result.split(",")]

    return apps


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

    # CLOSE ALL (SAFE + STORE)
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

        apps = get_running_apps()

        close_list = []

        for app in apps:

            skip = False
            for p in protected:
                if p.lower() in app.lower():
                    skip = True
                    break

            if skip:
                continue

            close_list.append(app)

            subprocess.Popen(
                ["osascript", "-e", f'tell application "{app}" to quit']
            )

            print(f"Closing {app}")

        store_closed(close_list)

    # START ALL APPS
    elif act == "start_all":

        apps = get_last_closed()

        for app in apps:
            subprocess.Popen(["open", "-a", app])
            print(f"Opening {app}")

    # RESTORE SESSION
    elif act == "restore_session":

        apps = get_last_session()

        for app in apps:
            subprocess.Popen(["open", "-a", app])
            print(f"Restoring {app}")

    # OPEN FAVORITES
    elif act == "open_favorites":

        apps = get_favorites()

        for app in apps:
            subprocess.Popen(["open", "-a", app])
            print(f"Opening {app}")

    # OPEN COMMON
    elif act == "open_common":

        apps = get_common()

        for app in apps:
            subprocess.Popen(["open", "-a", app])
            print(f"Opening {app}")

    # ENTER MODE
    elif act == "mode":

        running = get_running_apps()
        apps = enter_mode(value, running)

        if apps:
            for app in apps:
                subprocess.Popen(["open", "-a", app])
                print(f"Opening {app}")

    # EXIT MODE
    elif act == "exit_mode":

        apps = exit_mode()

        if apps:
            for app in apps:
                subprocess.Popen(["open", "-a", app])
                print(f"Restoring {app}")

    else:
        print("Unknown action:", action)