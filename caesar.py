def alphabet_position(letter):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter.islower() == True:
        pos = lower.find(letter)
        return pos
    if letter.isupper() == True:
        pos = upper.find(letter)
        return pos

def rotate_character(char, rot):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot = int(rot)

    if char.isalpha() == False:
        return char
    if rot >= 26:
        rot = (rot % 26)
    new_position = alphabet_position(char) + rot
    if char.islower() == True:
        if new_position > 25:
            new_position = new_position - 26
        new_char = lower[new_position]
        return new_char
    if char.isupper() == True:
        if new_position > 25:
            new_position = new_position - 26
        new_char = upper[new_position]
        return new_char

def encrypt(message, rot):
    new_text = ""
    for char in message:
        next_char = rotate_character(char, rot)
        new_text = new_text + next_char
    return new_text
