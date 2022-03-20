from nodes import *


class Interpreter:
    def __init__(self):
        pass

    # visit gets the root node of the tree to process this tree
    # and returns a set
    def visit(self, node, evn_val, basic_purposes,sig_inputs):
        # we have method to each node type
        # this lines to know which method to delegate to
        # method_name holds string(name) of method we want to call
        method_name = f'visit_{type(node).__name__}'
        # print(method_name)
        # below: to get the method from the name
        method = getattr(self, method_name)
        # print(method)
        return method(node, evn_val, basic_purposes,sig_inputs)

    def visit_VerNode(self, node, evn_val, basic_purposes,sig_inputs):
        # variable = str(node.value)
        variable = sig_inputs.pop(0)
        result = evn_val[variable]
        return result

    def visit_ConNode(self, node, evn_val, basic_purposes,sig_inputs):
        constant = str(node.value)
        if ';' in constant:
            result = set(constant.split(';'))
        else:
            result = set(constant.split(' '))
        return result

    def visit_JoinNode(self, node, evn_val, basic_purposes,sig_inputs):
        left_sid = self.visit(node.node_a, evn_val, basic_purposes,sig_inputs)
        right_sid = self.visit(node.node_b, evn_val, basic_purposes,sig_inputs)
        result = left_sid.union(right_sid)
        return result

    def visit_MeetNode(self, node, evn_val, basic_purposes,sig_inputs):
        left_sid = self.visit(node.node_a, evn_val, basic_purposes,sig_inputs)
        right_sid = self.visit(node.node_b, evn_val, basic_purposes,sig_inputs)
        result = left_sid.intersection(right_sid)
        return result

    def visit_TopNode(self, node, evn_val, basic_purposes,sig_inputs):
        # result = set.union(*evn_val.values())
        result = basic_purposes
        return result

    def visit_BottomNode(self, node, evn_val, basic_purposes,sig_inputs):
        result = set()
        return result
