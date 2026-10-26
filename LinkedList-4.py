# INSERTING NODE AND TRAVERSING IN A DOUBLE LINKED LIST

class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.previousNode = None

class DoubleLinkedList:
    def __init__(self):
        pass

    def insertElement(self,data,head):
        currentNode = head
        newNode = Node(data)

        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode

        currentNode.nextNode = newNode
        newNode.previousNode = currentNode

    def forwardTraverse(self,head):

        currentNode = head
        while currentNode!= None:
            data = currentNode.data
            print(data,"---.",end=" ")
            currentNode = currentNode.nextNode

        print("Null")

    def backwardTraverse(self,head):

        currentNode = head
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode

        lastNode = currentNode

        while lastNode != None:
            data = lastNode.data
            print(data,"--->",end=" ")
            lastNode = lastNode.previousNode
        print("Null")

node = Node(1)
head = node

dblist = DoubleLinkedList()
dblist.insertElement(2,head)
dblist.insertElement(3,head)
dblist.insertElement(4,head)
dblist.insertElement(5,head)

dblist.forwardTraverse(head)
dblist.backwardTraverse(head)