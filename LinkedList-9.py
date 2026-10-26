class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.previousNode = None

class CircularQueueWithLinkedList:

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front == None:
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
            self.rear.nextNode = self.front

    def Dequeue(self):
        data = self.front.data
        print(data)
        self.front = self.front.nextNode
        self.rear.nextNode = self.front

    def Traverse(self):
        CurrentNode = self.front
        while True:
            data = CurrentNode.data
            print(data,"--->",end=" ")
            CurrentNode = CurrentNode.nextNode
            if self.rear.nextNode == CurrentNode:
                print("Null")
                break


cqueList = CircularQueueWithLinkedList()
cqueList.Enqueue(1)
cqueList.Enqueue(2)
cqueList.Enqueue(3)
cqueList.Enqueue(4)
cqueList.Enqueue(5)
cqueList.Traverse()
cqueList.Dequeue()
cqueList.Traverse()