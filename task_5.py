def cipher(text, shift):
    result =""
    shift = shift % 26
    for letter in text:
        if letter == " ":
            result += letter
        elif letter.isupper():
            if ord(letter) + shift > ord('Z'):
                    result += chr(ord(letter) + shift - 26)
            elif ord (letter) + shift > ord('z'):
                result += chr(ord(letter) + shift - 26)
        else :
            result += chr(ord(letter) + shift)
    return result
def decipher(text, shift):
    result = ""
    for letter in text:
        if letter == " ":
            result += letter
        elif ord(letter) - shift < ord('A') and ord(letter) < 97:
            result += chr(ord(letter) - shift + 26)
        elif ord(letter) - shift < ord('a') and ord(letter) > 97:
            result += chr(ord(letter) - shift + 26)
        else:
            result += chr(ord(letter) - shift)
    return result
