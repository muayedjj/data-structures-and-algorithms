class Animal:
    """
    Animal instantiator
    """

    def __init__(self, typ: str = None, next=None):
        self.typ = typ
        self.next = next

    def cat(self):
        self.typ = 'cat'
        return self.typ

    def dog(self):
        self.typ = 'dog'
        return self.typ

class AnimalShelter(Animal):
    """
    Animal Queuer
    """
    cat = Animal().cat()
    dog = Animal().dog()

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def enqueue(self, animal):
        if self.front is None:
            self.front = Animal(animal)
        else:
            self.back = Animal(animal)
            self.front.next = self.back

    def dequeue(self, pref):
        if pref == 'cat':
            if self.front is None:
                raise Exception('error')
            val = self.front.typ
            self.front = self.front.next
            return val
        elif pref == 'dog':
            if self.front is None:
                raise Exception('error')
            val = self.front.typ
            self.front = self.front.next
            return val
        else:
            return 'null'
"""
    def peek(self):
        if self.is_empty():
            raise Exception('Error!')
        return self.front.value

    def is_empty(self):
        return self.front is None
"""


if __name__ == "__main__":
    shelter = AnimalShelter()
    ct = Animal()
    c = ct.cat()
    dg = Animal()
    d = dg.dog()
    shelter.enqueue(d)
    shelter.enqueue(d)
    shelter.enqueue(c)
    shelter.enqueue(d)
    shelter.enqueue(c)
    # print(c)
    # print(Animal('cat').typ)
    print(shelter.dequeue(Animal('dog').typ))
    print(shelter.dequeue(Animal('dog').typ))
    print(shelter.dequeue(Animal('dog').typ))

    # print(shelter.dequeue(d))
    # print(shelter.dequeue(c))
    # print(shelter.dequeue(d))
    # print(shelter.dequeue(c))


    # print(str(shelter.dog))
    # print(shelter.dequeue(dg))
    # print(list_one.get(4))
    # print(list_one.length())
    # print(list_one.__str__())
    # print(list_one.includes(4))
    # print(list_one.includes('C'))
    #
    # print(str(list_one))
    # print(repr(list_one))

