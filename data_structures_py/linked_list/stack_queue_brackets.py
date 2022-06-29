# from data_structures_py.linked_list.linkedlist import LinkedList
#
#
# def cook(s):
#     """
#     Arguments:
#         1. s: a string input (str)
#     Output:
#         2. A boolean value, True or False (bool)
#     """
#     l = list(s.split())
#     if l[0] == ')' or l[0] == ']' or l[0] == '}':
#         return False
#
#     a = []
#     b = []
#     c = []
#
#     valid = True
#
#     for i in s:
#         if i == '(':
#             a.append(i)
#         if i == '[':
#             b.append(i)
#         if i == '{':
#             c.append(i)
#         if i == ')':
#             a.append(i)
#         if i == ']':
#             b.append(i)
#         if i == '}':
#             c.append(i)
#
#     coun1 = 0
#     coun2 = 0
#
#     for aa in a:
#         if aa == '(':
#             coun1 += 1
#         if aa == ')':
#             coun2 += 1
#     if coun1 != coun2:
#         return False
#
#     coun1 = 0
#     coun2 = 0
#
#     for bb in b:
#         if bb == '[':
#             coun1 += 1
#         if bb == ']':
#             coun2 += 1
#     if coun1 != coun2:
#         return False
#
#     coun1 = 0
#     coun2 = 0
#
#     for cc in c:
#         if cc == '}':
#             coun1 += 1
#         if cc == '{':
#             coun2 += 1
#     if coun1 != coun2:
#         return False
#
#     return True
#
#
# class Node:
#     """
#     Node creator
#     """
#
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
#
#
# class Stack:
#     """
#     Stack creator
#     """
#
#     def __init__(self, top=None):
#         self.top = top
#
#     def push(self, value):
#         if self.is_empty():
#             self.top = Node(value)
#         else:
#             new_top = Node(value)
#             new_top.next = self.top
#             self.top = new_top
#
#     def pop(self):
#         if self.is_empty():
#             raise Exception('Error!')
#         val = self.top.value
#         self.top = self.top.next
#         return val
#
#     def peek(self):
#         if self.is_empty():
#             raise Exception('Error!')
#         else:
#             return self.top.value
#
#     def is_empty(self):
#         return self.top is None
#
#
# class Queue:
#     """
#     Queue creator
#     """
#     node = Node()
#
#     def __init__(self, front=None, back=None):
#         self.front = front
#         self.back = back
#
#     def enqueue(self, value):
#         if self.is_empty():
#             self.front = Node(value)
#         else:
#             self.back = Node(value)
#             self.front.next = self.back
#
#     def dequeue(self):
#         if self.is_empty():
#             raise Exception('Error!')
#         val = self.front.value
#         self.front = self.front.next
#         return val
#
#     def peek(self):
#         if self.is_empty():
#             raise Exception('Error!')
#         return self.front.value
#
#     def is_empty(self):
#         return self.front is None


def validate_brackets(s):
    """
    Arguments:
        1. s: a string input (str)
    Output:
        2. A boolean value, True or False (bool)
    """
    l = list(s.split())
    if l[0] == ')' or l[0] == ']' or l[0] == '}':
        return False

    """
    stk = Queue()

    opn = []
    clo = []

    for ss in s:
        if l[0] == '(' or l[0] == '[' or l[0] == '{':
            opn.append(ss)

        if l[0] == ')' or l[0] == ']' or l[0] == '}':
            clo.append(ss)

    for op in opn:
        stk.enqueue(op)

    for cl in clo:
        stk.enqueue(cl)

    while stk:
        r = stk.dequeue()
        if r ==
    """

    a = []
    b = []
    c = []

    for i in s:
        if i == '(':
            a.append(i)
        if i == '[':
            b.append(i)
        if i == '{':
            c.append(i)
        if i == ')':
            a.append(i)
        if i == ']':
            b.append(i)
        if i == '}':
            c.append(i)

    coun1 = 0
    coun2 = 0

    for aa in a:
        if aa == '(':
            coun1 += 1
        if aa == ')':
            coun2 += 1
    if coun1 != coun2:
        return False

    coun1 = 0
    coun2 = 0

    for bb in b:
        if bb == '[':
            coun1 += 1
        if bb == ']':
            coun2 += 1
    if coun1 != coun2:
        return False

    coun1 = 0
    coun2 = 0

    for cc in c:
        if cc == '}':
            coun1 += 1
        if cc == '{':
            coun2 += 1
    if coun1 != coun2:
        return False

    return True


if __name__ == "__main__":
    print(validate_brackets('{}'))
    print(validate_brackets('{}(){}'))
    print(validate_brackets('()[[Extra Characters]]'))
    print(validate_brackets('(){}[[]]'))
    print(validate_brackets('{}{Code}[Fellows](())'))
    print(validate_brackets('[({}]'))
    print(validate_brackets('(]('))
    print(validate_brackets('{(})}'))
    print(validate_brackets('{'))
    print(validate_brackets(')'))
    print(validate_brackets('[}'))
