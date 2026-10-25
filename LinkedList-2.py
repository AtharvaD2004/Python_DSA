# LINKING THE NODE , TRAVERSING AND INSERT A ELEMENT AT A SPECIFIC POSITION

class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList:

    def __init__(self):
        pass

    def insertElement(self,data,head):
        currentNode = head
        newNode = Node(data)

        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode

        currentNode.nextNode = newNode

    def specificPosition(self,position,head):
        if position == 0:
            newNode = Node(0)
            newNode.nextNode = head
            return newNode

        else:
            i = 0 
            currentNode = head
            while i < position -1:
                currentNode = currentNode.nextNode
                i+=1

            data = int(input("Enter the DATA : "))
            newNode = Node(data)
            temp = currentNode.nextNode
            newNode.nextNode = temp
            currentNode.nextNode = newNode


    def Traverse(self,head):
        currentNode = head

        while currentNode != None:
            data = currentNode.data
            print(data,"--->",end=" ")
            currentNode = currentNode.nextNode

        print("Null")

    

node = Node(1)
head = node

llist = LinkedList()

llist.insertElement(2,head)
llist.insertElement(4,head)
llist.insertElement(5,head)
llist.insertElement(6,head)
llist.Traverse(head)

position = int(input("Enter the Position : "))
if position == 0:
    head = llist.specificPosition(position,head)
    llist.Traverse(head)

else:
    llist.specificPosition(position,head)
    llist.Traverse(head)

