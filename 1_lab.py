def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

msg = input('Введите сообщение на английском: ')
shift = 3
encrypted_text = encrypt(msg, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("Зашифрованный текст:", encrypted_text)
print("Расшифрованный текст:", decrypted_text)
