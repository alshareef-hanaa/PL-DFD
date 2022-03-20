from dataclasses import dataclass
@dataclass
class Token:
    value: any = None

    def __repr__(self):
        return f"{self.value}" if self.value != None else ""
