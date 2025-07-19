## simple variables like v_string etc , both for number and string are immutable.
## this means the string is going to create a new memory address if you assign a new value
## but in case of instance of a class , the object is mutable.
## it means the object will only reference value stored in a particular memory address.
##

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to append a new node at the end
    def append(self, data):
        # new_node is of node type. new_node.val = value ( 1,2,3 etc ) and new_node.next = None ( initially )
        new_node = Node(data)
        if not self.head:
            # self.head is also node type. self.head.val = value ( 1,2,3 etc ) and self.head.next = None ( initially)
            self.head = new_node
            return
        # this is where we are reading the previous value and next. for the second iteration, self.head.val = 1 and self.head.next = none
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Function to print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current
            current = next_node  # Move current to next
        self.head = prev  # Update head to new first node


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List:")
ll.print_list()

# ll.reverse()

# print("Reversed List:")
# ll.print_list()
