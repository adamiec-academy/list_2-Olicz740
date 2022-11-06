def cipher(text, shift):
    result =""
    for letter in text:
        if letter == " ":
            result += letter
        elif letter == "Z":
            result += chr(ord("A") + shift - 1)
        elif letter == "z":
            result += chr(ord("a") + shift - 1)
        else :
            result += chr(ord(letter) + shift)
    print(result)
def decipher(text, shift):
    result = ""
    for letter in text:
        if letter == " ":
            result += letter
        elif letter == "A":
            result += chr(ord("Z") - shift + 1)
        elif letter == "a":
            result += chr(ord("z") - shift + 1)
        else:
            result += chr(ord(letter) - shift)
    print(result)

cipher("Imperator", 1)
decipher("Jnqfsbups", 1)
