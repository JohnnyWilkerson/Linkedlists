class Node():
    def __init__(self, data):
        self.data = data
        self.nextnode = None

class LinkedList():
    def __init__(self):
        self.head = None
    def addbegin(self, data):
        newnode = Node(data)
        newnode.nextnode = self.head
        self.head = newnode
    def addEnd(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            currentnode = self.head
            while currentnode.nextnode != None:
                currentnode = currentnode.nextnode
            currentnode.nextnode = newnode
    
    def deleteNode(self, removedata):
        currentnode = self.head
        while currentnode.data != removedata:
            currentnode = currentnode.nextnode
        
        prevnode = self.head
        
        if currentnode != self.head:
            while prevnode.nextnode != currentnode:
                prevnode = prevnode.nextnode
            prevnode.nextnode = currentnode.nextnode
        else:  
            self.head = currentnode.nextnode
            
    def deleteHead(self):
        currentnode = self.head
        self.head = currentnode.nextnode
    def deleteTail(self):
        currentnode = self.head
        prevnode = self.head
        while (currentnode.nextnode) != None:
            currentnode = currentnode.nextnode
        while prevnode.nextnode != currentnode:
                prevnode = prevnode.nextnode
        prevnode.nextnode = None   
        
    
    def printnodes(self):
        if self.head != None:
            currentnode = self.head
            while currentnode != None:
                print(currentnode.data)
                currentnode = currentnode.nextnode
        else:
            print, "It is empty. Add nodes."


list1 = LinkedList()
list1.addbegin("Jan")
list1.addbegin("Feb")
list1.addbegin("Mar")
list1.addEnd("April")
list1.printnodes()
#list1.deleteNode("Jan")
#list1.deleteHead()
#list1.deleteTail()
list1.printnodes()