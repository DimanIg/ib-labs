import string

class Enigma:
    def __init__(self, setting):
        self.setting = setting
        self.alphabet = string.ascii_letters

    def encode(self, message):
        encoded_message = ''
        for char in message:
            if char in self.alphabet:
                encoded_char = self.alphabet[(self.alphabet.index(char) + self.setting)]
                encoded_message += encoded_char
            else:
                encoded_message += char
        return encoded_message

    def decode(self, message):
        decoded_message = ''
        for char in message:
            if char in self.alphabet:
                decoded_char = self.alphabet[(self.alphabet.index(char) - self.setting)]
                decoded_message += decoded_char
            else:
                decoded_message += char
        return decoded_message

# Пример использования
enigma = Enigma(3)
msg = input('Введите сообщение на английском: ')
encoded = enigma.encode(msg)
print(f'Зашифрованное сообщение: {encoded}')
decoded = enigma.decode(encoded)
print(decoded)