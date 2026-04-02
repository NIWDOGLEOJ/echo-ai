from brain.decision_engine import decide
from core.executor import execute
from memory.recommend import log


def route(command):

    # log command for recommendation engine
    log(command)

    action = decide(command)

    if action:
        execute(action)
        return True

    return False