from dataclasses import dataclass


@dataclass
class Vers:
    value: any

    def __repr__(self):
        return f"{self.value}"
