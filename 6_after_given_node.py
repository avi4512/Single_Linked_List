#Creating Sinlge linked list and Adding data to it
#And displaying the Linked list

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty..!")
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=" ")
                temp = temp.next

    def after(self,x,data):

        temp = self.head
        while temp:
            if temp.data == x:
                break
            else:
                temp = temp.next
        if temp is None:
            print("Element not found...")
        else:
            na = Node(data)
            na.next = temp.next
            temp.next = na

#Creating obeject for Linked List
l = SingleLinkedList()

#Creating a nodes and Adding data to it
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

#Connecting the Nodes using the references(next)
l.head= n1
n1.next = n2
n2.next = n3
n3.next = n4

l.after(30,35)
l.after(10,15)
l.after(40,45)
#Displaying the Linked List
l.display()
