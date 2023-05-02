from sly import Lexer

class leksikal(Lexer):
    tokens = {PRINT, NUMBER, TO, ARROW, THEN, NAME, STRING, IF, ELSE, FOR, FUN, EQEQ}
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    PRINT = r'tampilna'
    IF = r'misale'
    ELSE = r'nekora'
    FOR = r'nggo'
    FUN = r'fungsine'
    STRING = r'\".*?\"'
    THEN = r'barkue'
    EQEQ = r'=='
    ARROW = r'->'
    TO = r'maring'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = leksikal()
    env = {}
    while True:
        try:
            text = input('ngapakLang> ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
