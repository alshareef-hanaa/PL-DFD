class Interpreter:
    def __init__(self):
        pass

    # visit gets the root node of the tree to process this tree
    # and returns a set
    def visit(self, node, basic_purposes):
        # we have method to each node type
        # this lines to know which method to delegate to
        # method_name holds string(name) of method we want to call
        method_name = f'visit_{type(node).__name__}'
        # print(method_name)
        # below: to get the method from the name
        method = getattr(self, method_name)
        # print(method)
        return method(node, basic_purposes)

    def visit_VerNode(self, node, basic_purposes):
        result = str(node.value)
        # result = evn_val[variable]
        return result

    def visit_JoinNode(self, node, basic_purposes):
        left_sid = self.visit(node.node_a, basic_purposes)
        if type(left_sid) == str:
            left_sid = {left_sid}
        right_sid = self.visit(node.node_b, basic_purposes)
        if type(right_sid) == str:
            right_sid = {right_sid}
        result = left_sid.union(right_sid)
        return result

    def visit_MeetNode(self, node, basic_purposes):
        left_sid = self.visit(node.node_a, basic_purposes)
        if type(left_sid) == str:
            left_sid = {left_sid}
        right_sid = self.visit(node.node_b, basic_purposes)
        if type(right_sid) == str:
            right_sid = {right_sid}
        result = left_sid.intersection(right_sid)
        return result

    def visit_TopNode(self, node, basic_purposes):
        # result = set.union(*evn_val.values())
        result = basic_purposes
        return result

    def visit_BottomNode(self, node, basic_purposes):
        result = set()
        return result