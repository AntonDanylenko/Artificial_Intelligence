class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class Dlist:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self,value):
        if self.first==None:
            self.first = Node(value)
            self.last = self.first
        else:
            element = self.first
            while element.next!=None and element.value<value:
                element = element.next
            new = Node(value)
            element.next.previous = new
            new.next = element.next
            element.next = new
            new.previous = element

    def delete(self,value):
        element = self.first
        while element!=None:
            if element.value==value:
                if element.previous==None and element.next==None:
                    self.first = None
                    self.last = None
                elif element.previous==None:
                    element.next.previous = None
                    self.first = element.next
                elif element.next==None:
                    element.previous.next = None
                    self.last = element.previous
                else:
                    element.previous.next = element.next
                    element.next.previous = element.previous
                return True
            element = element.next
        return False

    def tolist(self):
        list = []
        element = self.first
        while element!=None:
            list.append(element.value)
            element = element.next
        return list

def main():
    dlist = Dlist()
    dlist.insert(0)
    dlist.insert(9)
    dlist.insert(5)
    dlist.insert(3)
    dlist.insert(8)
    dlist.insert(12)
    dlist.insert(9)
    dlist.insert(3)
    dlist.insert(6)
    dlist.insert(1)
    print(dlist.tolist())

main()
