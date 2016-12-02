class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
              self.tail=x

    def remove(self, node_value):
        n = self.head #becomes current head
        while n is not None: #while n is not null
            if n.value == node_value: #gains value
                if n.prev is not None: #if it's not first in list
                    n.prev.next = n.next 
                    n.next.prev = n.prev
                else: #no previous if first on list
                    self.head = n.next #head comes next
                    n.next.prev = None #prev value becomes none
            n = n.next
            
    def display(self):
        values=[]
        n=self.head
        while n!=None:
             values.append(str(n.value))
             n=n.next
        print ("List: ",",".join(values))
          
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.remove(4)
    l.display()
