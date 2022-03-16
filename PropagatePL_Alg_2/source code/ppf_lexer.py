WHITESPACE = ' \n\t'
DIGITS = '0123456789'
SET_OPERATIONS = '|&TF'
HASH = '#'
LPAREN = '('
RPAREN = ')'

class LexerPPF:
    def __init__(self, text):
        self.current_char = None
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_formula(self, sig_inputs):
        formula = ''
        while self.current_char != None:
            if self.current_char in HASH:
                var = self.generate_variables(sig_inputs)
                formula += var
            elif self.current_char in WHITESPACE or self.current_char in SET_OPERATIONS or self.current_char in RPAREN or self.current_char in LPAREN:
                formula += self.current_char
                self.advance()
        return formula

    def generate_variables(self, sig_inputs):
        var = ''
        self.advance()
        while self.current_char != None and (self.current_char in DIGITS or self.current_char in WHITESPACE):
            self.advance()
        var = sig_inputs[0]
        del sig_inputs[0]
        return var

# sig_inputs = ['7', '8']
# text = '#1|#2'
# lexer = LexerPPF(text)
# formula = lexer.generate_formula(sig_inputs)
# print(formula)
# output -> 'i0|i1' woooow got it