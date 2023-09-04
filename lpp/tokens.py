from enum import (
    auto,
    Enum,
    unique,
    
)
from typing import (
    NamedTuple,
    Dict
)

@unique
class TokenType(Enum):
    ASSING=auto()
    COMMA=auto()
    DIF=auto()
    DIVISION=auto()
    ELSE=auto()
    ELSEIF=auto()
    EQ=auto()
    EOF=auto()
    FALSE=auto()
    FOR=auto()
    FUNCTION=auto()
    GT=auto()
    GTE=auto()
    IDENT=auto()
    IF=auto()
    ILLEGAL=auto()
    INT=auto()
    LBRACE=auto()
    LET=auto()
    LPAREN=auto()
    LT=auto()
    LTE=auto()
    MINUS=auto()
    MULTIPLICATION=auto()
    NEGATION=auto()
    NEQ=auto()
    PLUS=auto()
    RBRACE=auto()
    RPAREN=auto()
    RETURN=auto()
    SEMICOLON=auto()
    TRUE=auto()



class Token(NamedTuple):
    token_type:TokenType
    literal:str
    def __str__(self) -> str:
        return f'Type {self.token_type}, Literal {self.literal}'
    


def lookup_token_type(literal:str)->TokenType:
    keywords:Dict[str,TokenType]={
        'variable':TokenType.LET,
        'funcion':TokenType.FUNCTION,
        'para':TokenType.FOR,
        'regresa':TokenType.RETURN,
        'si':TokenType.IF,
        'si_no':TokenType.ELSE,
        'si_no_si':TokenType.ELSEIF,
        'verdadero':TokenType.TRUE,
        'falso':TokenType.FALSE
    }
    return keywords.get(literal,TokenType.IDENT)