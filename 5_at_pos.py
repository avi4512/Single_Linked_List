class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None


    def display(self):

        temp = self.head

        if temp is None:
            print("Linked list is Empty..!")

        else:
            while temp:
                print(temp.data, '-->', end=" ")
                temp = temp.next

    def length(self,c):

        temp = self.head

        if temp is None:
            c = 0

        else:
            while temp:
                temp = temp.next
                c = c + 1
            return c



    def begin(self, d):

        nb = Node(d)
        nb.next = self.head
        self.head = nb

    def end(self, info):

        temp = self.head

        if temp is None:
            ne = Node(info)
            ne.next = self.head
            self.head = ne
        else:

            while temp.next is not None:
                temp = temp.next

            ne = Node(info)
            ne.next = temp.next
            temp.next = ne

    def position(self, pos, data):
        if pos > l.length(0):
            print("Pos Exceed.....! take range in |----| {}".format(l.length(0)-1))

        elif pos == 0:
            np = Node(data)
            np.next = self.head
            self.head = np

        else:
            temp = self.head

            for i in range(pos - 1):
                temp = temp.next

            np = Node(data)
            np.next = temp.next
            temp.next = np


l = Linkedlist()

l.begin(10)
l.begin(20)
l.begin(30)
l.begin(40)

l.position(4, 25)
l.position(0,10)
l.position(8,20)
l.begin(1)
l.end(2)


l.display()




