def character_shift(text, shift): #text yang mau di enkripsi, jumlah pergeseran karakter
    result = "" #variabel kosong untuk menyimpan hasil enkripsi
    for char in text: #membaca setiap karakter dalam teks
        new_char = chr((ord(char) + shift) % 256) #ord mengubah karakter menjadi ASCII, kemudian ditambahkan dengan shift, dan diambil modulus 256 untuk memastikan tetap dalam rentang karakter ASCII
        result += new_char #pergeseran karakter, caesar cipher
    return result #mengembalikan hasil enkripsi

def xor_encryption(text, key): #text yang mau di enkripsi, kunci untuk XOR
    result = "" #variabel kosong untuk menyimpan hasil enkripsi
    for i in range(len(text)): #membaca setiap teks berdasarkan indeks
        new_char = chr(ord(text[i]) ^ ord(key[i % len(key)])) #ord mengubah karakter menjadi ASCII, kemudian dilakukan operasi XOR dengan karakter dari kunci yang diulang jika panjang teks lebih dari kunci
        result += new_char #menambahkan karakter hasil XOR ke hasil enkripsi
    return result #mengembalikan hasil enkripsi

def reverse_text(text): #text yang mau di enkripsi
    return text[::-1] #mengembalikan teks yang dibalik

def encrypt_dxlc(plaintext, key): #plaintext yang mau di enkripsi, kunci untuk XOR
    step1 = character_shift(plaintext, 3) #langkah pertama: pergeseran karakter dengan Caesar cipher
    step2 = xor_encryption(step1, key) #langkah kedua: enkripsi XOR dengan kunci
    ciphertext = reverse_text(step2) #langkah ketiga: membalik teks hasil XOR
    return ciphertext #mengembalikan hasil enkripsi akhir

def decrypt_dxlc(ciphertext, key): #ciphertext yang mau di dekripsi, kunci untuk XOR
    step1 = reverse_text(ciphertext) #langkah pertama: membalik teks ciphertext
    step2 = xor_encryption(step1, key) #langkah kedua: dekripsi XOR dengan kunci (sama dengan enkripsi karena XOR bersifat simetris)
    plaintext = character_shift(step2, -3) #langkah ketiga: pergeseran karakter dengan Caesar cipher (negatif untuk dekripsi)
    return plaintext #mengembalikan hasil dekripsi akhir

def main():
    while True:
        print("\n=== DXLC Log Encryption App ===")
        print("1. Encrypt Log")
        print("2. Decrypt Log")
        print("3. Exit")

        choice = input("Choose menu: ")

        if choice == "1":
            log = input("Input log: ")
            key = input("Input key: ")
            encrypted = encrypt_dxlc(log, key)
            encrypted_hex = encrypted.encode().hex()
            print("Ciphertext (hex):", encrypted_hex)

        elif choice == "2":
            cipher_hex = input("Ciphertext (hex): ")
            key = input("Input key: ")
            cipher = bytes.fromhex(cipher_hex).decode()
            decrypted = decrypt_dxlc(cipher, key)
            print("Plaintext:", decrypted)

        elif choice == "3":
            break

        else:
            print("Invalid menu")
if __name__ == "__main__":
    main()