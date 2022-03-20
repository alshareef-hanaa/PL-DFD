from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    VARIABLE = 0
    JOIN = 1
    MEET = 2
    TOP = 3
    BOTTOM = 4
    CONSTANT = 5
    LPAREN = 6
    RPAREN = 7


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")
