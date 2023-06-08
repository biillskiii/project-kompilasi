import interpreter_Ngapak
import lexer_Ngapak
import parser_Ngapak

from sys import *

# DENGAN MASUKAN BERUPA FILE DENGAN EKSTENSION .ngpk
lexer = lexer_Ngapak.leksikal()
parser = parser_Ngapak.sintaksis()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    interpreter_Ngapak.BasicExecute(tree, env)
