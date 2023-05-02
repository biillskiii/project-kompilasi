import lexer_Ngapak
import parser_Ngapak
import interpreter_Ngapak
from sys import *

#MASUKAN LANGSUNG DENGAN TERMINAL PADA PROGRAM
if __name__ == '__main__':
    lexer_Ngapak = lexer_Ngapak.leksikal()
    parser_Ngapak = parser_Ngapak.sintaksis()
    env = {}
    while True:
        try:
            text = input('ngapakLang> ')
        except EOFError:
            break
        if text:
            tree = parser_Ngapak.parse(lexer_Ngapak.tokenize(text))
            interpreter_Ngapak.BasicExecute(tree, env)