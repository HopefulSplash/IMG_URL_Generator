import urllib.request
import webbrowser
import random
import os

from colorama import Fore, Back, Style

#alphabet combo maker
def print_Alphabet(option):
    results = {}
    count = 0
    alphabet = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z'
    }

    #for testing but will make the combo for the alphabet chars
    if option == "Yes":
        for key, value in alphabet.items():
            for key1, value1 in alphabet.items():
                count = count + 1
                results.update({count: value+value1})
    else:
        print(option, "No Print Required")

    return results

#number comba generator
def print_Numbers(option):

    results = {}
    count = 0
    numbers = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9
    }
    #for testing but will make the list of numbers - 4 digits
    if option == "Yes":
        for key, value in numbers.items():
            for key1, value1 in numbers.items():
                for key2, value2 in numbers.items():
                    for key3, value3 in numbers.items():
                        count = count + 1
                        result_String = str(value)
                        result_String1 = str(value1)
                        result_String2 = str(value2)
                        result_String3 = str(value3)
                        four_digit_int = (result_String + result_String1 + result_String2 + result_String3)
                        results.update({count: four_digit_int})

    else:
        print(option, "No Print Required")

    return results

#combines both the alphabet and number combos
def print_Search(letter_Combo, number_Combo):

    results = {}
    count = 0

    for letter_Combo_Key, letter_Value in letter_Combo.items():
        for number_Combo_Key, number_Value in number_Combo.items():
            #print(letter_Value + number_Value)
            count = count + 1
            results.update({count: letter_Value + number_Value})

    return results
#random URL opens for testing a variety of links
def open_Random(search_Links):
    webbrowser.open_new_tab('https://prnt.sc/' + search_Links[random.randrange(0, len(search_Links.items()))])


if __name__ == '__main__':

    letter_Combo = print_Alphabet('Yes')
    #print(letter_Combo)

    number_Combo = print_Numbers('Yes')
    #print(number_Combo)

    search_Links = print_Search(letter_Combo, number_Combo)
    #for key, value in search_Links.items():
        #print(value)

    option = "ask"
    while option != "n":
        print('\n' * 2)
        print(Fore.RESET +"=======================================================================")
        print(Fore.GREEN + "        Do You Want To Open A Random Image? (Y = Yes, N = No)")
        print(Fore.RESET+ "=======================================================================")
        #validation
        option = input(Fore.GREEN + "                            Enter (Y/N) :")
        option = option.lower()
        option = option.strip()

        if option == "y":
            open_Random(search_Links)
        elif option == 'n':
            option = "n"
        else:
            print(Fore.RED + "=======================================================================")
            print(Fore.RED + "            Please Enter A Valid Option (Y = Yes, N = No)")
            print(Fore.RED + "=======================================================================")
