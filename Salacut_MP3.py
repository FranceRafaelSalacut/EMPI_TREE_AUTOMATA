'''
HONOR CODE
I declare, upon my honor, that I did this machine problem assignment by myself using references from the lecture notes and MPs.

I have watched the video primer and decided to follow its lead

REPO LINK

NOTE: THE COMMIT MESSAGES AND REPO NAME ARE NOT FUNCTIONAL
https://github.com/FranceRafaelSalacut/EMPI_TREE_AUTOMATA.git

'''

from icecream import ic

#DataType
D_TYPE = ["int",
        "char",
        "float",
        "double",
        "void"
        ]

classes = ["int",	"char",	"double",	"float", "var name",	"number",	"char",	 "space",	"comma",	"semi colon",	"period",	"equal",	"others"]

var_table = [
    ['1', '9', '19', '19', '27', '27', '27', '27', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '2', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '3', '27', '27', '2', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '4', '2', '5', '27', '6', '27'],
['27', '27', '27', '27', '27', '27', '27', '4', '27', '5', '27', '6', '27'],
['1', '9', '19', '19', '27', '27', '27', '0', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '7', '27', '6', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '8', '2', '5', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '8', '2', '5', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '10', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '11', '27', '27', '10', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '12', '10', '13', '27', '14', '27'],
['27', '27', '27', '27', '27', '27', '27', '12', '27', '13', '27', '14', '27'],
['1', '9', '19', '19', '27', '27', '27', '0', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '15', '14', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '16', '10', '13', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '16', '10', '13', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '18', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '19', '27', '27', '18', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '20', '18', '21', '27', '22', '27'],
['27', '27', '27', '27', '27', '27', '27', '20', '27', '21', '27', '22', '27'],
['1', '9', '19', '19', '27', '27', '27', '0', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '23', '27', '22', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '23', '18', '21', '24', '27', '27'],
['27', '27', '27', '27', '27', '25', '27', '27', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '26', '18', '21', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '26', '18', '21', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '27', '27', '27', '27', '27', '27']
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

def classify(str):
    

    if str == 'int':
        return 0
    elif str == 'char':
        return 1
    elif str == 'double':
        return 2
    elif str == 'float':
        return 3
    elif str == " ":
        return 7
    elif str == ",":
        return 8
    elif str == ";":
        return 9
    elif str ==".":
        return 10
    elif str == "=":
        return 11
    elif valid_name(str):
        return 4
    elif valid_integer(str):
        return 5
    elif valid_character(str):
        return 6
    else:
        return 12

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
    state = 0
    ic(str)
    for token in str:
        ic(token)
        ic(classes[classify(token)])
        state = int(var_table[state][classify(token)])
        ic(state)
        if state == 27:
            break

    if state == 5:
        return "VALID VARIABLE DECLARATION"
    elif state == 13:
        return "VALID VARIABLE DECLARATION"
    elif state == 21:
        return "VALID VARIABLE DECLARATION"
    else:
        return "INVALID VARIABLE DECLARATION"
    

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