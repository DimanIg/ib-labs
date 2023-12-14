def leftrotate(i, n):
    return (i << n) | (i >> (32 - n))

def rightrotate(i, n):
    return (i >> n) | (i << (32 - n))

def rc5_encrypt_block(plaintext, key, rounds, wordsize, keysize):
    # Constants
    P = 0xB7E15163
    Q = 0x9E3779B9
    mod = 2**wordsize

    # Key expansion
    L = [int.from_bytes(key[i:i+4], byteorder='little') for i in range(0, keysize, 4)]
    c = (keysize + 3) // 4
    t = 2 * (rounds + 1)
    S = [0] * t
    S[0] = P
    for i in range(1, t):
        S[i] = (S[i-1] + Q) % mod

    i = j = x = y = 0
    A = B = 0
    A = int.from_bytes(plaintext[:4], byteorder='little')
    B = int.from_bytes(plaintext[4:], byteorder='little')

    A = (A + L[0]) % mod
    B = (B + L[1]) % mod

    for _ in range(rounds):
        A = (A ^ B)
        A = (A + x) % mod
        A = (A * 3) % mod

        B = (B ^ A)
        B = (B + y) % mod
        B = (B * 3) % mod

    return A.to_bytes(4, byteorder='little') + B.to_bytes(4, byteorder='little')

# Пример использования
plaintext = input("Введите текст: ").encode()
key = input("Введите ключ: ").encode()

ciphertext = rc5_encrypt_block(plaintext, key, rounds=12, wordsize=32, keysize=len(key))

print("Исходный текст:", plaintext)
print("Зашифрованный текст:", ciphertext)