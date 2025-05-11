#!/usr/bin/env python3

import sys
import random
import secrets
import string

def password_generator(length, complexity, symbols):
    password = ""
    match complexity:
        case 1:
            # making password with alphabet letters
            for i in range(length):
                alphabet = string.ascii_letters
                password += secrets.choice(alphabet)
        case 2:
            # making password with alphabet and numbers
            for i in range(length):
                alphanums = string.ascii_letters + string.digits
                password += secrets.choice(alphanums)
        case 3:
            # initializing objects
            ind_dict = {}
            ind_list = list(range(length))
            random.shuffle(ind_list)

            # adding random index with symbol into dictionary
            for s in symbols:
                ind_dict[ind_list.pop()] = s

            # making password with symbol dictionary
            for i in range(length):
                if i in ind_dict:
                    password += ind_dict[i]
                else:
                    alphanums = string.ascii_letters + string.digits
                    password += secrets.choice(alphanums)


    print("Password generated: " + password)



def usage_print():
    print("wrong input (input is empty or wrong values inserted), try again")

if __name__ == "__main__":
    # reading default settings input
    def_status = input("use default settings (length: 20, complexity: 3, symbols: _-)? y/n ")
    if ("y" in def_status or len(def_status) == 0):
        password_generator(20, 3, "_-")
        exit(0)
    elif (not "n" in def_status):
        usage_print()
        exit(1)


    # reading length input
    len_inp = input("insert password length: ")
    if (not len_inp.isnumeric() or len(len_inp) == 0):
        usage_print()
        exit(1)
    length = int(len_inp)

    # reading complexity input
    comp_inp = input("insert complexity value (1 - simple (only letters), 2 - medium (letters with numbers), 3 - hard (letters, numbers and symbols)): ")
    if (not comp_inp.isnumeric() or len(comp_inp) == 0):
        usage_print()
        exit(1)
    complexity = int(comp_inp)
    if (complexity < 1 or complexity > 3):
        usage_print()
        exit(1)

    # calling password generator early if no high complexity requested
    if (complexity != 3):
        password_generator(length, complexity, "")
        exit(0)

    # reading symbols input
    symbols = input("insert symbols included in password: ")
    if (len(symbols) == 0):
        usage_print()
        exit(1)
    if (len(symbols) > length / 2):
        print("wrong input (length of symbols appears too large), try again")
        exit(1)
    for letter in symbols:
        if (letter.isalpha() or letter.isnumeric()):
            print("wrong input (letters and numbers shouldn't be included), try again")
            exit(1)


    #calling password generator
    if (length < 8):
        print("warning! password length appears too small, consider making larger size")
    password_generator(length, complexity, symbols)
