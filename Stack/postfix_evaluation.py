class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def do_math(op, op1, op2):
    if op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1+op2
    else:
        return op1-op2

def postfix_eval(postfix_expr):
    op_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            op_stack.push(int(token))
        else:
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            result = do_math(token, op1, op2)
            op_stack.push(result)
    return op_stack.pop()
