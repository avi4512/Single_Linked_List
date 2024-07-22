class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:

    def __init__(self):
        self.head = None

    def display(self):

        if self.head is None:
            print("Linked list is Empty...")
            return
        temp = self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp = temp.next

    def at_begin(self,data):

        if self.head is None:
            nb = Node(data)
            nb.next = self.head
            self.head = nb
            return
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def at_end(self,data):

        if self.head is None:
            ne = Node(data)
            ne.next = self.head
            self.head = ne
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        ne = Node(data)
        temp.next = ne

    def after_node(self,n,data):

        if self.head is None:
            print("No node is Present in the LinkedList")
            return
        temp = self.head
        while temp:
            if temp.data == n:
                break
            temp = temp.next

        if temp is None:
            print("Node not found..!")
        else:
            an = Node(data)
            an.next = temp.next
            temp.next = an

    def before_node(self, data, n):
        if self.head is None:
            print("Their is No before node is Presented..")
            return
        if self.head.data == n:
            bn = Node(data)
            bn.next = self.head
            self.head = bn
            return
        temp = self.head
        prev = None
        while temp:
            if temp.data == n:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print("Node Not Found...!")
        else:
            bn = Node(data)
            bn.next = prev.next
            prev.next = bn


    def specific_pos(self,pos,data):

        if pos == 0:
            np = Node(data)
            np.next = self.head
            self.head = np
            return
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np = Node(data)
        np.next = temp.next
        temp.next = np


    def del_at_begin(self):

        if self.head is None:
            print("Can't Remove from the Empty LinkedList...!")
            return

        self.head = self.head.next

    def del_at_end(self):

        if self.head is None:
            print("Can't Remove from the Empty LinkedList...!")
            return

        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

    def del_by_val(self,data):

        if self.head is None:
            print("Can't Remove from the Empty LinkedList...!")
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head
        prev = None

        while temp:

            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print("Node Not Found...!")
        else:
            prev.next = temp.next

    def del_by_pos(self,pos):

        if self.head is None:
            print("Can't Remove from the Empty LinkedList...!")
            return

        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        temp.next = temp.next.next


l = Linked_list()

#Adding
l.at_begin(40)
l.at_begin(30)
l.at_begin(20)
l.at_begin(10)
l.at_end(45)
l.after_node(45,50)
l.before_node(43,45)
l.before_node(5,10)
l.before_node(48,50)
l.specific_pos(3,25)

#Removing
l.del_at_begin()
l.del_at_end()
l.del_by_val(43)
l.del_by_pos(6)

l.display()
