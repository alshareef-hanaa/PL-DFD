from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None
        result = self.expr()
        if self.current_token != None:
            self.raise_error()
        return result

    def expr(self):
        result = self.factor()
        while self.current_token != None and self.current_token.type in (TokenType.JOIN, TokenType.MEET):
            if self.current_token.type == TokenType.JOIN:
                self.advance()
                result = JoinNode(result, self.factor())
            elif self.current_token.type == TokenType.MEET:
                self.advance()
                result = MeetNode(result, self.factor())
        return result

    def factor(self):
        token = self.current_token
        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            self.advance()
            return result
        elif token.type == TokenType.VARIABLE:
            self.advance()
            return VerNode(token.value)
        elif token.type == TokenType.TOP:
            self.advance()
            return TopNode(token.value)
        elif token.type == TokenType.BOTTOM:
            self.advance()
            return BottomNode(token.value)
        elif token.type == TokenType.CONSTANT:
            self.advance()
            return ConNode(token.value)
        self.raise_error()
