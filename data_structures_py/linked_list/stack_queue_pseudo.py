from data_structures_py.linked_list.stack_and_queue import Node, Stack


class PseudoQueue:

    def __init__(self):
        # self.front = self.s_1.top
        self.s_1 = Stack()
        self.s_2 = Stack()

    # def __init__(self, s_1=None, s_2=None, front=None, rear=None):
    #     self.s_1 = s_1
    #     self.s_2 = s_2
    # #     self.front = front
    #     self.rear = rear

    def enqueue(self, value):
        self.s_1.push(value)
        # self.front = self.s_1.top

    def dequeue(self):
        if self.s_1.top is None:
            raise Exception('Error!')
        while self.s_1.top:
            self.s_2.push(self.s_1.pop())
        val = self.s_2.pop()
        while self.s_2.top:
            self.s_1.push(self.s_2.pop())

        return val



