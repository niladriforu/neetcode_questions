# head is the linked list
# temp is what I am going to use to traverse linked list and create it
# setting head = new_node and then temp = self.head means temp is also of Node Type.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
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

# taking two completely new variables here to do the reversal
# prev will be used to define the last element in the node . it will be read first though
# next_node will immediately point to the next value of the current pointer
#     def reverse(self):
#         prev = None # not a Node type yet
#         current = self.head   # take a variable to point to the linked list to start reversal
#         while current:
#             next_node = current.next # saving the next value in a variable because we are going to reverse it
#             # MOST IMPORTANT PART to understand.
#             current.next = prev      # actually reversing the value
#             #Suppose the linked list is 1 -> 2 -> 3 -> None, and you are in the second iteration:
#             # prev points to the first node (1 -> None).
#             # current points to the second node (2 -> 3 -> None).
#             # After current.next = prev, the second node (2) now points to the first node (1), making it 2 -> 1 -> None.
#             prev = current           # move the loop one to the right. prev becomes Node type.
#             current = next_node      # move the loop one to the right. current again becomes Node type
#         self.head = prev

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev







ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print('Original list')
ll.print_list()

print('Reverse list')
ll.reverse()
ll.print_list()
