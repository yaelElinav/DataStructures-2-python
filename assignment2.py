from Lib.random import randrange


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def generator():
    lltype = randrange(1, 3, 1)
    linkedlist = LinkedList()

    first = Node(randrange(1, 101, 1))
    linkedlist.head = first
    tail = first

    if lltype == 1:
        more = randrange(1, 101, 1)
        while more != 100:
            nnode = Node(randrange(1, 101, 1))
            tail.next = nnode
            tail = nnode
            more = randrange(1, 101, 1)
        return linkedlist
    else:
        print('snail')
        loop = randrange(1, 1001, 1)
        while loop < 985:
            nnode = Node(randrange(1, 101, 1))
            tail.next = nnode
            tail = nnode
            loop = randrange(1, 1001, 1)
        loop_to = tail
        more = randrange(1, 101, 1)
        while more != 100 and more != 99:
            nnode = Node(randrange(1, 101, 1))
            tail.next = nnode
            tail = nnode
            more = randrange(1, 101, 1)
        tail.next = loop_to
        return linkedlist


def printer(llist, loop=None):
    head = llist.head
    length = 1
    if not loop:
        print("Snake!")
        while head:
            print(head.data, end=' → ')
            head = head.next
            length += 1
        length -= 1
        print("null")
        print("snake length:{}".format(length))
    else:
        print("Snail!")
        while head.next is not loop:
            print(head.data, end=' → ')
            head = head.next
            length += 1
        print('{} ↱'.format(head.data), end=' ')
        head = head.next
        length += 1
        loop_length = 1
        while head.next is not loop:
            print(head.data, end=' → ')
            head = head.next
            length += 1
            loop_length += 1
        print('{} ↲'.format(head.data))
        print("snail total length:{}".format(length))
        print("loop length:{}".format(loop_length))


def snake_or_snail(head):
    pass


if __name__ == "__main__":
    snek = LinkedList()

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    snek.head = n1

    snel = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n3
    snel.head = n1

    # s = generator()
    # printer(s)

    printer(snek)
    printer(snel, n3)
