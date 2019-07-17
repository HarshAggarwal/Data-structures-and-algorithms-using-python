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

def divide_by_2(dec_no):
    rem_stack = Stack()
    while dec_no > 0:
        rem = dec_no % 2
        rem_stack.push(rem)
        dec_no = dec_no // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return(bin_string)
