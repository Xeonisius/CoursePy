from simplecrypt import decrypt, DecryptionException

with open("C:\\path\\encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("C:\\path\\passwords.txt", "r") as pwd_file:
    passwords = pwd_file.read().splitlines()

for password in passwords:
    try:
        decrypted = decrypt(password, encrypted)
        print("Пароль:", password)
        print("Расшифрованная информация:", decrypted.decode('utf-8'))
        break
    except DecryptionException:
        continue
    except Exception as e:
        print(f"Произошла ошибка: {e}")
