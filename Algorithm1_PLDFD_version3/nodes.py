from dataclasses import dataclass


@dataclass
class VerNode:
    value: any

    def __repr__(self):
        return f"{self.value}"

@dataclass
class ConNode:
    value: any

    def __repr__(self):
        return f"{self.value}"


@dataclass
class TopNode:
    value: any

    def __repr__(self):
        return f"TOP"


@dataclass
class BottomNode:
    value: any

    def __repr__(self):
        return f"BOTTOM"


@dataclass
class JoinNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}|{self.node_b})"


@dataclass
class MeetNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}&{self.node_b})"
