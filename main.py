print("""
    .+yhddddyo-     mdddddddhs/`    +ddm. /dddy.      dddd
  -hmmmmmmmmmmmd/   mmmmmmmmmmmms`  ommN. +mmmmm:     dmmm
 +mmmd+/Nmm-/hmmms  mmmy   `:smmmd- ommN. +mmmmmms`   dmmm
-mmmh` .Nmm  `ymmm/ mmmy     -mmmd  ommN. +mmmhmmmh.  dmmm
+mmm/  .Nmm   .Nmms mmmy      ymmN` ommN. +mmm:/mmmm/ dmmm
:mmms  .Nmm   +mmmo mmmy     `dmmm` ommN. +mmm: .hmmmsmmmm
 ymmmy-.Nmm` .smmmd`mmmy    `:hmmm/ ommN. +mmm:  `ommmmmmm
  `ommmmdmmmdmmmms` mmmdyyyhdmmmd:  ommN. +mmm:    :dmmmmm
   .+ydmmmmmdho.    mmmmmmmmmhs/`   ommN. +mmm:     .ymmmm
      `.---.``      --------``      .---` `---`      `---- """)
print("Version: 1.0.0")
print("Copyright@2020 ODIN Cryptography")
print('''
CIPHER SELECTION MENU
1. Caesar {E/D/B}
2. Morse {E/D}
3. Vigenere {E/D}''')


def recursion():
    global Choice
    re = input("Do you want to Run Code again {y/n}: ")
    if re.casefold() == 'y':
        Choice = True
    elif re.casefold() == 'n':
        Choice = False
    else:
        print("Wrong Input")
        recursion()


Choice = True
while Choice:
    cipher = input("Enter the number For CIPHER: ")

    if cipher == "1" or cipher == "1.":
        from Ciphers.Caesar import *

        print("""
    Welcome to ODIN/Caesar
    1. Encrypt
    2. Decrypt
    3. BruteForce""")
        x = input("Enter Your Choice: ")
        if x == '1' or x == '1.':
            t = input("Enter The Text You Want To Encrypt: ")
            print('')
            print('+ --> right shift')
            print('- --> left shift')
            s = int(input("Enter the Shift: "))
            encryption = encrypt(t, s)
            print('Encryption: ', encryption)

        elif x == '2' or x == '2.':
            t = input("Enter The Text You Want to Decrypt: ")
            print('')
            print('+ --> right shift')
            print('- --> left shift')
            s = int(input("Enter the Code: "))
            decryption = decrypt(t, s)
            print('Decryption: ', decryption)

        elif x == '3' or x == '3.':
            t = input("Enter The Text You Want to Decrypt: ")
            Decryption = brute_force(t)
            print(Decryption)

        else:
            print("Wrong input")

    elif cipher == "2" or cipher == "2.":
        from Ciphers.Morse import *

        print("""
        Welcome to ODIN/Morse
        1. Encrypt
        2. Decrypt""")
        x = input("Enter your Choice: ")
        if x == '1' or x == '1.':
            t = input("Enter The Text You Want to Encrypt: ")
            encryption = encrypt(t)
            print('Encryption: ', encryption)

        elif x == '2' or x == '2.':
            print('2 spaces --> letter gap')
            print('5 spaces --> Word gap')
            print('While Copying be wary of extra gaps between code and input and in the end\nBetter typed by hand')
            print(' ')
            t = input("Enter The Text You Want to Decrypt: ")
            decryption = decrypt(t)
            print('Decryption: ', decryption)
        else:
            print("Wrong input")

    if cipher == "3" or cipher == "3.":
        from Ciphers.Vigenere import *

        print("""
    Welcome to ODIN/Vigenere
    1. Encrypt
    2. Decrypt""")
        x = input("Enter your Choice: ")
        if x == '1' or x == '1.':
            t = input("Enter The Text You Want to Encrypt: ")
            k = input("Enter The Key: ")
            encryption = encrypt(t, k)
            print('Encryption: ', encryption)
        elif x == '2' or x == '2.':
            t = input("Enter The Text You Want to Decrypt(NO SPACES): ")
            k = input("Enter the Key: ")
            decryption = decrypt(t, k)
            print('Decryption: ', decryption)
        else:
            print('wrong input')
    recursion()
