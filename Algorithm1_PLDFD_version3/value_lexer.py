from value_tokens import Token

WHITESPACE = ' \n\t'
LETTER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGIT = "0123456789"
LPAREN = '('
RPAREN = ')'
COMMA = ','
SPECIALCH = '-'


class LexerValue:
    def __init__(self, text):
        # self.current_char = None
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_value_tokens(self):
        while self.current_char != None:
            # if self.current_char in WHITESPACE:
            #     self.advance()
            if self.current_char in LETTER or self.current_char in WHITESPACE:
                yield self.generate_value()
            elif self.current_char in LPAREN:
                self.advance()
                if self.current_char in LETTER or self.current_char in WHITESPACE:
                    yield self.generate_purposes()
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_value(self):
        string_str = self.current_char
        self.advance()
        while self.current_char != None and (
                self.current_char in LETTER or self.current_char in SPECIALCH or self.current_char in DIGIT or self.current_char in WHITESPACE):
            string_str += self.current_char
            self.advance()
        return Token(str(string_str))

    def generate_purposes(self):
        purposes_list = []
        string_str = self.current_char
        self.advance()
        if self.current_char in RPAREN:
            self.advance()
        else:
            while self.current_char != None and (self.current_char in LETTER or self.current_char in WHITESPACE):
                string_str += self.current_char
                self.advance()
                if self.current_char == ',':
                    purposes_list.append(string_str)
                    string_str = ''
                    self.advance()
                if self.current_char == ')':
                    purposes_list.append(string_str)
                    self.advance()
                    break
        return Token((','.join(purposes_list)))


# text = 'password( )'
# lexer = LexerValue(text)
# tokens = lexer.generate_value_tokens()
# list_tokens = list(tokens)
# value = list_tokens[0]
# purposes = list_tokens[1]
# print(value)
# print(purposes)
