from linkedlist import LinkedList, Node


def zip_lists(list_1, list_2):
    """
    2 into 1 linked list merger.
    This function takes in two linked lists and merges them together.
    Arguments:
        1. lin_lst_1 (A singly-linked Linked List).
        2. lin_lst_2 (A singly-linked Linked List).
    Output:
        1. A mutated version of one of the input linked lists in the form of
           a new linked list made up of the alternating node values from both of the two input arguments.
    """

    """
    if list_1.length() == 0:
        return list_2
    elif list_2.length() == 0:
        return list_1
    elif list_1.length() >= list_2.length():
        poi_1 = list_1.head
        poi_2 = list_2.head
        while poi_2 is not None:
            temp = poi_1.next
            list_1.insert_after(poi_1.value, poi_2.value):
            poi_1 = temp
            poi_2 = poi_2.next
        
        return list_1
        
    else:
        poi_1 = list_1.head
        poi_2 = list_2.head
        while poi_1 is not None:
            temp = poi_2.next
            list_2.insert_after(poi_2.value, poi_1.value):
            poi_2 = temp
            poi_1 = poi_1.next
        
        return list_1


    """

    curr_1 = list_1.head
    curr_2 = list_2.head

    while curr_1 and curr_2:
        nxt_1 = curr_1.next
        nxt_2 = curr_2.next

        curr_1.next = curr_2
        curr_2.next = nxt_1

        curr_1 = nxt_1
        curr_2 = nxt_2

    return list_1


if __name__ == "__main__":
    list_one = LinkedList()
    list_one.append('A')
    list_one.append('B')
    list_one.append('C')
    list_one.append('D')
    list_one.append('E')

    list_two = LinkedList()
    list_two.append('1')
    list_two.append('2')
    list_two.append(3)
    list_two.append(4)
    list_two.append(5)

    # print(list_one.length())
    print(list_one.__str__())

    # print(list_two.length())
    print(list_two.__str__())

    print(zip_lists(list_one, list_two))
