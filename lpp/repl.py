from lpp.lexer import Lexer
from lpp.tokens import(
    Token,
    TokenType
)
EOF_TOKEN:Token=Token(TokenType.EOF,'')

#Se inicia la petición de comandos
def start_repl()->None:
    while (source:=input('>>>'))!='salir()':
        lexer:Lexer=Lexer(source)
        
        while(token:=lexer.next_token())!=EOF_TOKEN:
            print(token)
