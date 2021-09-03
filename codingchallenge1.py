# YOUTUBE VID LIVE CODING SESSION: https://youtu.be/mwzegTnj1CE

class Node:
    def __init__(self, data):
        self._data = data
        self.next = None


n1 = Node(1)
n2 = Node(5)
n3 = Node(10)
n4 = Node(3)
n5 = Node(6)
head = n1

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

def insert(value, pos):
    current = head
    for i in range(1, pos - 1):
        current = current.next

    new_node = Node(value)
    new_node.next = current.next

    current.next = new_node

    current = head
    print("Output: ", end="")
    while current.next:
        print(current._data, " -> ", end="")
        current = current.next

    print(current._data)

insert(9, 3)
