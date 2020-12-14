import re

test = "x = y/1+3 - array(500)"

#check if a string is valid according to a regex
def valid_regex(regex,string):
    extracted_regex = regex.findall(string)
    found = False
    if(len(extracted_regex) != 0):
        found = True
    return found,extracted_regex

identifier_regex = re.compile('^[a-z][a-z]*[0-9]*[a-z]*$')
number_regex = re.compile('^[-+]?[0-9]+$')
split_regex = '(\W)'

token_types = {
    'SEMICOLON':';',
    'IF':'if',
    'THEN':'then',
    'END':'end',
    'REPEAT':'repeat',
    'UNTIL':'until',
    'READ':'read',
    'WRITE':'write',
    'ASSIGN':':=',
    'LESSTHAN':'<',
    'EQUAL':'=',
    'PLUS':'+',
    'MINUS':'-',
    'MULT':'*',
    'DIV':'/',
    'OPENBRACKET':'(',
    'CLOSEDBRACKET':')'
}


class token:
    def __init__(self, value):
        self.token_type = None
        self.value = value
        self.error = True

    def find_type(self):
        error = True
        # check if found in token_types dict
        for token_type in token_types:
            if (self.value == token_types[token_type]):
                self.token_type = token_type
                self.error = False
        # check if number
        found, extracted_regex = valid_regex(number_regex, self.value)
        if (found == True):
            self.token_type = 'NUMBER'
            self.error = False
        # check if identifer
        found, extracted_regex = valid_regex(identifier_regex, self.value)
        if (found == True):
            self.token_type = 'IDENTIFIER'
            self.error = False

#remove spaces
splitted = test.split()

tokens = []
for s in splitted:
    # split by words
    regex_splitted = re.split(split_regex, s)
    for r in regex_splitted:
        if r != '':
            tokens.append(token(r))
            tokens[-1].find_type()
            print(tokens[-1].error, tokens[-1].value, tokens[-1].token_type)

