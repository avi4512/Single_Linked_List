class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None


    def display(self):

        if self.head is None:
            print("Linked list is Empty..")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,'-->',end=" ")
                temp = temp.next

    def insert_begin(self,data):

        if self.head is None:
            nb = Node(data)
            self.head = nb
        else:
            nb = Node(data)
            nb.next = self.head
            self.head = nb

    def insert_end(self,data):

        if self.head is None:
            ne = Node(data)
            self.head = ne
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            ne = Node(data)
            temp.next = ne
            
    def before_node(self,data,node):
        if self.head is None:
            print("Their is No before node is Presented..")
            return 
        if self.head.data == node:
            bn = Node(data)
            bn.next = self.head
            self.head = bn
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == node:
                    break
                else:
                    temp = temp.next
            if temp.next is None:
                print("Not Found the Node..")
            else:
                bn = Node(data)
                bn.next = temp.next
                temp.next = bn

    def after_node(self,node,data):

        if self.head is None:
            print("Their is No After node is Presented..")
            return
        temp = self.head
        while temp is not None:
            if temp.data == node:
                break
            else:
                temp = temp.next
        if temp is None:
            print("Node Not Found..")
        else:
            an = Node(data)
            an.next = temp.next
            temp.next = an

    def add_position(self,pos,data):
            temp = self.head
            if pos == 1:
                np = Node(data)
                np.next = self.head
                self.head = np
                return
            for i in range(1,pos-1):
                temp = temp.next
            np = Node(data)
            np.next = temp.next
            temp.next = np
        
            


l = Linkedlist()


#Creating Nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

#Making the Connections
l.head = n1
n1.next = n2
n2.next = n3
n3.next = n4


l.insert_begin(5)
l.insert_end(45)
l.before_node(25,30)
l.after_node(45,50)
l.add_position(3,15)



l.display()

