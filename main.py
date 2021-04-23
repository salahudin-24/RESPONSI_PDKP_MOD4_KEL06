from security import separator
from security import encrypt
from security import decrypt
from os import system

## KELOMPOK 6
# Muhammad Salman Alfarisi - 21120120120001
# Rina Santika - 21120120120030
# Salahudin Al Ayubi - 21120120140078
# Wisnu Adi Setianto - 21120120140142

key=6
while True :
    separator()
    print("Program Enkripsi dekripsi Kelompok 6")
    separator()
    PlainOrCipher=input("Masukkan text : ")
    option=int(input("1. Enkripsi\n2. Dekripsi\nPilihan :"))
    if option == 1 :
        result=encrypt(PlainOrCipher,key)
        print('Hasil enkripsi :',result)
    elif option == 2 :
        decryptProcess=decrypt(PlainOrCipher,key)
        result=decryptProcess.decrypt()
        print('Hasil dekripsi :',result)
    else :
        print("Masukan tidak tepat")
    separator()
    input("Tekan enter jika selesai")
    system('cls')

