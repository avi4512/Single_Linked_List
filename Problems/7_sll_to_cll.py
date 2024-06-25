class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:

    def __init__(self):
        self.head = None

    def values(self,data):

        if self.head is None:
            nn = Node(data)
            self.head = nn
            return
        temp = self.head
        while temp.next :
            temp = temp.next
        nn = Node(data)
        temp.next = nn

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,'-->',end=" ")
            temp = temp.next
        print("NULL")

    def Convert_cll(self):
        if self.head is None:
            self.head.next = self.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head

    def display_cll(self):
        if self.head.next == self.head:
            print(self.head.data)
            return
        temp = self.head
        print(temp.data,'-->',end=" ")
        while temp.next != self.head:
            temp = temp.next
            print(temp.data,'-->',end=" ")
        print(temp.next.data)

l1 = Linked_list()

x = input()
n = map(int,x.split())
for i in n:
    if i == -1:
        break
    l1.values(i)
l1.display()

l1.Convert_cll()
l1.display_cll()


