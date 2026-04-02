from memory.session import store_session, get_last_session

MODES = {

    "development": [
        "Terminal",
        "Safari",
        "Finder"
    ],

    "editing": [
        "Music",
        "Finder",
        "Safari"
    ],

    "learning": [
        "Safari",
        "Notes",
        "Music"
    ],

    # open Games app
    "game": [
        "Games"
    ],

    # special keyword handled by executor
    "private": [
        "__PRIVATE_SAFARI__"
    ]
}

current_mode = None


def enter_mode(name, running_apps):
    global current_mode

    if name not in MODES:
        return None

    # save current session
    store_session(running_apps)

    current_mode = name
    return MODES[name]


def exit_mode():
    global current_mode
    current_mode = None
    return get_last_session()


def get_mode():
    return current_mode