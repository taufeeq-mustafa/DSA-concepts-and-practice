class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    
    def print_list(self):
        current=self.head
        while current:
            print(current.data, end="->")
            current=current.next
        print ("None")
    
    def delete_node(self, key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return

        prev=None
        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next

        if temp is None:
            return
        prev.next=temp.next
        temp=None

    def search(self, key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
        return False
    
linked_list=Linkedlist()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print("initial list")
linked_list.print_list()
if linked_list.search(30):
    print("element 30 found")
linked_list.delete_node(40)
linked_list.print_list()