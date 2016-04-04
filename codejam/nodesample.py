class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext
class UnorderedList:

    def __init__(self):
        self.head = None
    def isEmpty(self):
     return self.head == None
    def add(self,item):
     temp = Node(item)
     temp.setNext(self.head)
     self.head = temp
    def size(self):
     current = self.head
     count = 0
     while current != None:
        count = count + 1
        current = current.getNext()

     return count
mylist = UnorderedList()
print mylist.add(31)
temp = Node(93)
print temp.getData()