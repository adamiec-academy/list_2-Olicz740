text ="Ala (nie) ma kota"
def remove_parentheses(text):
    result = ""
    spacebar = False
    is_inside = False
    for letter in text:
        if letter == "(":
            is_inside = True
            result = result
        elif letter == ")":
            is_inside = False
            spacebar = True
        elif spacebar:
            result = result
            spacebar = False
        elif not is_inside:
            result += letter

    return result


print(remove_parentheses(text))
