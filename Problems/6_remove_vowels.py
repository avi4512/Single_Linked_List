class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:

    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty..!")
        else:
            temp = self.head
            while temp:
                print(temp.data,end="")
                temp = temp.next

    def values(self,data):

        if self.head is None:
            nn = Node(data)
            nn.next = self.head
            self.head = nn

            return
        temp = self.head
        while temp.next:
            temp = temp.next
        nn = Node(data)
        temp.next = nn

    def Conso(self):
        vowels = "aeiouAEIOU"
        temp = self.head
        prev = None
        while temp:
            if temp.data in vowels:
                if temp == self.head:
                    self.head = temp.next
                    temp = self.head
                else:
                    prev.next = temp.next
                    temp = prev.next
            else:
                prev = temp
                temp = temp.next

l1 = Linked_list()

n = "Avinash Reddy"

for i in n:
    l1.values(i)

print("Original list.......")
l1.display()
print()
l1.Conso()
print("After ........")
l1.display()



