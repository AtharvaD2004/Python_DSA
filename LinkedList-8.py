class Node:

    def  __init__(self,data):
        self.data = data
        self.nextNode = None
        self.previousNode = None

class QueueWithLinkedList:

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.rear == None:
            return True

    def Enqueue(self,data):
        newNode = Node(data)
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode

        else:
            self.rear.nextNode = newNode
            newNode.previousNode = self.rear
            self.rear = newNode


    def Dequeue(self):
        value = self.front.data
        self.front = self.front.nextNode
        print(value)
        self.front.previousNode = None

    def Traverse(self):
        currentNode = self.front
        while currentNode!= None:
            data = currentNode.data
            print(data,"--->",end=" ")
            currentNode = currentNode.nextNode
        print("Null")

queList = QueueWithLinkedList()
queList.Enqueue(1)
queList.Enqueue(2)
queList.Enqueue(3)
queList.Enqueue(4)
queList.Enqueue(5)
queList.Traverse()
queList.Dequeue()