import math
from enum import Enum

Token_Type = Enum('Token_Type', ('ORIGIN', 'SCALE', 'ROT', 'IS', 'TO', 'STEP',
                                'DRAW', 'FOR', 'FROM', 'T', 'SEMICO', 'L_BRACKET',
                                'R_BRACKET', 'COMMA', 'PLUS', 'MINUS', 'MUL',
                                'DIV', 'POWER', 'FUNC', 'CONST_ID', 'NONTOKEN',
                                'ERRTOKEN'))


class Token:
    '''
    Token_Type  type;
    str lexeme
    double value
    Func is a function
    '''
    def __init__(self, _type, _lexeme, _value, _Func):
        self.type = _type
        self.lexeme = _lexeme
        self.value = _value
        self.Func = _Func

    def show(self):
        if self.Func == None:
            func_name = 'NULL'
        else:
            func_name = self.Func.__name__

        print('< ' + str(self.type) + '\t' + '"' + self.lexeme + '"' + '\t' + str(self.value) + '\t' + func_name + '>')

    def get_value(self):
        return self.value


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def sqrt(x):
    return math.sqrt(x)


TokenTab = []
TokenTab.append(Token(Token_Type.CONST_ID.name, 'PI', 3.1415926, None))
TokenTab.append(Token(Token_Type.CONST_ID.name, 'E', 2.71828, None))
TokenTab.append(Token(Token_Type.T.name, 'T', 0.0, None))
TokenTab.append(Token(Token_Type.FUNC.name, 'SIN', 0.0, sin))
TokenTab.append(Token(Token_Type.FUNC.name, 'COS', 0.0, cos))
TokenTab.append(Token(Token_Type.FUNC.name, 'TAN', 0.0, tan))
TokenTab.append(Token(Token_Type.FUNC.name, 'LN', 0.0, log))
TokenTab.append(Token(Token_Type.FUNC.name, 'EXP', 0.0, exp))
TokenTab.append(Token(Token_Type.FUNC.name, 'SQRT', 0.0, sqrt))
TokenTab.append(Token(Token_Type.ORIGIN.name, 'ORIGIN', 0.0, None))
TokenTab.append(Token(Token_Type.SCALE.name, 'SCALE', 0.0, None))
TokenTab.append(Token(Token_Type.ROT.name, 'ROT', 0.0, None))
TokenTab.append(Token(Token_Type.IS.name, 'IS', 0.0, None))
TokenTab.append(Token(Token_Type.FOR.name, 'FOR', 0.0, None))
TokenTab.append(Token(Token_Type.FROM.name, 'FROM', 0.0, None))
TokenTab.append(Token(Token_Type.TO.name, 'TO', 0.0, None))
TokenTab.append(Token(Token_Type.STEP.name, 'STEP', 0.0, None))
TokenTab.append(Token(Token_Type.DRAW.name, 'DRAW', 0.0, None))