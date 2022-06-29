class Animal:
    """
    Animal instantiator
    """
    def __init__(self, typ: str = None, next=None):
        self.value = typ
        self.next = next

    # def cat(self):
    #     self.value = 'cat'
    #     return self.value
    #
    # def dog(self):
    #     self.value = 'dog'
    #     return self.value



class AnimalShelter(Animal):
    """
    Animal Queuer
    """

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def enqueue(self, animal):
        if self.front is None:
            self.front = animal
        else:
            self.back = animal
            self.front.next = self.back

    def dequeue(self, pref):
        if pref == 'cat' or pref == 'dog':
            if self.front is None:
                raise Exception('error')
            val = self.front.value
            self.front = self.front.next
            return val

        else:
            return 'null'


if __name__ == "__main__":
    shelter = AnimalShelter()
    cat1 = Animal('cat')
    dog1 = Animal('dog')
    dog2 = Animal('dog')
    cat2 = Animal('cat')

    # print(dog1.value)
    # c = ct.cat()
    dg = Animal()
    # d = dg.dog()
    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    shelter.enqueue(cat2)
    print(shelter.dequeue('cat'))
    print(shelter.dequeue('dog'))
    print(shelter.dequeue('dog'))

    # shelter.enqueue(c)
    # # print(c)
    # # print(Animal('cat').typ)
    # print(shelter.dequeue(Animal('dog').value))
    # print(shelter.dequeue(Animal('dog').value))
    # print(shelter.dequeue(Animal('dog').value))
    #
    # # print(shelter.dequeue(d))

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

