from lpp.lexer import Lexer
from lpp.tokens import (
    Token,
    TokenType,
)

from lpp.parser import Parser
from lpp.ast import Program
from lpp.evaluator import evaluate
EOF_TOKEN: Token = Token(TokenType.EOF, '')


def start_repl() -> None:
    while (source := input('>> ')) != 'salir()':
        lexer: Lexer = Lexer(source)

        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()

        print(program)
        evaluated = evaluate(program)
        if evaluated is not None:
            print(evaluated.inspect())


