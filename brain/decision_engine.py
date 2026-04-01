from brain.layer1_rules import match_rule
from brain.layer2_bitnet import parse_intent
from brain.layer3_llama import reason


def decide(command):

    # Layer 1
    action = match_rule(command)
    if action:
        return action

    # Layer 2
    action = parse_intent(command)
    if action:
        return action

    # Layer 3 reasoning
    new_command = reason(command)

    if new_command:

        print("Layer3 interpreted:", new_command)

        # try layer1 again
        action = match_rule(new_command)
        if action:
            return action

        # try layer2 again
        action = parse_intent(new_command)
        if action:
            return action

    return None