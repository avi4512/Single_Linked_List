class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class SinlgeLinkedLIst:

    def __init__(self):
        self.head = None

    # Adding at the end of the linked list
    def at_end(self,data):
        ne = Node(data)
         if self.head is None:
            self.head = ne
        else:   
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ne

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

#adding at end using at_end method
l.at_end(50)
l.at_end(60)

l.display()
