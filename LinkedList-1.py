# LINKING THE NODE AND ONLY FOR TRAVERSE

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
llist.insertElement(3,head)
llist.insertElement(4,head)
llist.insertElement(5,head)

llist.Traverse(head)