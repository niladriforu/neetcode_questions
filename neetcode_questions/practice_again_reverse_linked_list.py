class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end='->')
            temp = temp.next
        print('None')
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # saving the pointer
            current.next = prev  # cutting off, pointing to previous value
            prev = current  # incrementing it by one to the right
            current = next_node #
        self.head = prev


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()
ll.reverse()
ll.print_list()












