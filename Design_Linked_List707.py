class Linked_Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size =0


    def get(self, index):
        if self.head==None:
            return
        if index < 0 :
            return -1
        elif index >=  self.size :
            print(-1)
            return -1
        
        else:  
            moveNode = self.head
            index_count = 0
            while index_count != index:
                moveNode = moveNode.next
                index_count += 1
            print(moveNode.data)
            return moveNode.data


    def addAtHead(self, val):
        newNode =  Linked_Node(val)
        if self.head == None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size +=1


    def addAtTail(self, val):
        newNode =  Linked_Node(val)
        if self.head == None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size +=1


    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        elif index ==self.size:
            self.addAtTail(val)

        elif not 1<= index <= self.size:
            print("index out of list")
        elif  1<= index < self.size:
            newNode =  Linked_Node(val)
            index_count =0
            moveNode = self.head
            while index_count+1 != index:
                moveNode = moveNode.next
                index_count +=1
            newNode.next = moveNode.next
            moveNode.next = newNode
            self.size +=1

    def deleteAtIndex(self, index):
        print(self.size)
        if self.head==None:
            return
        if index == 0 and self.size == 1:
            self.head=None
            self.tail=None
        elif index == 0 and self.size > 1:
            self.head = self.head.next
        elif 0<index<self.size-1:
            index_count =0
            moveNode = self.head
            while index_count != index:
                preNode = moveNode
                moveNode = moveNode.next
                index_count +=1
            preNode.next = moveNode.next
      
        elif index==self.size-1:
            index_count =0
            moveNode = self.head
            while index_count != index:
                preNode = moveNode
                moveNode = moveNode.next
                index_count +=1
            preNode.next = None
            self.tail = preNode
        else:
            return
        self.size-=1

    def print_linkedlist(self):
        current_node = self.head
        for i in range(self.size):
            print("[%d]%s" % (i,str(current_node.data)))
            current_node = current_node.next
        

def main():
    s=MyLinkedList()
    s.addAtHead(4)
    s.get(1)
    s.addAtHead(1)
    s.addAtHead(5)
    s.print_linkedlist()
    s.deleteAtIndex(3)
    s.print_linkedlist()
    s.addAtHead(7)
    s.get(3)
    s.get(3)
    s.get(3)
    s.addAtHead(1)
    s.deleteAtIndex(4)
    # s.print_linkedlist()

    # s.print_linkedlist()
if __name__ == '__main__':
    main()
