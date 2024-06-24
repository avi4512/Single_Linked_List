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

    def sorted(self,n):

        if self.head is None or n < self.head.data:
            nn = Node(n)
            nn.next = self.head
            self.head = nn
            return

        temp = self.head
        prev = None
        while temp is not None and n > temp.data:
            prev = temp
            temp = temp.next

        nn = Node(n)
        nn.next = temp
        prev.next = nn

    def rev(self):
        prev = None
        current = self.head
        Nex = None

        while current:
            Nex = current.next   #to store current.next in Nex
            current.next = prev  # Store Current.next as Previous
            prev = current       #Previous as Current
            current = Nex        #Current as the Nex
          
        self.head = prev  #After the loop Change the head as Prev

#Creating obeject for Linked List
l = SingleLinkedList()


#Displaying the Linked List
x = input("Enter number with space:")
n = map(int,x.split())
for i in n:
    if i == -1:
        break
    l.sorted(i)

print("Before")
l.display()
#calling_reverse_method
l.rev()
print()
print("After")
l.display()
