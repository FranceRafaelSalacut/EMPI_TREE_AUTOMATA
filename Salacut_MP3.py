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
classes2 = ["int",	"char",	"double",	"float",	"void",	"var name",	 "space",	"comma",	"semi colon",	"others",	"(",	")"]

var_table = [
['1', '9', '17', '17', '27', '27', '27', '27', '27', '27', '27', '27', '27'],  
['27', '27', '27', '27', '27', '27', '27', '2', '27', '27', '27', '27', '27'], 
['27', '27', '27', '27', '3', '27', '27', '2', '27', '27', '27', '27', '27'],  
['27', '27', '27', '27', '27', '27', '27', '4', '2', '5', '27', '6', '27'],    
['27', '27', '27', '27', '27', '27', '27', '4', '27', '5', '27', '6', '27'],   
['1', '9', '17', '17', '27', '27', '27', '0', '27', '27', '27', '27', '27'],   
['27', '27', '27', '27', '27', '7', '7', '6', '27', '27', '27', '27', '27'],  
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
['27', '27', '27', '27', '21', '27', '27', '20', '27', '21', '27', '22', '27'],
['1', '9', '17', '17', '27', '27', '27', '0', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '23', '27', '22', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '23', '18', '21', '24', '27', '27'],
['27', '27', '27', '27', '27', '25', '27', '27', '27', '27', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '26', '18', '21', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '26', '18', '21', '27', '27', '27'],
['27', '27', '27', '27', '27', '27', '27', '27', '27', '27', '27', '27', '27']
]

fun_table = [
['1', '1', '1', '1', '1', '9', '9', '9', '9', '9', '9', '9'],
['9', '9', '9', '9', '9', '2', '1', '9', '9', '9', '9', '9'],
['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '3', '9'],
['4', '4', '4', '4', '4', '9', '3', '9', '9', '9', '9', '5'],
['9', '9', '9', '9', '9', '7', '4', '3', '9', '9', '9', '5'],
['9', '9', '9', '9', '5', '9', '9', '1', '6', '9', '9', '9'],
['1', '1', '1', '1', '1', '9', '0', '9', '9', '9', '9', '9'],
['9', '9', '9', '9', '9', '9', '8', '3', '9', '9', '9', '5'],
['9', '9', '9', '9', '9', '9', '8', '3', '9', '9', '9', '5'],
['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
]

def manual_tokenize_(str):
    tokens = []
    delimiter = [',', ';', ' ', "=", ".", "(", ")"]

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
    elif valid_integer(str):
        return 5
    elif valid_character(str):
        return 6
    elif valid_name(str):
        return 4
    else:
        return 12

def valid_name(name):
    if name in D_TYPE:
        return False
    
    if name[0].isdigit():
        return False
    
    if "-" in name:
        return False
    
    return True

def valid_integer(str):
    str = str.replace("-","")
    return str.isdigit()

def valid_character(str):
    return True if "'" in str and len(str) == 3 else False

def check_var_declaration(str):
    state = 0
    ic(str)
    for token in str:
        ic(token)
        ic(classes[classify(token)])
        #an extra check for numbers from 0-255 declared as chars
        if state == 14 and classes[classify(token)] == "number":
            if int(token) >= 0 and int(token) <= 255:
                state = 15
        else:
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


def classify2(str):
    if str == 'int':
        return 0
    elif str == 'char':
        return 1
    elif str == 'double':
        return 2
    elif str == 'float':
        return 3
    elif str == 'void':
        return 4
    elif str == " ":
        return 6
    elif str == ",":
        return 7
    elif str == ";":
        return 8
    elif str == "(":
        return 10
    elif str == ")":
        return 11
    elif valid_name(str):
        return 5
    else: 
        return 9

def check_fun_declaration(str):
    state = 0
    ic(str)
    for token in str:
        ic(token)
        ic(classes2[classify2(token)])
        state = int(fun_table[state][classify2(token)])
        ic(state)
        if state == 9:
            break

    if state == 6:
        return "VALID FUNCTION DECLARATION"
    else:
        return "INVALID FUNCTION DECLARATION"


def main():
    #i = int(input())
    i = 1
    input = ["1 int x = 2, y = 5, z = -10; float num = -1234.56; double dobol = z; int a = y = z;"]

    for i in range(0, i):
        #word = manual_tokenize_(input()) # the tokenizer removes any extra spaces in the process
        word = manual_tokenize_(input[0]) 
        result = check_var_declaration(word[2:]) if word[0] == "1" else check_fun_declaration(word[2:])

        print(result)

main()
