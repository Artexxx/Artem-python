#!/usr/bin/env python

"""shifr ??????"""
arr1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z', \
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
# make arr_2
arr2 = arr1.copy()


# ???????? arr_2
def cange_arr2():
    """????? ??????? ?? ???? number"""
    for i in range(number):
        arr2.append(arr2[0])
        arr2.remove(arr2[0])


# interfes
print("  1)crupt the text/file")
print("  2)Decrupt text from the file")
print("  3)Decrupt text from the terminal\n")

try:
    ans = int(input("[*]Write the number:\n[number]>"))

    if ans == 1:  # ------------------------------------- crypt the text/file"
        number = int(input("[*]??????? (Key-number) ??? ?????? [0-%s]:" % (str(len(arr1)))))
        cange_arr2()  # ????? ??????? ?? ???? number

        mcg = input("\n[*] Write the text: \n[text]->")

        mcgc = ""
        for i in mcg:
            for j in range(len(arr1)):
                if i in arr1[j]:
                    mcgc += arr2[j]

        print("\n Your crypto_text: " + mcgc + "\n")

        # ???????? ????? ? ???????
        answer = input("\n[*]Save crypted text in file? \n[y/n]->")
        if answer=='y':
            crypt = open("text_crypto.txt", "w")
            crypt.write(mcgc)
            crypt.close()
        else:
            pass

    elif ans == 2:  # ----------------------------------Decrupt text from the file"""
        number = int(input("[*]??????? (Key-number) [0-%s]:" % (str(len(arr1)))))
        cange_arr2()  # ????? ??????? ?? ???? number

        # ???????? ????? ? ??????
        decrypt_r = open("text_crypto.txt", "r")
        read = decrypt_r.read()

        mcgd = ""
        for i in read:
            for j in range(len(arr1)):
                if i == arr2[j]:
                    mcgd += arr1[j]

        print("\n Decrypted_text: " + mcgd + "\n")

        # ???????? ????? ? text?
        answer = input("\n[*]Save decripted text in file? \n[y/n]->")
        if answer == 'y':  # -Yes
            decrypt_w = open("text_decrypt.txt", "w")
            decrypt_w.write(mcgd)
            decrypt_w.closed()
            print("File text_decrypt.txt saved!")
        else:
            pass
        decrypt_r.closed()

    elif ans==3: # -------------------------------Decrypt text from the terminal
        number = int(input("[*]??????? (Key-number) [0-%s]:" % (str(len(arr1)))))
        cange_arr2()  # ????? ??????? ?? ???? number

        mcg = input("\n[*] Write the crypted text: \n[text]->")
        mcgd = ""
        for i in mcg:
            for j in range(len(arr1)):
                if i == arr2[j]:
                    mcgd += arr1[j]
        print("\n Your decrypted_text :"+ mcgd + "\n")

    else:
        print("Number not found!")

except ValueError:
    print("Error! Print only INT numbers!")
