WHITESPACE = ' \n\t'
LETTER = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
LPAREN = '('
RPAREN = ')'
COMMA = ';'
DIGITAL = '0123456789'


class LexerSignatures:
    def __init__(self, text):
        self.current_char = None
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_signature_dict(self):
        # sig formats :
        # 1) sig_name(letters & whitespace)(input flows value separated by ,)(output flow value)
        # 2) sig_name( )(output flow value) *means no input flows
        # TODO: 3) sig_name( input flow value)( ) *means no output flow (identity function)
        signature = dict()
        string_str = ''
        count_LPAREN = 1
        while self.current_char != None:
            if self.current_char in LETTER or self.current_char in DIGITAL or self.current_char in WHITESPACE:
                string_str += self.current_char
                self.advance()
                if self.current_char == '(' and count_LPAREN == 1:
                    count_LPAREN += 1
                    signature.update({'signature_name': string_str})
                    signature_inputs = self.generate_signature_inputs()
                    signature.update({'signature_inputs': signature_inputs})
                if self.current_char == '(' and count_LPAREN == 2:
                    count_LPAREN += 1
                    signature_output = self.generate_signature_output()
                    signature.update({'signature_output': signature_output})
                if self.current_char == ')':
                    break
        return signature

    def generate_signature_inputs(self):
        inputs_list = []
        self.advance()
        string_str = ''
        while self.current_char in LETTER or self.current_char in DIGITAL or self.current_char in WHITESPACE or self.current_char in COMMA:
            string_str += self.current_char
            self.advance()
            if self.current_char == ')':
                if ';' in string_str:
                    inputs_list = string_str.split(';')
                else:
                    inputs_list = [string_str]
                self.advance()
                break
        return inputs_list

    def generate_signature_output(self):
        output = str()
        self.advance()
        string_str = ''
        while self.current_char in LETTER or self.current_char in DIGITAL or self.current_char in WHITESPACE:
            string_str += self.current_char
            self.advance()
            if self.current_char == ')':
                output = string_str
                break
        return output

# text =  'sign3(FLOW1;FLOW2)(FLOW3)'
# lexer = LexerSignatures(text)
# signature_dict = lexer.generate_signature_dict()
# print(signature_dict)

# text = 'RestrictMultiple( )(Flow 3)'
# lexer = LexerSignatures(text)
# signature_dict = lexer.generate_signature_dict()
# print(signature_dict)
