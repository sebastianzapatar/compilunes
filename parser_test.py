from unittest import TestCase
from lpp.ast import (
    Program,
    LetStament
)
from lpp.lexer import Lexer
from lpp.parser import Parser
from typing import(
    cast,
    List
)
class ParserTest(TestCase):
    def test_parse_program(self) -> None:
        source:str="variable x=5;"
        lexer:Lexer=Lexer(source)
        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()
        self.assertIsNotNone(program)
        self.assertIsInstance(program,Program)
    def test_let_statement(self)->None:
        source:str='''
            variable c=10;
            variable sa=25;
            variable otra=3244;
        '''
        lexer:Lexer=Lexer(source)
        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()
        self.assert_Equal(len(program.statements),3)
        for statement in program.statements:
            self.assertEqual(statement.token_literal(),'variable')
    

    def test_name_in_let_statements(self)->None:
        source:str='''
            variable c=10;
            variable sa=25;
            variable otra=3244;
        '''
        lexer:Lexer=Lexer(source)
        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()
        names:List[str]=[]
        for statement in program.statements:
            statement=cast(LetStament,statement)
            assert statement.name is not None
            names.append(statement.name.value)
        expected_names:List[str]=['c','sa','otra']
        self.assertEqual(names,expected_names)
    
    def test_error(self)->None:
        source:str='variable x 5;'
        lexer:Lexer=Lexer(source)
        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()

        self.assertEqual(len(parser.errors),1)
    
    def test_return_statement(self)->None:
        source:str='''
            regresa 5;
            regresa x;
        '''
        lexer:Lexer=Lexer(source)
        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()
        self.assertEqual(len(program.statements),2)

        






