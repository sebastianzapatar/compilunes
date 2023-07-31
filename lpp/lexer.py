from re import match
from lpp.tokens import(
    Token,
    TokenType,
    lookup_token_type
)

class Lexer:
    def __init__(self,source:str) -> None:
        self._source:str=source
        self._character:str=''
        self._position:int = 0
        self._read_position:int=0
        self._read_character()
        

    def next_token(self)->Token:
        self._skip_whitespace()
        if match(r'^=$', self._character):
            if self._peek_character() == '=':
                token = self._make_two_character_token(TokenType.EQ)
            else:
                token = Token(TokenType.ASSIGN, self._character)
        elif match(r'^\+$',self._character):
            token=Token(TokenType.PLUS,self._character)
        elif match(r'^$',self._character):
            token=Token(TokenType.EOF,self._character)
        elif self._is_letter(self._character):
            literal=self._read_identifier()
            token_type=lookup_token_type(literal)
            return Token(token_type,literal)
        elif self._is_number(self._character):
            literal=self._read_number()
            token_type=lookup_token_type(literal)
            return Token(TokenType.INT,literal)
        else: 
            token=Token(TokenType.ILLEGAL,self._character)
        self._read_character()
        return token

    def _is_letter(self,character:str)->bool:
        return bool(match(r'^[a-z-A-Z]',character))
    def _is_number(self,character:str)->bool:
        return bool(match('^\d$', character ))
        #return bool(match('^[0-9]$', character ))
    def _make_two_character_token(self, token_type: TokenType) -> Token:
        prefix = self._character
        self._read_character()
        suffix = self._character

        return Token(token_type, f'{prefix}{suffix}')
    def _peek_character(self) -> str:
        if self._read_position >= len(self._source):
            return ''
        return self._source[self._read_position]
    def _read_character(self)->None:
        if self._read_position>=len(self._source):
            self._character=''
        else:
            self._character=self._source[self._read_position]
        self._position=self._read_position
        self._read_position+=1
    def _read_identifier(self)->str:
        initial_position=self._position
        while self._is_letter(self._character):
            self._read_character()
        return self._source[initial_position:self._position]
    def _read_number(self)->str:
        initial_position=self._position
        while self._is_number(self._character):
            self._read_character()
        return self._source[initial_position:self._position]
    def _skip_whitespace(self)->None:
        while match(r'^\s$',self._character):
            self._read_character()

