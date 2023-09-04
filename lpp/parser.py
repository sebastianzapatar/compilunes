from enum import IntEnum
from typing import (
    Optional,
    List,
    Callable,
    Dict
)
from lpp.ast import (
    Identifier,
    LetStatement,
    Statement,
    Expression,
    Program,
    ReturnStatements,
    Call,
    ExpressionStatement,
    Function,
    If,
    Infix,
    Integer,
    Prefix,
    Block,
    Boolean
)
from lpp.tokens import(
    Token,
    TokenType
)
from lpp.lexer import Lexer

PrefixParseFn=Callable[[],Optional[Expression]]
InfixParseFn = Callable[[Expression],Optional[Expression]]
PrefixParseFns=Dict[TokenType,PrefixParseFn]
InfixParseFns=Dict[TokenType,InfixParseFn]


class Precedence(IntEnum):
    LOWEST=1
    EQUAL=2
    LESSGREATER=3
    SUM=4
    PRODUCT=5
    POW=6
    PREFIX=7
    CALL=8

PRECEDNCES:Dict[TokenType,Precedence]={
    TokenType.EQ:Precedence.EQUAL,
    TokenType.LTE:Precedence.LESSGREATER,
    TokenType.LT:Precedence.LESSGREATER,
    TokenType.GT:Precedence.LESSGREATER,
    TokenType.GTE:Precedence.LESSGREATER,
    TokenType.PLUS:Precedence.SUM,
    TokenType.MINUS:Precedence.SUM,
    TokenType.DIVISION:Precedence.PRODUCT,
    TokenType.MULTIPLICATION:Precedence.PRODUCT,
    TokenType.LPAREN: Precedence.CALL,
    TokenType.DIF:Precedence.EQUAL
}
    
class Parser:

    def __init__(self, lexer: Lexer) -> None:
        self._lexer = lexer
        self._current_token:Optional[Token]=None
        self._peek_token:Optional[Token]=None
        self._errors:List[str]=[]
        self._advance_tokens()
        self._advance_tokens()

    @property
    def errors(self)->List[str]:
        return self._errors
    
    def _expected_token_error(self,token_type:TokenType)->None:
        assert self._peek_token is not None
        error=f'Se esperaba {token_type} y se obtuvo {self._peek_token.token_type}'
        self._errors.append(error)
    def parse_program(self) -> Program:
        program: Program = Program(statements=[])

        return program
    def _expected_token(self,token_type:TokenType)->bool:
        assert self._peek_token is not None
        if self._peek_token==token_type:
            self._advance_tokens()
            return True
        # Para agregar el error en el token
        self._expected_token_error(token_type)
        return False
    def _advance_tokens(self)->None:
        self._current_token=self._peek_token
        self._peek_token=self._lexer.next_token()
    def _parse_let_statement(self)->Optional[LetStatement]:
        assert self._current_token is not None
        let_statement:LetStatement=LetStatement(token=self._current_token)

        if not self._expected_token(TokenType.IDENT):
            return None
        
        let_statement.name=Identifier(token=self._current_token,value=self._current_token)

        if not self._expected_token(TokenType.ASSING):
            return None
        
        #Por hacer cuando sepamos transformar guardar los valores

        while self._current_token.token_type != TokenType.SEMICOLON:
            self._advance_tokens()

        return let_statement
    def _parse_return_statement(self)->Optional[ReturnStatements]:
        assert self._current_token is not None
        return_statement=ReturnStatements(token=self._current_token)
        #Cuando sepamos evaluar expresiones para retonar
        self._advance_tokens()
        while self._current_token.token_type!=TokenType.SEMICOLON:
            self._advance_tokens()
        
        return return_statement
    def _parse_statement(self)->Optional[Statement]:
        assert self._current_token is not None
        if self._current_token.token_type==TokenType.LET:
            return self._parse_let_statement()
        elif self._current_token.token_type==TokenType.RETURN:
            return self._parse_return_statement()
        else:
            return None