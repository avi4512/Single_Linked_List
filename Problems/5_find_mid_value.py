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
                print(temp.data,'-->',end=" ")
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

    def find_mid(self):
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

        print(slow.data)


l1 = Linked_list()



while True:
    n = int(input("Enter the n:"))
    if n == -1:
        break
    l1.values(n)

l1.display()
print()
print("Mid Value is:")
l1.find_mid()
