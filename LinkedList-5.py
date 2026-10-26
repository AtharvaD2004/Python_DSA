# INSERTING NODE , TRAVERSING AND INSERTING AT A SPECFIC POSITION IN A DOUBLE LINKED LIST

class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode =None
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

    def SpeciificPosition(self,position,head):
        if position == 0:
            currentNode = head
            data = 0
            newNode = Node(data)
            newNode.nextNode = currentNode
            currentNode.previousNode = newNode
            return newNode

        else:
            i = 0
            currentNode = head 
            while i < position-1:
                currentNode = currentNode.nextNode
                i+=1

            temp = currentNode.nextNode
            data = 10 
            newNode = Node(data)
            newNode.nextNode = temp 
            currentNode.nextNode = newNode
            newNode.previousNode = currentNode
            newNode.nextNode.previousNode = newNode


    def forwardTraverse(self,head):
        currentNode = head
        while currentNode != None:
            data = currentNode.data
            print(data,"--->",end=" ")
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

position = int(input("Enter the Position : "))
if position == 1:
    head = dblist.SpeciificPosition(position,head)
    dblist.forwardTraverse(head)
    dblist.backwardTraverse(head)

else:
    dblist.SpeciificPosition(position,head)
    dblist.forwardTraverse(head)
    dblist.backwardTraverse(head)