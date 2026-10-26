class Node:

    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.previousNode = None

class StackWithLinkedList:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top == None:
            return True

    def push(self,data):
        newNode = Node(data)
        if self.isEmpty():
            self.top = newNode

        else:
            self.top.nextNode = newNode
            newNode.previousNode = self.top
            self.top = newNode

    def traverse(self):
        currentNode = self.top
        while currentNode != None:
            data = currentNode.data
            print(data,"--->",end=" ")
            currentNode = currentNode.previousNode

        print("Null")

    def pop(self):
        value = self.top.data
        self.top = self.top.previousNode
        print(value)


StckList = StackWithLinkedList()
StckList.push(2)
StckList.push(3)
StckList.pop()
StckList.push(4)
StckList.push(5)
StckList.push(6)

StckList.traverse()
StckList.pop()