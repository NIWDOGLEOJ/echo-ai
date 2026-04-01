from core.router import route
from voice.microphone import listen_continuous


def run():
    print("Echo always listening...")

    while True:
        command = listen_continuous()

        if not command:
            continue

        handled = route(command)

        if not handled:
            print("Echo: command not understood")