import random
import math

def generate_keypair():
    # Pilih dua bilangan prima acak, p dan q
    p = generate_prime_number()
    q = generate_prime_number()

    # Hitung n dan totient(n)
    n = p * q
    totient_n = (p - 1) * (q - 1)

    # Pilih bilangan e yang relatif prima terhadap totient(n)
    e = choose_public_exponent(totient_n)

    # Hitung kunci pribadi d
    d = modular_inverse(e, totient_n)

    return ((n, e), (n, d))

def generate_prime_number():
    # Fungsi ini dapat ditingkatkan untuk menghasilkan bilangan prima yang lebih besar
    return random.choice([i for i in range(50, 200) if is_prime(i)])

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def choose_public_exponent(totient_n):
    # Pilih bilangan acak untuk e yang relatif prima terhadap totient(n)
    while True:
        e = random.randint(2, totient_n - 1)
        if math.gcd(e, totient_n) == 1:
            return e

def modular_inverse(a, m):
    # Hitung invers modular dari a mod m menggunakan Algoritma Extended Euclidean
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(message, public_key):
    n, e = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

def decrypt(cipher_text, private_key):
    n, d = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(decrypted_text)

if __name__ == "__main__":
    public_key, private_key = generate_keypair()
    msg = input("Masukan teks yang ingin di enkripsi: ")
    encrypt_msg = encrypt(msg, public_key)
    print(f"Pesan yang di enkripsi: {encrypt_msg}")
    print(f"Public_Key: {public_key}")
    print(f"Private_key: {private_key}")