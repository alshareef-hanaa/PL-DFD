from tokens import Token, TokenType

WHITESPACE = ' \n\t'
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
HASH = '#'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in HASH:
                yield self.generate_var()
                # yield Token(TokenType.VARIABLE, str(self.current_char))
                # self.advance()
            elif self.current_char in LETTERS:
                yield self.generate_constant()
            elif self.current_char == '|':
                self.advance()
                yield Token(TokenType.JOIN)
            elif self.current_char == '&':
                self.advance()
                yield Token(TokenType.MEET)
            elif self.current_char == 'T':
                self.advance()
                yield Token(TokenType.TOP)
            elif self.current_char == 'F':
                self.advance()
                yield Token(TokenType.BOTTOM)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_constant(self):
        constant_str = self.current_char
        self.advance()
        while self.current_char != None and (
                self.current_char in DIGITS or self.current_char in LETTERS or self.current_char == ';'):
            # if ';' in string_str:
            #     inputs_list = string_str.split(';')
            # else:
            #     inputs_list = [string_str]
            constant_str += self.current_char
            self.advance()
        return Token(TokenType.CONSTANT, str(constant_str))

    def generate_var(self):
        var_str = self.current_char
        self.advance()
        while self.current_char != None and self.current_char in DIGITS:
            var_str += self.current_char
            self.advance()
        return Token(TokenType.VARIABLE, str(var_str))
