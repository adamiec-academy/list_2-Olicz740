def remove_parentheses(text):
    result = ""
    is_inside = False

    for letter in text:
        if letter == "(":
            is_inside = True
            result = result
        elif letter == ")":
            is_inside = False
        elif not is_inside:
            result += letter

    return result
