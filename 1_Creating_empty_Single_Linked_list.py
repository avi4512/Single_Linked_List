#Creating Empty Sinlg Linked List

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


#Creating obeject for Linked List
l = SingleLinkedList()

#Displaying the Linked List
l.display()
