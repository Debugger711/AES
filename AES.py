import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

iv = pad(b"myiv",AES.block_size)
key = pad(get_random_bytes(16),AES.block_size)
with open ('MasterKey.txt','wb') as mk:
    mk.write(key)
    
def encrypt():
    plaintext = input("Ingrese el texto: ")
    data_bytes=bytes(plaintext, 'utf-8')
    padded_bytes=pad(data_bytes, AES.block_size)
    AES_obj = AES.new(key, AES.MODE_CBC,iv)
    ciphertext=AES_obj.encrypt(padded_bytes)
    with open('Cryptext.key','wb') as fo:
        fo.write(ciphertext)
    return ciphertext

def decrypt():
    nombre = input("nombre del archivo :")
    Nkey = input("nombre de la llave :")
    with open(nombre,'rb') as fo:
        ciphertext = fo.read()
    with open(Nkey,'rb') as lk:
        key = lk.read()
    AES_obj=AES.new(key,AES.MODE_CBC,iv)
    raw_bytes=AES_obj.decrypt(ciphertext)
    extracted_bytes=unpad(raw_bytes,AES.block_size)
    with open('DesCrypt_text.txt','wb') as fa:
        fa.write(extracted_bytes)
    return extracted_bytes


while True:
    
    ans = int(input("1-encriptar\n2-desencriptar\n3-exit"))
    if ans == 1:
        encrypt()
    elif ans == 2:
        decrypt()
    elif ans == 3:
        exit()
    else:
        print("Ingrese una opcion valida")

