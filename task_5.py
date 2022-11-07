def cipher(text, shift):
    result =""
    for letter in text:
        if letter == " ":
            result += letter
        elif ord(letter) + shift > 90 and ord(letter) < 97:
            result += chr(65 - 90 + ord(letter) + shift)
        elif ord(letter) + shift > 122 and ord(letter) > 97:
            result += chr(97 - 122 + ord(letter) + shift)
        else :
            result += chr(ord(letter) + shift)
    return result
def decipher(text, shift):
    result = ""
    for letter in text:
        if letter == " ":
            result += letter
        elif ord(letter) - shift < 65 and ord(letter) < 97:
            result += chr(90 - 65 + ord(letter) - shift)
        elif ord(letter) - shift < 97 and ord(letter) > 97:
            result += chr(122 - 97 + ord(letter) - shift)
        else:
            result += chr(ord(letter) - shift)
    return result


print(cipher("Imperator", 1))
print(decipher("Jnqfsbups", 1))
