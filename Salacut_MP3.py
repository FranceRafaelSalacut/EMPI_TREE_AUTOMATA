'''
HONOR CODE
I declare, upon my honor, that I did this machine problem assignment by myself using references from the lecture notes and MPs.

I have watched the video primer and decided to follow its lead

REPO LINK

NOTE: THE COMMIT MESSAGES AND REPO NAME ARE NOT FUNCTIONAL
https://github.com/FranceRafaelSalacut/EMPI_TREE_AUTOMATA.git

'''

import tokenize
from io import BytesIO
import re

#DataType
D_TYPE = ["int",
        "char",
        "float",
        "double",
        "void"
        ]


def manual_tokenize_(str):
    tokens = []
    delimiter = [',', ';', ' ']

    token = ''
    for char in str:
        if char in delimiter:
            if token != '':
                tokens.append(token)
            tokens.append(char)
            token = ''
        else:
            token = token + char

    return tokens

def valid_name(name):
    if name in D_TYPE:
        return False
    
    if name[0].isdigit():
        return False
    
    return True

def valid_integer(str):
    return str.isdigit()

def valid_character(str):
    return str.isalnum()

def check_var_declaration(str):
    print(str)

    return False
    

def check_fun_declaration(str):
    print(str)

    return False


def main():
    i = int(input())

    for _ in range(0, i):
        word = manual_tokenize_(input()) # the tokenizer removes any extra spaces in the process
        
        result = check_var_declaration(word[2:]) if word[0] == "1" else check_fun_declaration(word[2:])

        print(result)
main()
