from brain.decision_engine import decide
from core.executor import execute


def route(command):

    action = decide(command)

    if action:
        execute(action)
        return True

    return False