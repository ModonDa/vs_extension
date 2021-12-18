class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.Next=None
class double_linked_list:
    def __init__(self):
        self.start_node=None
    def insert(self,num):
        if self.start_node==None:
            new_node=Node(num)
            self.start_node=new_node
        else:
            n=self.start_node
            while n.Next!=None:
                n=n.Next
            new_node=Node(num)
            n.Next=new_node
            new_node.prev=n
    def display(self):
        if self.start_node is None:
            print("The list is empty !")
            return;
        else:
            n=self.start_node
            while n is not None:
                print(n.data,end='->')
                n=n.Next
    def reverse(self):
        current=self.start_node
        while(current!=None):
            temp=current.prev
            current.prev=current.Next
            current.Next=temp
            current=current.prev
        if temp is not None:
            self.start_node=temp.prev
k=double_linked_list()
k.insert(20)
k.insert(65)
k.insert(23)
k.insert(12)
k.insert(87)
k.insert(45)
k.insert(32)
k.display()
k.reverse()
print("\nReversed list:")
k.display()

'''Output:-

20->65->23->12->87->45->32->
Reversed list:
32->45->87->12->23->65->20->

'''
