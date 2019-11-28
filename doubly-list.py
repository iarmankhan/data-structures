class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    
    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    
    def printList(self, node):
        while node is not None:
            print(node.data)
            node = node.next
        
    def deleteNode(self, node):

        if self.head is None or node is None:
            return

        if self.head == node:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

    def reverseList(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp is not None:
            self.head = temp.prev
            



dll = DoublyLinkedList()

dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

dll.printList(dll.head)

print('-----')
dll.reverseList()

dll.printList(dll.head)
