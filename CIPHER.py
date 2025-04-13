def ciphertext (text, kay):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - offset - kay) % 26 + offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


text = input("Input the text: ")
print("\nTrying all possible text:\n")
for kay in range(1, 26):
    plain_text = ciphertext (text, kay)
    print (plain_text)
