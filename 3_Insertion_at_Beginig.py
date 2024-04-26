#inserting node at the Beginig of the Single  Linked List

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class SinlgeLinkedLIst:

    def __init__(self):
        self.head = None

    #insertion node at the Begining of Linked List
    def insert_begin(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def display(self):
        if self.head is None:
            print("Linked List is Empty...!")
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end="")
                temp = temp.next

l = SinlgeLinkedLIst()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4

#Calling method and Adding node
l.insert_begin(5)

l.display()
