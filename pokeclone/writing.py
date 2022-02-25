def validate_input(msg, allowed):
    i = ""
    while i not in allowed:
        i = input(msg)
    return i

def format_choices(choices):
    return " | ".join(choices)
